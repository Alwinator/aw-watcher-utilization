import logging
from typing import Dict

import psutil

logger = logging.getLogger(__name__)


def get_utilization() -> Dict:
    cpu_times = get_property_safe(lambda: psutil.cpu_times())
    cpu_times_percent = get_property_safe(lambda: psutil.cpu_times_percent())
    cpu_percent = get_property_safe(lambda: psutil.cpu_percent(interval=1, percpu=True))
    cpu_states = get_property_safe(lambda: psutil.cpu_stats())
    cpu_freq = get_property_safe(lambda: psutil.cpu_freq())

    memory_virtual = get_property_safe(lambda: psutil.virtual_memory())
    memory_swap = get_property_safe(lambda: psutil.swap_memory())

    disk_usage = get_property_safe(lambda: psutil.disk_usage('/'))
    disk_io_counters = get_property_safe(lambda: psutil.disk_io_counters(perdisk=False))

    network_io_counters = get_property_safe(lambda: psutil.net_io_counters(pernic=True))
    network_if_stats = get_property_safe(lambda: psutil.net_if_stats())

    sensors_temperatures = get_property_safe(lambda: psutil.sensors_temperatures())
    sensors_fans = get_property_safe(lambda: psutil.sensors_fans())
    sensors_battery = get_property_safe(lambda: psutil.sensors_battery())

    data = {
        "cpu": {
            "times": {
                "user": get_property_safe(lambda: cpu_times.user),
                "nice": get_property_safe(lambda: cpu_times.nice),
                "system": get_property_safe(lambda: cpu_times.system),
                "idle": get_property_safe(lambda: cpu_times.idle),
                "iowait": get_property_safe(lambda: cpu_times.iowait),
                "irq": get_property_safe(lambda: cpu_times.irq),
                "softirq": get_property_safe(lambda: cpu_times.softirq),
                "steal": get_property_safe(lambda: cpu_times.steal),
                "guest": get_property_safe(lambda: cpu_times.guest),
            },
            "times_percent": {
                "user": get_property_safe(lambda: cpu_times_percent.user),
                "nice":  get_property_safe(lambda: cpu_times_percent.nice),
                "system":  get_property_safe(lambda: cpu_times_percent.system),
                "idle":  get_property_safe(lambda: cpu_times_percent.idle),
                "iowait":  get_property_safe(lambda: cpu_times_percent.iowait),
                "irq":  get_property_safe(lambda: cpu_times_percent.irq),
                "softirq":  get_property_safe(lambda: cpu_times_percent.softirq),
                "steal":  get_property_safe(lambda: cpu_times_percent.steal),
                "guest":  get_property_safe(lambda: cpu_times_percent.guest),
            },
            "percent": cpu_percent,
            "count_logical": psutil.cpu_count(),
            "count": get_property_safe(lambda: psutil.cpu_count(logical=False)),
            "stats": {
                "ctx_switches":  get_property_safe(lambda: cpu_states.ctx_switches),
                "interrupts":  get_property_safe(lambda: cpu_states.interrupts),
                "soft_interrupts":  get_property_safe(lambda: cpu_states.soft_interrupts),
                "syscalls":  get_property_safe(lambda: cpu_states.syscalls)
            },
            "freq": {
                "current": get_property_safe(lambda: cpu_freq.current),
                "min": get_property_safe(lambda: cpu_freq.min),
                "max": get_property_safe(lambda: cpu_freq.max),
            },
            "loadavg": get_property_safe(lambda: psutil.getloadavg())
        },
        "memory": {
            "virtual": {
                "total":  get_property_safe(lambda: memory_virtual.total),
                "available": get_property_safe(lambda: memory_virtual.available),
                "percent": get_property_safe(lambda: memory_virtual.percent),
                "used": get_property_safe(lambda: memory_virtual.used),
                "free": get_property_safe(lambda: memory_virtual.free),
                "active": get_property_safe(lambda: memory_virtual.active),
                "inactive": get_property_safe(lambda: memory_virtual.inactive),
                "buffers": get_property_safe(lambda: memory_virtual.buffers),
                "cached": get_property_safe(lambda: memory_virtual.cached),
                "shared": get_property_safe(lambda: memory_virtual.shared),
            },
            "swap": {
                "total": get_property_safe(lambda: memory_swap.total),
                "used": get_property_safe(lambda: memory_swap.used),
                "free": get_property_safe(lambda: memory_swap.free),
                "percent": get_property_safe(lambda: memory_swap.percent),
                "sin": get_property_safe(lambda: memory_swap.sin),
                "sout": get_property_safe(lambda: memory_swap.sout)
            }
        },
        "disk": {
            "usage": {
                "total": get_property_safe(lambda: disk_usage.total),
                "used": get_property_safe(lambda: disk_usage.used),
                "free": get_property_safe(lambda: disk_usage.free),
                "percent": get_property_safe(lambda: disk_usage.percent)
            },
            "io_counters": {
                "read_count": get_property_safe(lambda: disk_io_counters.read_count),
                "write_count": get_property_safe(lambda: disk_io_counters.write_count),
                "read_bytes": get_property_safe(lambda: disk_io_counters.read_bytes),
                "write_bytes": get_property_safe(lambda: disk_io_counters.write_bytes),
                "read_time": get_property_safe(lambda: disk_io_counters.read_time),
                "write_time": get_property_safe(lambda: disk_io_counters.write_time),
                "read_merged_count": get_property_safe(lambda: disk_io_counters.read_merged_count),
                "write_merged_count": get_property_safe(lambda: disk_io_counters.write_merged_count),
                "busy_time": get_property_safe(lambda: disk_io_counters.busy_time),
            }
        },
        "network": {
            "io_counters": iterate_safe(lambda x: parse_net_io_counter(x), network_io_counters),
            "net_if_stats": iterate_safe(lambda x: parse_net_if_stat(x), network_if_stats),
        },
        "sensors": {
            "temperatures": iterate_safe(lambda x: list(map(parse_temperature, x)), sensors_temperatures),
            "fans": iterate_safe(lambda x: list(map(parse_fan, x)), sensors_fans),
            "battery": {
                "percent": get_property_safe(lambda: sensors_battery.percent),
                "secsleft": get_property_safe(lambda: sensors_battery.secsleft),
                "power_plugged": get_property_safe(lambda: sensors_battery.power_plugged),
            }
        },
        "other": {
            "users": get_property_safe(lambda: list(map(parse_user, psutil.users()))),
            "boot_time": get_property_safe(lambda: psutil.boot_time())
        }
    }

    return data


def iterate_safe(callback, dict_object):
    if not dict_object:
        return None

    return {
        key: callback(dict_object[key]) for key in dict_object
    }


def get_property_safe(callback):
    try:
        return callback()
    except AttributeError:
        return None
    except Exception as ex:
        logger.exception(ex)
        return None


def parse_net_io_counter(counter):
    return {
        "bytes_sent": get_property_safe(lambda: counter.bytes_sent),
        "bytes_recv": get_property_safe(lambda: counter.bytes_recv),
        "packets_sent": get_property_safe(lambda: counter.packets_sent),
        "packets_recv": get_property_safe(lambda: counter.packets_recv),
        "errin": get_property_safe(lambda: counter.errin),
        "errout": get_property_safe(lambda: counter.errout),
        "dropin": get_property_safe(lambda: counter.dropin),
        "dropout": get_property_safe(lambda: counter.dropout),
    }


def parse_net_if_stat(stat):
    return {
        "isup": get_property_safe(lambda: stat.isup),
        "duplex": get_property_safe(lambda: stat.duplex),
        "speed": get_property_safe(lambda: stat.speed),
        "mtu": get_property_safe(lambda: stat.mtu),
    }


def parse_user(user):
    return {
        "name": get_property_safe(lambda: user.name),
        "terminal": get_property_safe(lambda: user.terminal),
        "host": get_property_safe(lambda: user.host),
        "started": get_property_safe(lambda: user.started),
        "pid": get_property_safe(lambda: user.pid),
    }


def parse_temperature(temperature):
    return {
        "label": get_property_safe(lambda: temperature.label),
        "current": get_property_safe(lambda: temperature.current),
        "high": get_property_safe(lambda: temperature.high),
        "critical": get_property_safe(lambda: temperature.critical),
    }


def parse_fan(fan):
    return {
        "label": get_property_safe(lambda: fan.label),
        "current": get_property_safe(lambda: fan.current)
    }
