class Heart:
    def __init__(self, heartbeat):
        self.heartbeat = heartbeat
        # TODO: use setter: self.heartbeat = heartbeat
        pass

    # TODO: property heartbeat
    @property
    def heartbeat(self):
        return self._heartbeat

    @heartbeat.setter
    def heartbeat(self, heartbeat):
        if heartbeat >= 0:
            self._heartbeat = heartbeat
        else:
            raise ValueError
    # TODO: setter heartbeat with validation
