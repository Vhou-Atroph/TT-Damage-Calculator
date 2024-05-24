//! TT-Damage-Calculator
//! Copyright (C) 2022-2024 Vhou-Atroph

use std::fs;

use pyo3::prelude::*;
use serde::{Serialize, Deserialize};

/// Struct for the Settings file
#[pyclass]
#[derive(Serialize,Deserialize)]
pub struct Settings {
    #[pyo3(get, set)]
    keybinds: Keybinds
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

/// Struct for the Keybinds portion of the Settings file
/// | Field            | Description                         |
/// |------------------|-------------------------------------|
/// | organic          | Keybind for the organic toggle      |
/// | lure             | Keybind for the lure toggle         |
/// | reset            | Keybind to reset calculations       |
/// | lock             | Keybind to toggle status lock       |
/// | defense          | Keybind to set cog defense          |
/// | negative_defense | Keybind to set negative cog defense |
/// | pin              | Keybind to toggle window pin status |
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
    negative_defense: String,
    #[pyo3(get, set)]
    pin: String,
}

#[pymethods]
impl Keybinds {

    /// Get default keybinds in case settings.toml keybinds are unusable for whatever reason
    #[staticmethod]
    pub fn default() -> Keybinds {
        Keybinds {
            organic: String::from("Shift_L"),
            lure: String::from("Control-l"),
            reset: String::from("Control-r"),
            lock: String::from("Control-x"),
            defense: String::from("Control-d"),
            negative_defense: String::from("Alt-d"),
            pin: String::from("Alt-Up")
        }
    }
}

/// Swap a toggle
#[pyfunction]
pub fn toggleswap(toggle:bool) -> bool {
    return !toggle
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
    let repo_ver = git_version("https://raw.githubusercontent.com/Vhou-Atroph/TT-Damage-Calculator/main/src/tt_damage_calculator/assets/version.txt").unwrap();
    let local_ver = fs::read_to_string(localfile).unwrap();
    if repo_ver == local_ver {return (true,repo_ver,local_ver);} (false,repo_ver,local_ver)
}
