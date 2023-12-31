def decodeHuff(root, s):
    current = root
    for c in s: 
        current = current.left if c == '0' else current.right
        if current.data!='\0':
            print(current.data, end = '')
            current = root