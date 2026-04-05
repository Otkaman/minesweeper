def is_pangram(sentence):
    sentence = sentence.replace(' ','').lower()

    alf = 'abcdefghijklmnopqrstuvwxyz'
    answer = [str(sentence[i]) for i in range(len(sentence))]
    res = sorted(list(set(answer)))
    result = ''.join(res)
    return alf in result
