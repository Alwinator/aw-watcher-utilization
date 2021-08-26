# WIP: aw-watcher-utilization

An [Activity Watch](https://github.com/ActivityWatch/activitywatch) watcher which monitors CPU, RAM, disk, network and sensor usage.

It is basically a [psutil](https://github.com/giampaolo/psutil) wrapper for [Activity Watch](https://github.com/ActivityWatch/activitywatch). I have only left out some too detailed information.

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
pyinstaller --clean aw_linux.spec
```
### Test
```
python test.py
```