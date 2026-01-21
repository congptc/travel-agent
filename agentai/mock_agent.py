from google import genai
from config.config import CONFIG, PROMPT_TEMPLATE
from agentai.base import AgentAI
from agentai.agent_factory import AgentFactory

GEMINI_API_KEY = "AIzaSyB_6đasadsadsad"

class MockAgent(AgentAI):
    
    """
    Implementation of AgentAI for Gemini API
    """
    def ai_summarize(self,places):
        client = genai.Client(api_key=GEMINI_API_KEY)
        #for m in genai.list_models():
         #   if 'generateContent' in m.supported_generation_methods:
         #       print(f"Model khả dụng: {m.name}")

        # Điền dữ liệu vào Prompt Template
        #prompt = PROMPT_TEMPLATE.format(places_data=places)
        #print("Prompt for Gemini AI:", prompt)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents= PROMPT_TEMPLATE,
        )
        print(f"Kết quả của Gemini: {response.text}")
        return response.text
    
AgentFactory._registry["mock"] = MockAgent