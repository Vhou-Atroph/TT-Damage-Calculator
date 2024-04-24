all:

exe:
	pip install pyinstaller
	cargo build --release
	rename .\target\release\tt_damage_calculator.dll tt_damage_calculator.pyd
	move .\target\release\tt_damage_calculator.pyd .\src\tt_damage_calculator
	pyinstaller "Toontown Damage Calculator.spec"
	copy ".\src\tt_damage_calculator\assets" ".\dist\assets"
	copy ".\src\tt_damage_calculator\assets\img" ".\dist\assets\img"
	copy "./LICENSE" "./dist"

# creates a virtual environment for compiling the calculator
.ONESHELL:
env:
	python3 -m venv .venv --system-site-packages
	. .venv/bin/activate
	python3 -m pip install -r requirements.txt

exe-linux:
	cargo build --release
	mv -n target/release/libtt_damage_calculator.so src/tt_damage_calculator/tt_damage_calculator.so
	pyinstaller "Toontown Damage Calculator.spec"
	cp -r -f src/tt_damage_calculator/assets dist
	cp -f LICENSE dist/LICENSE
