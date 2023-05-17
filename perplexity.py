import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


haikus = {"pond": "traipsing through the pond, a mythical pond of dreams, in the pond england.", 
          "love": "ove discovered me, a red whites and love is not, my friend called love is", 
          "winter": "winter foreboding, leaves you thought the winter sun, cold winter is joy", 
          "flower": "do not fake jackson, dried dying flower blossoms, the flower head now"}

# pre-trained GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
for theme in haikus.keys():
  inputs = tokenizer.encode(haikus[theme], return_tensors='pt')

  with torch.no_grad():
      outputs = model(inputs, labels=inputs)
      loss = outputs.loss
      perplexity = torch.exp(loss)  

  print(theme +  " haiku perplexity :", perplexity.item())

