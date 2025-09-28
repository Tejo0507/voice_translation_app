
import requests

class ElevenLabsTTS:
    def __init__(self, api_key, voice_id):
        self.api_key = api_key
        self.voice_id = voice_id
        self.api_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"

