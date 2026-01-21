from abc import ABC, abstractmethod

class AgentAI(ABC):
    """
    Abstract base class cho mọi Agent AI API
    """

    @abstractmethod
    def ai_summarize(self,places):
        """
        Tóm tắt địa điểm sử dụng AI
        """
        raise NotImplementedError