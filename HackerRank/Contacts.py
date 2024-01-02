from collections import Counter

def contacts(queries):
    cnter = Counter()
    result = []
    for cmd, word in queries:
        if cmd == 'add':
            for i in range(1, len(word) + 1):
                cnter.update([word[0:i]])
        else:
            result.append (cnter[word])
    return result
