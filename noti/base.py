from abc import ABC, abstractmethod

class NotiChanel(ABC):
    """
    Abstract base class cho mọi kênh thông báo
    """

    @abstractmethod
    def send(self,summary):
        """
        Gửi thông báo với nội dung tóm tắt
        """
        raise NotImplementedError