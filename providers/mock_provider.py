from providers.base import PlacesProvider
from models.place import Place
from typing import List
from providers.places_provider_factory import PlacesProviderFactory

class MockPlacesProvider(PlacesProvider):
    """
    Provider giả để test hệ thống
    """

    def search_nearby(
        self,
        lat: float,
        lng: float,
        radius_m: int
    ) -> List[Place]:

        return [
            Place(
                name= 'Công viên trung tâm',
                address = '123 Đường A',
                rating = 4.5
            ),
            Place(
                name = 'Quán cà phê đẹp',
                address = '123 Đường A',
                rating = 1.2
            )
        ]

PlacesProviderFactory._registry["mock"] = MockPlacesProvider