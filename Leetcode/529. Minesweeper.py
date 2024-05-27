 # 

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
       # print()
        ##print('initial')
       # for x in board: print(x)
        
        def dfs(i,j): # assign number to black box
            #print('i,j = ', i,j)

            nonlocal vis
            if (i,j) in vis: return
            vis.add((i,j))

            # base
            if not 0<=i<=m-1 or not 0<=j<=n-1: return

            if board[i][j]=='E':
                adj_mines = 0
                
                for ii,jj in directions:
                    if 0<=i+ii<=m-1 and 0<=j+jj<=n-1:
                        if (board[i+ii][j+jj]=='M' 
                                            or board[i+ii][j+jj]=='X'):
                            adj_mines+=1
                            
                
                if not adj_mines:
                    board[i][j] = 'B'
                    for di, dj in directions:
                        dfs(i + di, j + dj)
                else: # >0
                    board[i][j] = str(adj_mines)
            
        m,n = len(board), len(board[0])
        vis=set() # positions that were visited

        directions=[
            [-1,-1], [-1,0], [-1,1],
            [0,-1],[0,1],
            [1,-1],[1,0],[1,1]
        ]

        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]] = 'X'

        if board[click[0]][click[1]] =='E':
            dfs(click[0], click[1])
        
        #print()
        #print('final')
        for x in board: print(x)

        return board
