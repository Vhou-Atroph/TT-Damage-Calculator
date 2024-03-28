//! TT-Damage-Calculator
//! Copyright (C) 2022-2024 Vhou-Atroph

use pyo3::prelude::*;

use std::cmp::Ordering;

/// Basic function to evaluate health of any cog levels 1 through 20.
#[pyfunction]
pub fn cog_hp(lvl:i64) -> i64 {
    match lvl {
        1..=11 => (lvl+1) * (lvl+2),
        12..=20 => (lvl+1) * (lvl+2) + 14,
        _ => panic!("Cog levels cannot exceed 20 or be lower than 1.")
    }
}

/// Iterate list to the next value (for i64 values)
#[pyfunction]
pub fn advance_int(list:Vec<i64>,entry:i64) -> i64 {
    let ind = list.iter().position(|&i| i == entry).unwrap();
    if let Some(x) = list.get(ind+1) {return *x} 0
}

/// Iterate list to the next value (for f64 values)
/// (I really wish pyfunction supported generics)
#[pyfunction]
pub fn advance_float(list:Vec<f64>,entry:f64) -> f64 {
    let ind = list.iter().position(|&i| i == entry).unwrap();
    if let Some(x) = list.get(ind+1) {return *x} 0.0
}

/// Evaluates cog defense buff applicable in a round.
pub fn cog_defense(gags:&Vec<i64>,strength:f64) -> Vec<i64> {
    let mut newvec: Vec<i64> = Vec::new();
    for i in gags.iter() {newvec.push(i - (*i as f64 * strength).ceil() as i64);}
    newvec
}

/// Evaluates the flat damage bonus from negative cog defense.
fn damage_negative_defense(gags:&Vec<i64>, strength:f64) -> i64 {
    let sum: i64 = gags.iter().sum();
    (sum as f64 * strength).ceil() as i64
}

/// Evaluates the total damage of a group of gags used during a given round without lure.
fn damage_lureless(gags:&Vec<i64>) -> i64 {
    if gags.len() > 1 {
        let mut gagdmg: i64 = 0;
        for i in gags.iter() {gagdmg+=i;}
        gagdmg+=(gagdmg as f64 * 0.2).ceil() as i64;
        return gagdmg
    }
    gags[0]
}

/// Evaluates the total damage of a group of gags used during a given round with lure.
fn damage_lured(gags:&Vec<i64>) -> i64 {
    if gags.len() > 1 {
        let mut gagdmg: i64 = 0;
        for i in gags.iter() {gagdmg+=i;}
        gagdmg+=(gagdmg as f64 * 0.5).ceil() as i64 + (gagdmg as f64 * 0.2).ceil() as i64;
        return gagdmg
    }
    gags[0] + (gags[0] as f64 * 0.5).ceil() as i64
}

/// Evaluates which functions to perform for a particular gag usage round.
#[pyfunction]
pub fn gag_calculator(gags:Vec<i64>, lured:bool, defense:Option<f64>, neg_defense:Option<f64>) -> i64 {
    let mut modlist: Vec<i64> = gags;
    let mut gagdmg: i64;
    if let Some(def) = defense { modlist = cog_defense(&modlist, def) }
    if lured {gagdmg = damage_lured(&modlist);}
    else {gagdmg = damage_lureless(&modlist);}
    if let Some(neg_def) = neg_defense { gagdmg = gagdmg + damage_negative_defense(&modlist, neg_def) }
    gagdmg
}

/// Full damage calculation for a given round in a cog battle.
#[pyfunction]
pub fn full_calc(trap:Vec<i64>,
    sound:Vec<i64>,
    throw:Vec<i64>,
    squirt:Vec<i64>,
    drop:Vec<i64>,
    no_group: i64,
    lured:bool,
    defense:Option<f64>,
    neg_defense:Option<f64>) -> i64 {
    let mut gagdmg: i64 = no_group;
    let mut lured_loc = lured;
    if trap.len() == 1 && lured_loc {
        gagdmg+=gag_calculator(trap,false,defense,neg_defense);
        lured_loc = false;
    }
    if !sound.is_empty() {
        gagdmg+=gag_calculator(sound,false,defense,neg_defense);
        lured_loc = false;
    }
    if !throw.is_empty() {
        gagdmg+=gag_calculator(throw,lured_loc,defense,neg_defense);
        lured_loc = false;
    }
    if !squirt.is_empty() {
        gagdmg+=gag_calculator(squirt,lured_loc,defense,neg_defense);
        lured_loc = false;
    }
    if !drop.is_empty() && !lured_loc {
        gagdmg+=gag_calculator(drop,false,defense,neg_defense);
    }
    gagdmg
}

/// Calculates the level of cog a particular amount of damage would destroy.
#[pyfunction]
pub fn lvl_ind(dmg:i64) -> i64 {
    let mut lvl: i64 = 0;
    while lvl < 20 {
        lvl+=1;
        match cog_hp(lvl).cmp(&dmg) {
            Ordering::Less => continue,
            Ordering::Equal => return lvl,
            Ordering::Greater => return lvl-1,
        }
    }
    20
}

/// Matches the current defense and plating values to correctly show how much defense the calculator is working with.
#[pyfunction]
pub fn lvl_ind_string(lvl:u64, def:i64, neg_def:i64) -> String {
    match (def, neg_def) {
        (0, 0) => format!("Level {}",lvl),
        (_, 0) => format!("Level {} ({}% defense)",lvl, def),
        (0, _) => format!("Level {} (-{}% defense)",lvl, neg_def),
        (_, _) => format!("Level {} (+{}%/-{}% defense)",lvl, def, neg_def)
    }
}

/// Struct to create an output for the calculation history box when a user chooses to reset the calculation.
#[pyclass]
pub struct CalculationResults {
    #[pyo3(get, set)]
    dmg: i64,
    #[pyo3(get, set)]
    lvl: i64,
    #[pyo3(get, set)]
    lured: bool,
    #[pyo3(get, set)]
    pdef: f64,
    #[pyo3(get, set)]
    ndef: f64
}

#[pymethods]
impl CalculationResults {
    #[new]
    pub fn new(dmg:i64, lvl:i64, lured:bool, pdef:f64, ndef:f64) -> Self {
        Self { dmg, lvl, lured, pdef, ndef }
    }

    /// Builds the calculation history string
    pub fn build(&self) -> String {
        format!(
            "--------\nDamage this round:{}\nWill kill: Level {} cogs\nLured: {}\n{}\n",
            self.dmg, self.lvl, self.lured, self.give_defense())
    }

    /// Matches the defense values to create a string to reflect the most recent battle's calculations in calculation history.
    fn give_defense(&self) -> String {
        let pos_def = (self.pdef * 100.) as i64;
        let neg_def = (self.ndef * 100.) as i64;
        match (pos_def, neg_def) {
            (0, 0) => format!(""),
            (_, 0) => format!("Defense: {}%\n", pos_def),
            (0, _) => format!("Defense: -{}%\n", neg_def),
            (_, _) => format!("Defense: +{}%/-{}%\n", pos_def, neg_def)
        }
    }
}