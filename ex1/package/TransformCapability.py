from abc import ABC , abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._is_transformed = False

    @abstractmethod
    def transform(self):
        pass
    
    @abstractmethod
    def revert(self):
        pass