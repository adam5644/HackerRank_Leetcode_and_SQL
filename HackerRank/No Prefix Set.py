def noPrefix(words):   
    prefixes = set()
    prev_words = set()
    for w in words:
        # Check if w is prefix of any previous word
        if w in prefixes:
            print(f"BAD SET \n{w}")
            return
        # Check if any previous word is a prefix of w
        for i in range(1, len(w)+1):
            if w[:i] in prev_words:
                print(f"BAD SET \n{w}")
                return
            prefixes.add(w[:i])
        prev_words.add(w)
    print("GOOD SET")