//! This is Rust module for the Toontown Damage Calculator. Its purpose is to help speed up operations performed by the program, which is written in Python.
//! 
//! BUILD INSTRUCTIONS:
//! To build a tt_calc.pyd file, you must have Rust installed. If you don't have Rust installed, you can find the download link at <https://www.rust-lang.org/tools/install>.
//! Once you have Rust installed, you need to navigate to the tt_calc file and run `cargo build --release` in your favorite terminal. Following this, navigate to target/releases and rename the generated tt_calc.dll file to tt_calc.pyd and place it in the "mod" folder of the main damage calculator.
//! Make sure the program runs with any changes you have made!

#[macro_use]
extern crate cpython;

use cpython::{Python,PyResult};

py_module_initializer!(tt_calc, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "cog_hp", py_fn!(py, cog_hp(lvl:u16)))?;
    Ok(())
});

/// Basic function to evaluate health of any cog levels 1 through 20.
fn cog_hp(_:Python,lvl:u16) -> PyResult<u16> {
    match lvl {
        1..=11 => return Ok((lvl+1) * (lvl+2)),
        12..=20 => return Ok((lvl+1) * (lvl+2) + 14),
        _ => panic!("Cog levels cannot exceed 20 or be lower than 1.")
    }
}