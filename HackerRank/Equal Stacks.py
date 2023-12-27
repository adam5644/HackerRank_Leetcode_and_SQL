def equalStacks(h1, h2, h3):
    # Reverse the lists to start popping from the end (which is the top of the stack)
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    
    # Calculate the initial sum of heights for each stack
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    
    # Continue removing cylinders from the tallest stack until all are equal or any stack is empty
    while not (s1 == s2 == s3):
        # If any stack is empty, we cannot proceed further
        if not h1 or not h2 or not h3:
            return 0

        # Identify the tallest stack and remove the top cylinder
        if s1 >= s2 and s1 >= s3:
            s1 -= h1.pop()
        elif s2 >= s1 and s2 >= s3:
            s2 -= h2.pop()
        elif s3 >= s1 and s3 >= s2:
            s3 -= h3.pop()
    
    # At this point, all stacks are equal height
    return s1  # Or s2 or s3, since they are all the same

# The rest of the code (main part) remains the same