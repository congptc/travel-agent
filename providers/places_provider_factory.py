
from providers.base import PlacesProvider

class PlacesProviderFactory:

    _registry = {}

    @staticmethod
    def create(provider_name: str, **kwargs) -> PlacesProvider:
        try:
            cls = PlacesProviderFactory._registry[provider_name.lower()]
        except KeyError:
            raise ValueError(f"Unknown provider: {provider_name}")

        return cls(**kwargs)
