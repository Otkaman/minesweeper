def is_pangram(sentence):
    sentence = sentence.replace(' ','').lower()
    alf = 'abcdefghijklmnopqrstuvwxyz'
    res = sorted(list(set(sentence)))
    result = ''.join(res)
    return alf in result
