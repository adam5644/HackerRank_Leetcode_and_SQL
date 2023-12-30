def largestRectangle(h):
    stack = []
    max_area = 0
    index = 0
    h.append(0)  # Append 0 to handle the end of the list

    while index < len(h):
        if not stack or h[index] >= h[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = h[top] * (index if not stack else (index - stack[-1] - 1))
            max_area = max(max_area, area)

    return max_area