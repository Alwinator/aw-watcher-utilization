# aw-watcher-utilization
[![Create releases for Linux and Windows](https://github.com/Alwinator/aw-watcher-utilization/actions/workflows/build-release.yml/badge.svg)](https://github.com/Alwinator/aw-watcher-utilization/actions/workflows/build-release.yml)
[![stars](https://img.shields.io/github/stars/Alwinator/aw-watcher-utilization)](https://github.com/Alwinator/aw-watcher-utilization)

An [ActivityWatch](https://github.com/ActivityWatch/activitywatch) watcher that monitors CPU, RAM, disk, network, and sensor usage. It is basically a [`psutil`](https://github.com/giampaolo/psutil) wrapper for [ActivityWatch](https://github.com/ActivityWatch/activitywatch). I have only left out some information that was too detailed.

It creates a data dump every `n` seconds. (`n` can be changed in the config, default 5 seconds). Here is an example data dump:
<details>
<summary>Expand to see the data dump</summary>
<pre>
{
  "cpu": {
    "times": {
      "user": 1322.13,
      "nice": 8.4,
      "system": 295.14,
      "idle": 70291.32,
      "iowait": 88.89,
      "irq": 0.0,
      "softirq": 46.51,
      "steal": 0.0,
      "guest": 0.0
    },
    "times_percent": {
      "user": 8.0,
      "nice": 0.0,
      "system": 1.8,
      "idle": 88.5,
      "iowait": 0.9,
      "irq": 0.0,
      "softirq": 0.9,
      "steal": 0.0,
      "guest": 0.0
    },
    "percent": [
      1.0,
      7.0,
      2.0,
      1.0,
      2.0,
      1.0,
      0.0,
      1.0,
      0.0,
      1.0,
      4.0,
      9.1,
      2.9,
      1.0,
      0.0,
      1.0,
      1.0,
      0.0,
      0.0,
      1.0,
      2.0,
      0.0,
      1.0,
      0.0
    ],
    "count_logical": 24,
    "count": 12,
    "stats": {
      "ctx_switches": 37394300,
      "interrupts": 17828493,
      "soft_interrupts": 5348055,
      "syscalls": 0
    },
    "freq": {
      "current": 2511.235,
      "min": 2200.0,
      "max": 3700.0
    },
    "loadavg": [
      0.41,
      0.4,
      0.45
    ]
  },
  "memory": {
    "virtual": {
      "total": 33646522368,
      "available": 25273651200,
      "percent": 24.9,
      "used": 7725912064,
      "free": 20975898624,
      "active": 2285453312,
      "inactive": 9401901056,
      "buffers": 254865408,
      "cached": 4689846272,
      "shared": 196804608
    },
    "swap": {
      "total": 17179865088,
      "used": 0,
      "free": 17179865088,
      "percent": 0.0,
      "sin": 0,
      "sout": 0
    }
  },
  "disk": {
    "usage": {
      "total": 1967397240832,
      "used": 179485396992,
      "free": 1687902023680,
      "percent": 9.6
    },
    "io_counters": {
      "read_count": 106909,
      "write_count": 82554,
      "read_bytes": 4226650624,
      "write_bytes": 1836332032,
      "read_time": 14305,
      "write_time": 106840,
      "read_merged_count": 30221,
      "write_merged_count": 83702,
      "busy_time": 141588
    }
  },
  "network": {
    "io_counters": {
      "lo": {
        "bytes_sent": 3811967,
        "bytes_recv": 3811967,
        "packets_sent": 33176,
        "packets_recv": 33176,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
      },
      "enp39s0": {
        "bytes_sent": 7710002,
        "bytes_recv": 101937768,
        "packets_sent": 62853,
        "packets_recv": 90218,
        "errin": 0,
        "errout": 0,
        "dropin": 972,
        "dropout": 0
      },
      "wlo1": {
        "bytes_sent": 781046,
        "bytes_recv": 987573,
        "packets_sent": 5576,
        "packets_recv": 5028,
        "errin": 0,
        "errout": 0,
        "dropin": 23,
        "dropout": 0
      },
      "br-b9a41ca7844a": {
        "bytes_sent": 0,
        "bytes_recv": 0,
        "packets_sent": 0,
        "packets_recv": 0,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
      },
      "br-303b82cbab45": {
        "bytes_sent": 0,
        "bytes_recv": 0,
        "packets_sent": 0,
        "packets_recv": 0,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
      },
      "docker0": {
        "bytes_sent": 0,
        "bytes_recv": 0,
        "packets_sent": 0,
        "packets_recv": 0,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
      },
      "vmnet1": {
        "bytes_sent": 0,
        "bytes_recv": 0,
        "packets_sent": 499,
        "packets_recv": 0,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
      },
      "vmnet8": {
        "bytes_sent": 0,
        "bytes_recv": 0,
        "packets_sent": 501,
        "packets_recv": 0,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
      }
    },
    "net_if_stats": {
      "lo": {
        "isup": true,
        "duplex": 0,
        "speed": 0,
        "mtu": 65536
      },
      "enp39s0": {
        "isup": true,
        "duplex": 2,
        "speed": 1000,
        "mtu": 1500
      },
      "wlo1": {
        "isup": true,
        "duplex": 0,
        "speed": 0,
        "mtu": 1500
      },
      "br-b9a41ca7844a": {
        "isup": false,
        "duplex": 0,
        "speed": 65535,
        "mtu": 1500
      },
      "br-303b82cbab45": {
        "isup": false,
        "duplex": 0,
        "speed": 65535,
        "mtu": 1500
      },
      "docker0": {
        "isup": false,
        "duplex": 0,
        "speed": 65535,
        "mtu": 1500
      },
      "vmnet1": {
        "isup": true,
        "duplex": 0,
        "speed": 0,
        "mtu": 1500
      },
      "vmnet8": {
        "isup": true,
        "duplex": 0,
        "speed": 0,
        "mtu": 1500
      }
    }
  },
  "sensors": {
    "temperatures": {
      "nvme": [
        {
          "label": "Composite",
          "current": 39.85,
          "high": 81.85,
          "critical": 84.85
        },
        {
          "label": "Sensor 1",
          "current": 39.85,
          "high": 65261.85,
          "critical": 65261.85
        },
        {
          "label": "Sensor 2",
          "current": 44.85,
          "high": 65261.85,
          "critical": 65261.85
        },
        {
          "label": "Composite",
          "current": 38.85,
          "high": 81.85,
          "critical": 84.85
        },
        {
          "label": "Sensor 1",
          "current": 38.85,
          "high": 65261.85,
          "critical": 65261.85
        },
        {
          "label": "Sensor 2",
          "current": 45.85,
          "high": 65261.85,
          "critical": 65261.85
        }
      ],
      "k10temp": [
        {
          "label": "Tctl",
          "current": 45.75,
          "high": null,
          "critical": null
        },
        {
          "label": "Tdie",
          "current": 45.75,
          "high": null,
          "critical": null
        }
      ],
      "iwlwifi_1": [
        {
          "label": "",
          "current": 38.0,
          "high": null,
          "critical": null
        }
      ]
    },
    "fans": {}
  },
  "other": {
    "users": [
      {
        "name": "alwin",
        "terminal": ":1",
        "host": ":1",
        "started": 1629982080.0,
        "pid": 11504
      }
    ],
    "boot_time": 1629980632.0
  }
}
</pre>
</details>

On supported devices, you also see fan and battery metrics.

## Install
1. Download the latest release [here](https://github.com/Alwinator/aw-watcher-utilization/releases).
2. Unzip as `aw-watcher-utilization` folder.
3. Move the folder to your [ActivityWatch directory](https://docs.activitywatch.net/en/latest/directories.html#data).
4. Go to the [config directory](https://docs.activitywatch.net/en/latest/directories.html#config). In the `aw-qt` directory, find the `aw-qt.toml` file.
5. Add the `aw-table-utilization` to `autostart_modules` to enable auto-start. It should look like this:

`aw-qt.toml`:
```
[aw-qt]
autostart_modules = ["aw-server", "aw-watcher-afk", "aw-watcher-window", "aw-watcher-utilization"]
```
5. [Linux only]: Make the executable file in the `aw-watcher-utilization` folder executable:
```
chmod +x ./aw-watcher-utilization
```

## Testing
Unfortunately, I have a limited number of computers, so bug reports are always very welcome!

## Contribute
See [`DEV_SETUP.md`](DEV_SETUP.md).

Thanks in advance!
