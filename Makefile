all:
windows:
	maturin build -i python
linux:
	maturin build
exe:
	cargo build --release
	ren target\release\rustygag.dll rustygag.pyd
	move target\release\rustygag.pyd src\tt_damage_calculator
	pyinstaller "Toontown Damage Calculator.spec"