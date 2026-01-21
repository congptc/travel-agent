from noti.base import NotiChanel

class NotiFactory:
    _registry = {}

    @staticmethod
    def create(provider_name: str, **kwargs) -> NotiChanel:
        try:
            cls = NotiFactory._registry[provider_name.lower()]
        except KeyError:
            raise ValueError(f"Unknown provider: {provider_name}")

        return cls(**kwargs)
