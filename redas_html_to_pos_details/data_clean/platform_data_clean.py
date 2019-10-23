from abc import ABC, abstractmethod


class PlatformDataClean(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def data_clean(self):
        pass
