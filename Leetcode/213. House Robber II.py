
class Solution:
    def rob(self, nums) -> int:
        # If there's only one house, return its value because that's the maximum we can rob without alerting the police.
        if len(nums) == 1:
            return nums[0]

        # Define a helper function to compute the maximum amount that can be robbed from a linear array of houses.
        def compute_max_robbery(houses):
            # Initialize variables to store the maximum robbery amounts up to two houses back.
            max_rob_two_back = 0  # Maximum amount robbed two houses back.
            max_rob_one_back = 0  # Maximum amount robbed from the previous house.

            # Iterate through the list of house values.
            for current_house_value in houses:
                # Calculate the maximum money that can be robbed including the current house.
                current_max = max(max_rob_two_back + current_house_value, max_rob_one_back)

                # Update the values for the next iteration.
                max_rob_two_back = max_rob_one_back
                max_rob_one_back = current_max

            # Return the maximum amount robbed up to the last house.
            return max_rob_one_back

        return max(compute_max_robbery(nums[1:]), compute_max_robbery(nums[:-1]))

# Example usage
print(Solution().rob([2,3,2]))  # Output: 10