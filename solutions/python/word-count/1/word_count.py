from collections import Counter
def count_words(sentence):
    sentence = sentence.lower()
    symbols = ['\n','\t','!','\"','?',',','.',';',':','/','&','@','$','^','%','_']
    for symbol in symbols:
        sentence = sentence.replace(symbol,' ')
    
    words = [word.strip("'") for word in sentence.split()]
    result = [wrd for wrd in words if wrd]
    counts = Counter(result)
    return dict(counts)
