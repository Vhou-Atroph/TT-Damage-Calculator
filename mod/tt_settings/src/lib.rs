use pyo3::prelude::*;

#[pymodule]
fn tt_settings(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Keybind>()?;
    Ok(())
}

/// Struct for a Keybind
#[pyclass]
struct Keybind {
    #[pyo3(get, set)]
    key_id: String
}

#[pymethods]
impl Keybind {

    /// Create a new Keybind
    #[new]
    fn new(key_id:String) -> Self {
        Self {key_id}
    }
}