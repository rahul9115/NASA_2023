from summarizer import TransformerSummarizer
body=""
with open("19710021280_clean.txt","r") as f:
    body=f.read()
print(body)
GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
full = ''.join(GPT2_model(body, min_length=60))
print(full)