# 
pattern = 'DIIDDD'

result = ''
current_sequence = ''
next_number = 1

# Traverse each character in the pattern
for char in pattern:
    # Append the current number to the sequence
    current_sequence += str(next_number)
    if char == 'I':
        # If the character is 'I', reverse the current sequence and 
        # add it to the result
        result += current_sequence[::-1]
        # Reset the current sequence
        current_sequence = ''
    # Increment the next number
    next_number += 1

# Append the last number to the sequence and reverse the sequence
current_sequence += str(next_number)
result += current_sequence[::-1]

print(result)