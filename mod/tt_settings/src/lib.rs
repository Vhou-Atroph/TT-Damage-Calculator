//! TT-Damage-Calculator
//! Copyright (C) 2022 Vhou-Atroph

use std::fs;

use pyo3::prelude::*;
use serde::{Serialize, Deserialize};

/// Module for managing settings, keybind functions, and handling the update checker. This module is implemented in Rust.
#[pymodule]
fn tt_settings(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Settings>()?;
    m.add_function(wrap_pyfunction!(toggleswap, m)?)?;
    m.add_function(wrap_pyfunction!(orgswap,m)?)?;
    m.add_function(wrap_pyfunction!(comp_data, m)?)?;
    Ok(())
}

/// Struct for the Settings file
#[pyclass]
#[derive(Serialize,Deserialize)]
pub struct Settings {
    #[pyo3(get, set)]
    keybinds: Keybinds
}

/// Struct for the Keybinds portion of the Settings file
#[pyclass]
#[derive(Serialize,Deserialize,Clone)]
pub struct Keybinds {
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
    return !toggle
}

/// Specifically swap the organic gags toggle, which is significantly more painful than the checkbox ones!
#[pyfunction]
pub fn orgswap(toggle:bool) -> (bool,String,String,String) { // (state,indicator,bg,activebg)
    if toggle {return (false,String::from("OFF"),String::from("#1888D3"),String::from("#186AD3"));} 
    (true,String::from("ON"),String::from("darkorange"),String::from("orange"))
}

/// Get GitHub version.txt file
#[tokio::main]
async fn git_version(gitfile:&str) -> Result<String,Box<dyn std::error::Error>> {
    let data = reqwest::get(gitfile).await?.text().await?;
    Ok(data)
}

/// Compare local and git repo versions.txt file
#[pyfunction]
pub fn comp_data(localfile:String) -> (bool,String,String) { // (diff,repo,loc)
    let repo_ver = git_version("https://raw.githubusercontent.com/Vhou-Atroph/TT-Damage-Calculator/main/mod/version.txt").unwrap();
    let local_ver = fs::read_to_string(localfile).unwrap();
    if repo_ver == local_ver {return (true,repo_ver,local_ver);} (false,repo_ver,local_ver)
}