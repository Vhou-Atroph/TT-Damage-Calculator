//! TT-Damage-Calculator
//! Copyright (C) 2022 Vhou-Atroph

use std::fs;

use pyo3::prelude::*;
use serde::{Serialize, Deserialize};

#[pymodule]
fn tt_settings(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Settings>()?;
    m.add_function(wrap_pyfunction!(toggleswap, m)?)?;
    Ok(())
}

/// Struct for the Settings file
#[pyclass]
#[derive(Serialize,Deserialize)]
struct Settings {
    #[pyo3(get, set)]
    keybinds: Keybinds
}

/// Struct for the Keybinds portion of the Settings file
#[pyclass]
#[derive(Serialize,Deserialize,Clone)]
struct Keybinds {
    #[pyo3(get, set)]
    organic: String,
    #[pyo3(get, set)]
    lure: String,
    #[pyo3(get, set)]
    reset: String,
    #[pyo3(get, set)]
    lock: String,
    #[pyo3(get, set)]
    defense: String,
    #[pyo3(get, set)]
    v2: String,
    #[pyo3(get, set)]
    pin: String,
}

#[pymethods]
impl Settings {

    /// Opens the Settings file.
    #[new]
    fn new(file:&str) -> Self {
        let data =  fs::read_to_string(file).unwrap();
        let settings: Settings = toml::from_str(data.as_str()).unwrap();
        settings
    }
}

/// Swap a toggle
#[pyfunction]
pub fn toggleswap(toggle:bool) -> bool {
    if toggle {return false;} true
}