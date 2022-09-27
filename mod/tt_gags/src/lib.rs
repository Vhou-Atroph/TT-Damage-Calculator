//! This is Rust module for the Toontown Damage Calculator. Its purpose is to help speed up operations performed by the program, which is written in Python.
//! 
//! BUILD INSTRUCTIONS:
//! To build a tt_gags.pyd file, you must have Rust installed. If you don't have Rust installed, you can find the download link at <https://www.rust-lang.org/tools/install>.
//! Once you have Rust installed, you need to navigate to the tt_gags file and run `cargo build --release` in your favorite terminal. Following this, navigate to target/releases and rename the generated tt_gags.dll file to tt_gags.pyd and place it in the "mod" folder of the main damage calculator.
//! Make sure the program runs with any changes you have made!

use pyo3::prelude::*;

#[pymodule]
fn tt_gags(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Gag>()?;
    Ok(())
}

/// Basic struct for a Gag.
#[pyclass]
struct Gag {
    #[pyo3(get, set)]
    gtype: String,
    #[pyo3(get, set)]
    name: String,
    #[pyo3(get, set)]
    track: Vec<u64>,
    #[pyo3(get, set)]
    level: u8,
    #[pyo3(get, set)]
    dmg: u64,
}

#[pymethods]
impl Gag {

    /// Creates a new Gag struct.
    #[new]
    fn new(gtype:String,name:String,track:Vec<u64>,level:u8,dmg:u64) -> Self {
        Self { gtype, name, track, level, dmg }
    }

    /// Returns the damage an organic gag of a certain type does.
    fn organic(&self) -> PyResult<u64> {
        Ok(org(self.dmg))
    }
}

/// Evaluates the amount of damage a gag will do when organic.
fn org(n:u64) -> u64 {
    let org_boost_f = n as f64 * 0.1;
    if org_boost_f < 1.0 {return n+1_u64}
    n + org_boost_f.floor() as u64
}