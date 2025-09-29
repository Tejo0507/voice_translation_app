import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class NeuralTranslator:
    def __init__(self, model_name="facebook/nllb-200-distilled-600M", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)

    def get_lang_token_id(self, lang_code):
        lang_token = f"<2{lang_code}>"
        token_id = self.tokenizer.get_vocab().get(lang_token)
        if token_id is None:
            raise ValueError(f"Language token {lang_token} not found in tokenizer vocabulary.")
        return token_id

    def translate(self, text, src_lang="eng_Latn", tgt_lang="fra_Latn"):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        forced_bos_token_id = self.get_lang_token_id(tgt_lang)
        generated_tokens = self.model.generate(
            **inputs,
            forced_bos_token_id=forced_bos_token_id
        )
        translated_text = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return translated_text
