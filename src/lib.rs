//! TT-Damage-Calculator
//! Copyright (C) 2023 Vhou-Atroph

use pyo3::prelude::*;

use crate::gags::*;
use crate::calc::*;
use crate::settings::*;

#[pymodule]
fn rustygag(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    // Calc
    m.add_function(wrap_pyfunction!(cog_hp, m)?)?;
    m.add_function(wrap_pyfunction!(gag_calculator, m)?)?;
    m.add_function(wrap_pyfunction!(full_calc, m)?)?;
    m.add_function(wrap_pyfunction!(def_parse, m)?)?;
    m.add_function(wrap_pyfunction!(lvl_ind, m)?)?;
    m.add_function(wrap_pyfunction!(v2_loop, m)?)?;
    m.add_function(wrap_pyfunction!(advance_int, m)?)?;
    m.add_function(wrap_pyfunction!(advance_float, m)?)?;
    m.add_function(wrap_pyfunction!(lvl_ind_string, m)?)?;
    m.add_function(wrap_pyfunction!(calc_fin_string, m)?)?;

    // Gags
    m.add_class::<Gag>()?;

    // Settings
    m.add_class::<Settings>()?;
    m.add_function(wrap_pyfunction!(toggleswap, m)?)?;
    m.add_function(wrap_pyfunction!(orgswap,m)?)?;
    m.add_function(wrap_pyfunction!(comp_data, m)?)?;

    Ok(())
}

pub mod calc;
pub mod gags;
pub mod settings;