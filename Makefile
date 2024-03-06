all:
exe:
	cargo build --release
	rename target\release\tt_damage_calculator.dll tt_damage_calculator.pyd
	move target\release\tt_damage_calculator.pyd src\tt_damage_calculator
	pyinstaller "Toontown Damage Calculator.spec"