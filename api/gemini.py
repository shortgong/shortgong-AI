import config, json
from ai.promport import promport
import google.generativeai as genai

genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-3.5-flash-lite")

def make_video_content(draft: str):
    response = model.generate_content(promport(draft))
    print(response.text)
    result = json.loads(response.text)
    return result['title'], result['content']