//! This is Rust module for the Toontown Damage Calculator. Its purpose is to help speed up operations performed by the program, which is written in Python.
//! 
//! BUILD INSTRUCTIONS:
//! To build a tt_settings.pyd file, you must have Rust installed. If you don't have Rust installed, you can find the download link at <https://www.rust-lang.org/tools/install>.
//! Once you have Rust installed, you need to navigate to the tt_settings file and run `cargo build --release` in your favorite terminal. Following this, navigate to target/releases and rename the generated tt_settings.dll file to tt_settings.pyd and place it in the "mod" folder of the main damage calculator.
//! Make sure the program runs with any changes you have made!

use std::fs;

use pyo3::prelude::*;
use serde::{Serialize, Deserialize};

#[pymodule]
fn tt_settings(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Settings>()?;
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
    reset: String,
    #[pyo3(get, set)]
    lure: String,
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