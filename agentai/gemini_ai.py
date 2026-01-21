import os
from google import genai
from config.config import CONFIG, PROMPT_TEMPLATE
from agentai.base import AgentAI
from agentai.agent_factory import AgentFactory

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class GeminiAI(AgentAI):
    
    """
    Implementation of AgentAI for Gemini API
    """
    def ai_summarize(self,places):
        client = genai.Client(api_key=GEMINI_API_KEY)
        print(f"Key API GENMINI: {GEMINI_API_KEY}")
        
        # Điền dữ liệu vào Prompt Template
        #prompt = PROMPT_TEMPLATE.format(places_data=places)
        #print("Prompt for Gemini AI:", prompt)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents= PROMPT_TEMPLATE,
        )
        #print(f"Kết quả của Gemini: {response.text}")
        return response.text
    
AgentFactory._registry["gemini"] = GeminiAI