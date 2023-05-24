## Get started

* Update your tools
```
python -m pip install --upgrade pip setuptools wheel virtualenv
```

* Make sure you have installed proper GUI backend for matplotlib
```
sudo apt install python3-tk
```

* Create virtual environment and install dependencies
```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel virtualenv
python -m pip install -r ./requirements.txt
```

* Run calculations
```
python -m main
```
