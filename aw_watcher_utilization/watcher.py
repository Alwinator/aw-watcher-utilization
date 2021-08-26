import logging
import datetime
import psutil
from time import sleep
from typing import Dict

from aw_core.models import Event
from aw_client import ActivityWatchClient

from aw_watcher_utilization.config import watcher_config
from aw_watcher_utilization.settings import Settings
from aw_watcher_utilization.util import get_utilization

logger = logging.getLogger(__name__)


class UtilizationWatcher:
    def __init__(self, testing=False):
        config_section = "aw-watcher-utilization" if not testing else "aw-watcher-utilization-testing"
        self.settings = Settings(watcher_config[config_section])

        self.client = ActivityWatchClient("aw-watcher-utilization", testing=testing)
        self.bucket_id = "{}_{}".format(self.client.client_name, self.client.client_hostname)

    def run(self):
        logger.info("aw-watcher-utilization started")

        # Initialization
        sleep(1)

        self.client.create_bucket(self.bucket_id, event_type='utilization', queued=True)

        # Start table checking loop
        with self.client:
            self.heartbeat_loop()

    def ping(self, utilization: Dict):
        event = Event(
            timestamp=datetime.datetime.now(datetime.timezone.utc),
            data=utilization
        )
        # 2 seconds processing time
        self.client.heartbeat(self.bucket_id, event, pulsetime=self.settings.poll_time+1+2, queued=True)

    def heartbeat_loop(self):
        while True:
            try:
                table_height = get_utilization()
                self.ping(table_height)
                sleep(self.settings.poll_time)
            except KeyboardInterrupt:
                logger.info("aw-watcher-utilization stopped by keyboard interrupt")
                break
