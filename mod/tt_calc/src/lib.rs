#[macro_use]
extern crate cpython;

use cpython::{Python,PyResult};

py_module_initializer!(tt_calc, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "cog_hp", py_fn!(py, cog_hp(lvl:u16)))?;
    Ok(())
});

fn cog_hp(_:Python,lvl:u16) -> PyResult<u16> {
    match lvl {
        1..=11 => return Ok((lvl+1) * (lvl+2)),
        12..=20 => return Ok((lvl+1) * (lvl+2) + 14),
        _ => panic!("Cog levels cannot exceed 20 or be lower than 1.")
    }
}