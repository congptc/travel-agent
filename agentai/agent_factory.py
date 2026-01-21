from agentai.base import AgentAI

class AgentFactory:

    _registry = {
    }

    @staticmethod
    def create(provider_name: str, **kwargs) -> AgentAI:
        try:
            cls = AgentFactory._registry[provider_name.lower()]
        except KeyError:
            raise ValueError(f"Unknown provider: {provider_name}")

        return cls(**kwargs)
