//! This is Rust module for the Toontown Damage Calculator. Its purpose is to help speed up operations performed by the program, which is written in Python.
//! 
//! BUILD INSTRUCTIONS:
//! To build a tt_gags.pyd file, you must have Rust installed. If you don't have Rust installed, you can find the download link at <https://www.rust-lang.org/tools/install>.
//! Once you have Rust installed, you need to navigate to the tt_gags file and run `cargo build --release` in your favorite terminal. Following this, navigate to target/releases and rename the generated tt_gags.dll file to tt_gags.pyd and place it in the "mod" folder of the main damage calculator.
//! Make sure the program runs with any changes you have made!

#[macro_use]
extern crate cpython;

use cpython::{Python,PyResult};

py_module_initializer!(tt_calc, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    Ok(())
});