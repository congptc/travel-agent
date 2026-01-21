
import os
from providers.base import PlacesProvider
import googlemaps
from config.config import CONFIG
from models.place import Place
from typing import List
from providers.places_provider_factory import PlacesProviderFactory

# Lấy API Keys từ GitHub Secrets
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

class GooglePlacesProvider(PlacesProvider):
    
    def __init__(self, api_key: str):
        self.client = googlemaps.Client(key=api_key)

    def search_nearby(
        self,
        lat: float,
        lng: float,
        radius_m: int
    ) -> List[Place]:
        
        # Khởi tạo client
        gmaps = googlemaps.Client(key=GOOGLE_PLACES_API_KEY)
        
        # Gọi API tìm kiếm địa điểm
        places_result = self.client.places_nearby(
            location=(lat, lng),
            radius=radius_m,
            type='tourist_attraction'
        )
        
        results = places_result.get('results', [])
        places = [
            Place(
                name=p.get("name"),
                address=p.get("vicinity"),
                rating=p.get("rating")
            ) 
            for p in results if p.get("rating", 0) >= CONFIG["min_rating"] and p.get("user_ratings_total",0) > CONFIG["min_user_ratings_total"]
        ]
        return places

PlacesProviderFactory._registry["google_places_api"] = GooglePlacesProvider    