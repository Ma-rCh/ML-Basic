from media import MediaFile

class AudioFile(MediaFile):
    def __init__(self, compression):
        super().__init__()
        self.compression = compression

    def play(self):
        def play_audio(): pass


    def convert(self):
        pass

class PhotoFile(MediaFile):
    def __init__(self, resolution):
        super().__init__()
        self.resolution = resolution

    def play(self):
        def show(): pass

class VideoFile(MediaFile):
    def __init__(self, resolution):
        super().__init__()
        self.format = format

    def play(self):
        def open_player(): pass
        def close_player(): pass