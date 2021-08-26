# aw-watcher-utilization

An [Activity Watch](https://github.com/ActivityWatch/activitywatch) watcher that monitors CPU, RAM, disk, network, and sensor usage.

It is basically a [psutil](https://github.com/giampaolo/psutil) wrapper for [Activity Watch](https://github.com/ActivityWatch/activitywatch). I have only left out some too detailed information.

## Install
1. Download the latest release [here](https://github.com/Alwinator/aw-watcher-utilization/releases)
2. Unzip and move the aq-watcher-utilization folder to your activity watch directory
3. Go to the [config directory](https://docs.activitywatch.net/en/latest/directories.html#config). In the aw-qt directory you should find an aw-qt.toml file.
Add the aw-table-utilization to autostart_modules to enable auto-start. It should look like this:

```
[aw-qt]
autostart_modules = ["aw-server", "aw-watcher-afk", "aw-watcher-window", "aw-watcher-utilization"]
```

## Testing
Unfortunately, I have a limited amount of computers, so I bug reports are always very welcomed!

## Contribute
Thanks in advance!

See [DEV_SETUP](DEV_SETUP.md).