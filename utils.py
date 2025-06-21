from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load directly from Hugging Face Hub
model_name = "shumukhe/coqa-t5-bot"
import logging
logging.basicConfig(level=logging.DEBUG)


tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
def get_answer(question, context):
    input_text = f"question: {question} context: {context}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=64)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)