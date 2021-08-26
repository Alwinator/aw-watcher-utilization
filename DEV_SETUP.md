# Dev Setup
## Install
```
virtualenv venv # create virtual environment
source ./venv/bin/activate # activate virtual environment
poetry install # install required packages
```
## Run
```
poetry run aw-watcher-utilization [--testing] [-v] [--verbose]
```
### Build
```
pyinstaller --clean pyinstaller.spec
```
### Test
```
python test.py
```