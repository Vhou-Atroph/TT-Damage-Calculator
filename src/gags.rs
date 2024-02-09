//! TT-Damage-Calculator
//! Copyright (C) 2022-2024 Vhou-Atroph

use pyo3::prelude::*;

/// This struct is for a basic Gag, which is a thing that toons use against cogs in the wild and wacky game Toontown Rewritten (or any of the other private servers I guess.)
/// | Field | Description                                     |
/// |-------|-------------------------------------------------|
/// | gtype | Whether the gag is a regular gag or an SOS Card |
/// | name  | The name of the gag.                            |
/// | track | The gag track a gag belongs to as a String      |
/// | level | The level that the gag is                       |
/// | dmg   | The amount of damage a gag may do to a  cog.    |
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
        if self.gtype == "Gag" && org_val {return Ok((self.org().expect("An error happened!"),format!("Organic {}",self.name)))}
        Ok((self.dmg,self.name.clone()))
    }

    /// Returns the amount of damage a gag will do when organic.
    fn org(&self) -> PyResult<i64> {
        if self.track == "Throw" {
            let org_boost_f = self.dmg as f64 * 0.05;
            if org_boost_f < 1.0 {return Ok(self.dmg + 1_i64)}
            return Ok(self.dmg + org_boost_f.floor() as i64)
            }
            else {
                let org_boost_f = self.dmg as f64 * 0.1;
                if org_boost_f < 1.0 {return Ok(self.dmg + 1_i64)}
                Ok(self.dmg + org_boost_f.floor() as i64)
            }
    }
}