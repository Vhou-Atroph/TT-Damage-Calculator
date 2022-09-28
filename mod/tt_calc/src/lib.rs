//! TT-Damage-Calculator
//! Copyright (C) 2022 Vhou-Atroph


use pyo3::prelude::*;

#[pymodule]
fn tt_calc(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cog_hp, m)?)?;
    m.add_function(wrap_pyfunction!(gag_calculator, m)?)?;
    m.add_function(wrap_pyfunction!(full_calc, m)?)?;
    m.add_function(wrap_pyfunction!(def_parse, m)?)?;
    Ok(())
}

/// Basic function to evaluate health of any cog levels 1 through 20.
/// ```
/// use tt_calc::*;
/// 
/// fn lvl12s() {
///     println!("Level 12 cogs have {} health!",cog_hp(12).expect("An error has occured"));
/// }
/// ```
#[pyfunction]
fn cog_hp(lvl:u64) -> u64 {
    match lvl {
        1..=11 => (lvl+1) * (lvl+2),
        12..=20 => (lvl+1) * (lvl+2) + 14,
        _ => panic!("Cog levels cannot exceed 20 or be lower than 1.")
    }
}

#[pyfunction]
fn def_parse(val:&str) -> f64 {
    match val {
        "10%" => return 0.1,
        "15%" => return 0.15,
        "20%" => return 0.2,
        "25%" => return 0.25,
        _ => 0.0
    }
}

/// Evaluates cog defense buff applicable in a round.
/// ```
/// use tt_calc::*;
/// 
/// fn round_w_def() {
///     let dmg = damage_lureless(cog_defense(vec![50,21,21,21],0.20));
///     println!("The damage dealt this round was: {}",dmg);
/// }
/// ```
fn cog_defense(gags:Vec<u64>,strength:f64) -> Vec<u64> {
    let mut newvec: Vec<u64> = Vec::new();
    for i in gags.iter() {newvec.push(i - (*i as f64 * strength).ceil() as u64);}
    newvec
}

/// Evaluates cog plating buff applicable in a round.
/// ```
/// use tt_calc::*;
/// 
/// fn round_w_plating() {
///     let dmg = damage_lureless(cog_plating(vec![50,21,21,21],10));
///     println!("The damage dealt this round was: {}",dmg);
/// }
/// ```
fn cog_plating(gags:Vec<u64>,lvl:u64) -> Vec<u64> {
    let mut newvec: Vec<u64> = Vec::new();
    for i in gags.iter() {newvec.push(i - (lvl as f64 * 1.5).floor() as u64);}
    newvec
}

/// Evaluates the total damage of a group of gags used during a given round without lure.
/// ```
/// use tt_calc::*;
/// 
/// fn avg_snd_users() {
///     let kills_10s = vec![50,21,21,21];
///     let dmg = damage_lureless(kills_10s);
///     println!("{} is more than enough damage to kill level 10 cogs.",dmg);
/// }
/// ```
fn damage_lureless(gags:Vec<u64>) -> u64 {
    if gags.len() > 1 {
        let mut gagdmg: u64 = 0;
        for i in gags.iter() {gagdmg+=i;}
        gagdmg+=(gagdmg as f64 * 0.2).ceil() as u64;
        return gagdmg
    }
    gags[0]
}

/// Evaluates the total damage of a group of gags used during a given round with lure.
/// ```
/// use tt_calc::*;
/// 
/// fn avg_thrw_users() {
///     let kills_14s = vec![132,27];
///     let dmg = damage_lured(kills_14s);
///     println!("{} is more than enough damage to kill level 14 cogs.",dmg);
/// }
/// ```
fn damage_lured(gags:Vec<u64>) -> u64 {
    if gags.len() > 1 {
        let mut gagdmg: u64 = 0;
        for i in gags.iter() {gagdmg+=i;}
        gagdmg+=(gagdmg as f64 * 0.5).ceil() as u64 + (gagdmg as f64 * 0.2).ceil() as u64;
        return gagdmg
    }
    gags[0] + (gags[0] as f64 * 0.5).ceil() as u64
}

/// Evaluates which functions to perform for a particular gag usage round.
#[pyfunction]
fn gag_calculator(gags:Vec<u64>,lured:bool,defense:Option<f64>,plating:Option<u64>) -> u64 {
    let mut modlist: Vec<u64> = gags;
    let gagdmg: u64;
    if let Some(def) = defense { modlist = cog_defense(modlist,def) }
    if let Some(plate) = plating { modlist = cog_plating(modlist,plate) }
    if lured {gagdmg = damage_lured(modlist);}
    else {gagdmg = damage_lureless(modlist);}
    gagdmg
}

/// Full damage calculation for a given round in a cog battle.
#[pyfunction]
fn full_calc(trap:Vec<u64>,sound:Vec<u64>,throw:Vec<u64>,squirt:Vec<u64>,drop:Vec<u64>,lured:bool,defense:Option<f64>,plating:Option<u64>) -> u64 {
    let mut gagdmg: u64 = 0;
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