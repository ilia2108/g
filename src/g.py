import nltk.data
import time
st = time.time()
fs = open('input', 'r', encoding='utf-8').read().split('\n')
is_text = fs[1]
tokenizer = nltk.data.load('russian.pickle')
sentences = tokenizer.tokenize(is_text.upper().strip())
cnt = 0
for s in sentences:
    if fs[0].upper() in s: cnt += 1
print (cnt)
print((time.time() - st) % 60)

