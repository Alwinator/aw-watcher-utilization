from configparser import ConfigParser
from aw_core.config import load_config

default_settings = {
    "poll_time": "5"  # seconds
}
default_testing_settings = {
    "poll_time": "5"  # seconds
}

default_config = ConfigParser()
default_config['aw-watcher-utilization'] = default_settings
default_config['aw-watcher-utilization-testing'] = default_testing_settings
watcher_config = load_config("aw-watcher-utilization", default_config)
