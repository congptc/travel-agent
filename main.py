import providers
import agentai
from config.config import CONFIG
from providers.places_provider_factory import PlacesProviderFactory
from agentai.agent_factory import AgentFactory
from noti.noti_factory import NotiFactory


if __name__ == "__main__":
    
    #places_provider = PlacesProviderFactory.create("mock")
    #agent_ai = AgentFactory.create("mock")
    #noti = NotiFactory.create("mock")
    agent_ai = AgentFactory.create("gemini")
    noti = NotiFactory.create("telegram")
    #summary = agent_ai.ai_summarize("")
    #noti.send(f"KẾ HOẠCH CUỐI TUẦN CHO BẠN\n{summary}")
    noti.send("KẾ HOẠCH CUỐI TUẦN CHO BẠN\n*** Làng gốm Bát Tràng Địa chỉ chính xác: Bát Tràng, Gia Lâm, Hà Nội***")
