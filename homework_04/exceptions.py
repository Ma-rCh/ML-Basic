class FileNotFound(Exception):
    pass


class NotEnoughSpace(Exception):
   pass

class NotEnoughDiskSpace(NotEnoughSpace):
   pass

class EoF(Exception):
    pass

class ResourceNotFound(ErrorLoading):
    pass

class ErrorLoading(Exception):
    def __init__(self, messege):
        self.messege = messege
        super().__init__(self.messege)