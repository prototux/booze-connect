from . import settings

class bmap():

    class settingsClass:
        def __init__(self, read, write):
            self.ANR = settings.ANRSettings(read, write)

    def __init__(self, read, write):

        # Callbacks
        self.dev_read = read
        self.dev_write = write

        self.settings = self.settingsClass(self.dev_read, self.dev_write)


