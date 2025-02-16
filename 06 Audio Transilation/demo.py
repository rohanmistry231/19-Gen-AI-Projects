import openai 
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

audio_file = open("Recording.mp3", "rb")
output = openai.Audio.translate("whisper-1", audio_file)
print(output)