from abc import ABC, abstractmethod
from datetime import datetime


# --- Слой Хранилищ (Storage Layer) ---
class Storage(ABC):
    """Абстрактный класс для логики хранения (Локально, S3, Облако)"""

    @abstractmethod
    def upload(self, file_path, data): pass

    @abstractmethod
    def delete(self, file_path): pass


class LocalStorage(Storage):
    def upload(self, file_path, date): print(f"Сохранение {file_path} на диск")

    def delete(self, file_path): print(f"Удаление с диска")


class S3Storage(Storage):
    def upload(self, file_path, date): print(f"Загрузка в S3 бакет")

    def delete(self, file_path): print(f"Удаление из S3")