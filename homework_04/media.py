from abc import ABC, abstractmethod

class MediaFile(ABC):
    def __init__(self, name, size, owner, storage: Storage):
        self.name = name
        self.size = size
        self.owner = owner
        self.created_at = datetime.now()
        self.storage = storage  # Инъекция зависимости (DI)

    def save(self, data):
        self.storage.upload(self.name, data)

    def delete(self):
        self.storage.delete(self.name)

    @abstractmethod
    def play(self):
        """У каждого типа медиа свой"""
        pass