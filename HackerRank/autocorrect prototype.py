from collections import defaultdict

def getSearchResults(words, queries):
    word_map = defaultdict(list)
    
    # Preprocess words to store sorted tuples of characters as keys
    for word in words:
        word_map[tuple(sorted(word))].append(word)
    
    result = []
    
    for query in queries:
        # Sort the query and convert to a tuple for matching
        sorted_query = tuple(sorted(query))
        # Fetch the anagrams from the preprocessed map and sort them
        result.append(sorted(word_map[sorted_query]))
    
    return result

words = ['allot', 'cat', 'peach', 'dusty', 'act', 'cheap']
queries = ['tac', 'study', 'peahc']
print(getSearchResults(words, queries))
