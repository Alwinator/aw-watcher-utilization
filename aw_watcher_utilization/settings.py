class Settings:
    def __init__(self, config_section):
        self.poll_time = config_section.getfloat("poll_time")

        assert self.poll_time > 0
