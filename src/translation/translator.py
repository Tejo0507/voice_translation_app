import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class NeuralTranslator:
    def __init__(self, model_name="facebook/nllb-200-distilled-600M", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)
