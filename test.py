import json

from aw_watcher_utilization.util import get_utilization

print(json.dumps(get_utilization(), indent=2))
