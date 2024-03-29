//! TT-Damage-Calculator
//! Copyright (C) 2022-2023 Vhou-Atroph

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

/// Function originally meant to parse defense strings to f64 values. No longer needed but still in the program for reference purposes.
#[pyfunction]
pub fn def_parse(mut val:String) -> f64 {
    val.pop();
    val.parse::<f64>().unwrap() / 100.0
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
pub fn cog_defense(gags:Vec<i64>,strength:f64) -> Vec<i64> {
    let mut newvec: Vec<i64> = Vec::new();
    for i in gags.iter() {newvec.push(i - (*i as f64 * strength).ceil() as i64);}
    newvec
}

/// Evaluates cog plating buff applicable in a round.
fn cog_plating(gags:Vec<i64>,lvl:i64) -> Vec<i64> {
    let mut newvec: Vec<i64> = Vec::new();
    for i in gags.iter() {
        let plating = (lvl as f64 * 1.5).floor() as i64;
        let dmg = i - plating;
        if dmg > 0 {newvec.push(dmg);} else {newvec.push(0);}
    }
    newvec
}

/// Evaluates the total damage of a group of gags used during a given round without lure.
fn damage_lureless(gags:Vec<i64>) -> i64 {
    if gags.len() > 1 {
        let mut gagdmg: i64 = 0;
        for i in gags.iter() {gagdmg+=i;}
        gagdmg+=(gagdmg as f64 * 0.2).ceil() as i64;
        return gagdmg
    }
    gags[0]
}

/// Evaluates the total damage of a group of gags used during a given round with lure.
fn damage_lured(gags:Vec<i64>) -> i64 {
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
pub fn gag_calculator(gags:Vec<i64>,lured:bool,defense:Option<f64>,plating:Option<i64>) -> i64 {
    let mut modlist: Vec<i64> = gags;
    let gagdmg: i64;
    if let Some(def) = defense { modlist = cog_defense(modlist,def) }
    if let Some(plate) = plating { modlist = cog_plating(modlist,plate) }
    if lured {gagdmg = damage_lured(modlist);}
    else {gagdmg = damage_lureless(modlist);}
    gagdmg
}

/// Full damage calculation for a given round in a cog battle.
#[pyfunction]
pub fn full_calc(trap:Vec<i64>,sound:Vec<i64>,throw:Vec<i64>,squirt:Vec<i64>,drop:Vec<i64>,lured:bool,defense:Option<f64>,plating:Option<i64>) -> i64 {
    let mut gagdmg: i64 = 0;
    let mut lured_loc = lured;
    if trap.len() == 1 && lured_loc {
        gagdmg+=gag_calculator(trap,false,defense,plating);
        lured_loc = false;
    }
    if !sound.is_empty() {
        gagdmg+=gag_calculator(sound,false,defense,plating);
        lured_loc = false;
    }
    if !throw.is_empty() {
        gagdmg+=gag_calculator(throw,lured_loc,defense,plating);
        lured_loc = false;
    }
    if !squirt.is_empty() {
        gagdmg+=gag_calculator(squirt,lured_loc,defense,plating);
        lured_loc = false;
    }
    if !drop.is_empty() && !lured_loc {
        gagdmg+=gag_calculator(drop,false,defense,plating);
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

/// Calculates what level of v2 cog a certain combination of gags would kill along with damage done.
/// This function is no longer present in the actual calculator, but remains here in case anyone wants to plug it back in at any point.
#[pyfunction]
pub fn v2_loop(trap:Vec<i64>,sound:Vec<i64>,throw:Vec<i64>,squirt:Vec<i64>,drop:Vec<i64>,lured:bool) -> PyResult<(i64,i64)> { // (dmg,lvl)
    let mut lvl: i64 = 0;
    while lvl < 20 {
        lvl+=1;
        let dmg = full_calc(trap.clone(),sound.clone(),throw.clone(),squirt.clone(),drop.clone(),lured,None,Some(lvl));
        match cog_hp(lvl).cmp(&dmg) {
            Ordering::Less => continue,
            Ordering::Equal => return Ok((lvl,dmg)),
            Ordering::Greater => return Ok((lvl-1,full_calc(trap,sound,throw,squirt,drop,lured,None,Some(lvl-1))))
        }
    }
    Ok((20,full_calc(trap,sound,throw,squirt,drop,lured,None,Some(20))))
}

/// Matches the current defense and plating values to correctly show how much defense/what level of v2 the calculator is working with.
#[pyfunction]
pub fn lvl_ind_string(lvl:u64,def:u64,v2:u64) -> String {
    match (def,v2) {
        (0,0) => format!("Level {}",lvl),
        (0,_) => format!("vs. V2.0 Level {}",v2),
        (_,0) => format!("Level {} ({}% defense)",lvl,def),
        (_,_) => format!("vs. V2.0 Level {} ({}% defense)",v2,def), // as was in the readme before, i don't actually know how v2s would calculate with a particular amount of defense. anything shown with this match guard is purely theoretical.
    }
}

/// Matches the current defense and plating values to give a calculation finish message to reflect the cog status effects.
#[pyfunction]
pub fn calc_fin_string(dmg:i64,lvl:i64,lured:bool,def:i64,v2:i64) -> String {
    match (def,v2) {
        (0,0) => format!("--------\nCalculation finished!\nDamage this round: {}\nWill kill: Level {} cogs\nLured: {}\n\n",dmg,lvl,lured),
        (0,_) => format!("--------\nCalculation finished!\nV.2.0 Level: {}\nDamage this round: {}\nWill kill: {}\nLured: {}\n\n",v2,dmg,dmg > cog_hp(v2),lured),
        (_,0) => format!("--------\nCalculation finished!\nDamage this round:{}\nDefense: {}%\nWill kill: Level {} cogs\nLured: {}\n\n",dmg,def,lvl,lured),
        (_,_) => format!("--------\nCalculation finished!\nV.2.0 Level: {}\nDamage this round: {}\nDefense: {}%\nWill kill: {}\nLured: {}\n\n",v2,dmg,def,dmg > cog_hp(v2),lured), // if more statuses like this are added, i will cry
    }
}