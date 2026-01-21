import providers
import agentai
from config.config import CONFIG
from providers.places_provider_factory import PlacesProviderFactory
from agentai.agent_factory import AgentFactory
from noti.noti_factory import NotiFactory


if __name__ == "__main__":
    
    places_provider = PlacesProviderFactory.create("mock")
    agent_ai = AgentFactory.create("mock")
    noti = NotiFactory.create("mock")

    raw_places = places_provider.search_nearby(
        lat=CONFIG["location"][0],
        lng=CONFIG["location"][1],
        radius_m=CONFIG["radius"]
    )
    if raw_places:
        summary = agent_ai.ai_summarize(raw_places[:10])
        noti.send(f"📅 **KẾ HOẠCH CUỐI TUẦN CHO BẠN**\n{summary}")
    else:
        noti.send("Hôm nay không tìm thấy địa điểm nào phù hợp tiêu chí rồi!")
