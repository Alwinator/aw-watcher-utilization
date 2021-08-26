from typing import Dict

import psutil


def get_utilization() -> Dict:
    cpu_times = psutil.cpu_times()
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_states = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq()

    memory_virtual = psutil.virtual_memory()
    memory_swap = psutil.swap_memory()

    disk_usage = psutil.disk_usage('/')
    disk_io_counters = psutil.disk_io_counters(perdisk=False)

    network_io_counters = psutil.net_io_counters(pernic=True)
    network_if_stats = psutil.net_if_stats()

    sensors_temperatures = psutil.sensors_temperatures()
    sensors_fans = psutil.sensors_fans()
    sensors_battery = psutil.sensors_battery()

    data = {
        "cpu": {
            "times": {
                "user": cpu_times.user,
                "nice": cpu_times.nice,
                "system": cpu_times.system,
                "idle": cpu_times.idle,
                "iowait": cpu_times.iowait,
                "irq": cpu_times.irq,
                "softirq": cpu_times.softirq,
                "steal": cpu_times.steal,
                "guest": cpu_times.guest,
            },
            "times_percent": {
                "user": cpu_times_percent.user,
                "nice": cpu_times_percent.nice,
                "system": cpu_times_percent.system,
                "idle": cpu_times_percent.idle,
                "iowait": cpu_times_percent.iowait,
                "irq": cpu_times_percent.irq,
                "softirq": cpu_times_percent.softirq,
                "steal": cpu_times_percent.steal,
                "guest": cpu_times_percent.guest,
            },
            "percent": cpu_percent,
            "count_logical": psutil.cpu_count(),
            "count": psutil.cpu_count(logical=False),
            "stats": {
                "ctx_switches": cpu_states.ctx_switches,
                "interrupts": cpu_states.interrupts,
                "soft_interrupts": cpu_states.soft_interrupts,
                "syscalls": cpu_states.syscalls
            },
            "freq": {
                "current": cpu_freq.current,
                "min": cpu_freq.min,
                "max": cpu_freq.max,
            },
            "loadavg": psutil.getloadavg()
        },
        "memory": {
            "virtual": {
                "total": memory_virtual.total,
                "available": memory_virtual.available,
                "percent": memory_virtual.percent,
                "used": memory_virtual.used,
                "free": memory_virtual.free,
                "active": memory_virtual.active,
                "inactive": memory_virtual.inactive,
                "buffers": memory_virtual.buffers,
                "cached": memory_virtual.cached,
                "shared": memory_virtual.shared,
            },
            "swap": {
                "total": memory_swap.total,
                "used": memory_swap.used,
                "free": memory_swap.free,
                "percent": memory_swap.percent,
                "sin": memory_swap.sin,
                "sout": memory_swap.sout
            }
        },
        "disk": {
            "usage": {
                "total": disk_usage.total,
                "used": disk_usage.used,
                "free": disk_usage.free,
                "percent": disk_usage.percent
            },
            "io_counters": {
                "read_count": disk_io_counters.read_count,
                "write_count": disk_io_counters.write_count,
                "read_bytes": disk_io_counters.read_bytes,
                "write_bytes": disk_io_counters.write_bytes,
                "read_time": disk_io_counters.read_time,
                "write_time": disk_io_counters.write_time,
                "read_merged_count": disk_io_counters.read_merged_count,
                "write_merged_count": disk_io_counters.write_merged_count,
                "busy_time": disk_io_counters.busy_time,
            }
        },
        "network": {
            "io_counters": {
                key: parse_net_io_counter(network_io_counters[key]) for key in network_io_counters
            },
            "net_if_stats": {
                key: parse_net_if_stat(network_if_stats[key]) for key in network_if_stats
            }
        },
        "sensors": {
            "temperatures": {
                key: list(map(parse_temperature, sensors_temperatures[key])) for key in sensors_temperatures
            },
            "fans": {
                key: list(map(parse_fan, sensors_fans[key])) for key in sensors_fans
            }
        },
        "other": {
            "users": list(map(parse_user, psutil.users())),
            "boot_time": psutil.boot_time()
        }
    }

    if sensors_battery:
        data["sensors"]["battery"] = {
            "percent": sensors_battery.percent,
            "secsleft": sensors_battery.secsleft,
            "power_plugged": sensors_battery.power_plugged,
        }

    return data


def parse_net_io_counter(counter):
    return {
        "bytes_sent": counter.bytes_sent,
        "bytes_recv": counter.bytes_recv,
        "packets_sent": counter.packets_sent,
        "packets_recv": counter.packets_recv,
        "errin": counter.errin,
        "errout": counter.errout,
        "dropin": counter.dropin,
        "dropout": counter.dropout,
    }


def parse_net_if_stat(stat):
    return {
        "isup": stat.isup,
        "duplex": stat.duplex,
        "speed": stat.speed,
        "mtu": stat.mtu,
    }


def parse_user(user):
    return {
        "name": user.name,
        "terminal": user.terminal,
        "host": user.host,
        "started": user.started,
        "pid": user.pid,
    }


def parse_temperature(temperature):
    return {
        "label": temperature.label,
        "current": temperature.current,
        "high": temperature.high,
        "critical": temperature.critical,
    }


def parse_fan(fan):
    return {
        "label": fan.label,
        "current": fan.current
    }
