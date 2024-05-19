class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()  # To keep track of the ugly numbers we have encountered
        q = [1]  # Start with the first ugly number
        i = 1  # Counter to keep track of how many ugly numbers we've generated

        while i < n:
            curr = q.pop(0)  # Pop the smallest number from the queue
            # Generate new ugly numbers by multiplying current number by 2, 3, and 5
            new = {curr * 2, curr * 3, curr * 5} - seen
            seen.update(new)  # Add the new numbers to the seen set
            q.extend(new)  # Add the new numbers to the queue
            q.sort()  # Sort the queue to maintain order
            i += 1  # Increment the counter

        # q[0] will be the nth ugly number after the loop ends
        return q[0]