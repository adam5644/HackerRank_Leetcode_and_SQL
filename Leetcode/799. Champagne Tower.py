class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0: return 0
        if query_row == 0: 
            if poured >= 1:
                return 1.0
            else:
                return 0
                

        prev_row = [poured]
        for i in range(1, query_row+1):
            curr_row =[0]*(i+1)
            for j, value in enumerate(prev_row):
                value-=1
                if value >0:
                    curr_row[j] += value*0.5
                    curr_row[j+1] += value*0.5
            prev_row = curr_row

            # print('i = ', i)
            # print('curr_row = ', curr_row)

        if curr_row[query_glass] >= 1:
            return 1.0
        else:
            return curr_row[query_glass]

