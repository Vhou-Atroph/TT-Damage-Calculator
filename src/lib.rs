//! TT-Damage-Calculator
//! Copyright (C) 2022-2024 Vhou-Atroph

use pyo3::prelude::*;

use crate::gags::*;
use crate::calc::*;
use crate::settings::*;

#[pymodule]
fn tt_damage_calculator(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    // Calc
    m.add_class::<CalculationResults>()?;
    m.add_function(wrap_pyfunction!(cog_hp, m)?)?;
    m.add_function(wrap_pyfunction!(gag_calculator, m)?)?;
    m.add_function(wrap_pyfunction!(full_calc, m)?)?;
    m.add_function(wrap_pyfunction!(lvl_ind, m)?)?;
    m.add_function(wrap_pyfunction!(advance_int, m)?)?;
    m.add_function(wrap_pyfunction!(advance_float, m)?)?;
    m.add_function(wrap_pyfunction!(lvl_ind_string, m)?)?;

    // Gags
    m.add_class::<Gag>()?;

    // Settings
    m.add_class::<Settings>()?;
    m.add_function(wrap_pyfunction!(toggleswap, m)?)?;
    m.add_function(wrap_pyfunction!(comp_data, m)?)?;

    Ok(())
}

pub mod calc;
pub mod gags;
pub mod settings;
