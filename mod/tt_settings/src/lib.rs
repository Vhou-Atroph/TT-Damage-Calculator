use pyo3::prelude::*;

#[pymodule]
fn tt_settings(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    Ok(())
}

/// Struct for a Keybind
#[pyclass]
struct Keybind {

}