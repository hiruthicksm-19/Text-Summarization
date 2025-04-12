from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

def abstractive_summary(text, max_len=60):
    input_ids = tokenizer("summarize: " + text, return_tensors="pt", truncation=True, max_length=512).input_ids
    output = model.generate(input_ids, max_length=max_len, num_beams=4, early_stopping=True)
    return tokenizer.decode(output[0], skip_special_tokens=True)