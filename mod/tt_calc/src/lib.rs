//! This is Rust module for the Toontown Damage Calculator. Its purpose is to help speed up operations performed by the program, which is written in Python.
//! 
//! BUILD INSTRUCTIONS:
//! To build a tt_calc.pyd file, you must have Rust installed. If you don't have Rust installed, you can find the download link at <https://www.rust-lang.org/tools/install>.
//! Once you have Rust installed, you need to navigate to the tt_calc file and run `cargo build --release` in your favorite terminal. Following this, navigate to target/releases and rename the generated tt_calc.dll file to tt_calc.pyd and place it in the "mod" folder of the main damage calculator.
//! Make sure the program runs with any changes you have made!


use pyo3::prelude::*;

#[pymodule]
fn tt_calc(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cog_hp, m)?)?;
    m.add_function(wrap_pyfunction!(gag_calculator, m)?)?;
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
        1..=11 => return (lvl+1) * (lvl+2),
        12..=20 => return (lvl+1) * (lvl+2) + 14,
        _ => panic!("Cog levels cannot exceed 20 or be lower than 1.")
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
fn gag_calculator(gags:Vec<u64>,lured:u8,defense:Option<f64>,plating:Option<u64>) -> u64 {
    let mut modlist: Vec<u64> = gags.clone();
    let gagdmg: u64;
    match defense {
        Some(def) => modlist = cog_defense(modlist,def),
        None => {}
    }
    match plating {
        Some(plat) => modlist = cog_plating(modlist,plat),
        None => {}
    }
    if lured == 1 {gagdmg = damage_lured(modlist);}
    else {gagdmg = damage_lureless(modlist);}
    gagdmg
}