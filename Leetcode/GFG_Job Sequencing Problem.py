class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, N):
        

        Jobs.sort(key=lambda x: x.profit, reverse=True)

        maxi = max(job.deadline for job in Jobs)
        # res = [-1] * (maxi + 1)
        res = [-1] * (N + 1)

        profit = 0
        c = 0

        for job in Jobs:
            for j in range(job.deadline, 0, -1):
                if res[j] == -1:
                    res[j] = 1
                    c += 1
                    profit += job.profit
                    break

        return [c, profit]