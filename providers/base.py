from abc import ABC, abstractmethod
from typing import List
from models.place import Place


class PlacesProvider(ABC):
    """
    Abstract base class cho mọi Places API
    """

    @abstractmethod
    def search_nearby(
        self,
        lat: float,
        lng: float,
        radius_m: int
    ) -> List[Place]:
        """
        Tìm địa điểm quanh 1 vị trí
        """
        raise NotImplementedError
