import os
from google import genai
from config.config import CONFIG, PROMPT_TEMPLATE
from agentai.base import AgentAI
from agentai.agent_factory import AgentFactory

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class GeminiAI(AgentAI):

    def __init__(self):
        # Nạp Key ngay khi đối tượng được tạo ra
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("LỖI: Không tìm thấy GEMINI_API_KEY trên GitHub Secrets!")
    
    """
    Implementation of AgentAI for Gemini API
    """
    def ai_summarize(self,places):
        client = genai.Client(api_key=self.api_key)
        # Điền dữ liệu vào Prompt Template
        #prompt = PROMPT_TEMPLATE.format(places_data=places)
        #print("Prompt for Gemini AI:", prompt)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents= PROMPT_TEMPLATE,
        )
        print(f"Kết quả của Gemini: {response.text}")
        return response.text
    
AgentFactory._registry["gemini"] = GeminiAI
