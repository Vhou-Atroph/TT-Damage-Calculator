//! TT-Damage-Calculator
//! Copyright (C) 2022 Vhou-Atroph

use pyo3::prelude::*;

/// Module for the Gag class. This module is implemented in Rust.
#[pymodule]
fn tt_gags(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Gag>()?;
    Ok(())
}

/// Basic struct for a Gag.
#[pyclass]
pub struct Gag {
    #[pyo3(get, set)]
    gtype: String,
    #[pyo3(get, set)]
    name: String,
    #[pyo3(get, set)]
    track: String,
    #[pyo3(get, set)]
    level: u8,
    #[pyo3(get, set)]
    dmg: i64,
}

#[pymethods]
impl Gag {

    /// Creates a new Gag struct.
    #[new]
    pub fn new(gtype:String,name:String,track:String,level:u8,dmg:i64) -> Self {
        Self { gtype, name, track, level, dmg }
    }

    /// Returns the damage an organic gag of a certain type does.
    pub fn button_press(&self,org_val:bool) -> PyResult<(i64,String)> { // (damage,name)
        if self.gtype == "Gag" && org_val {return Ok((org(self.dmg),format!("Organic {}",self.name)))}
        Ok((self.dmg,self.name.clone()))
    }
}

/// Evaluates the amount of damage a gag will do when organic.
fn org(n:i64) -> i64 {
    let org_boost_f = n as f64 * 0.1;
    if org_boost_f < 1.0 {return n+1_i64}
    n + org_boost_f.floor() as i64
}