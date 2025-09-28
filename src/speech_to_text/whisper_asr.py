
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration

class WhisperASR:
    def __init__(self, model_name="openai/whisper-large-v3-turbo", device="cuda"):
        self.device = device if torch.cuda.is_available() else "cpu"
        self.processor = WhisperProcessor.from_pretrained(model_name)
        self.model = WhisperForConditionalGeneration.from_pretrained(model_name).to(self.device)

    def transcribe(self, audio_chunk):
        inputs = self.processor(audio_chunk, sampling_rate=16000, return_tensors="pt").to(self.device)
        generated_ids = self.model.generate(inputs.input_features)
        transcription = self.processor.decode(generated_ids[0])
        return transcription
