import sys
from math import gcd # g
from collections import defaultdict
from fractions import Fraction

sys.setrecursionlimit(10**9)

def dfs1():
    '''keep 1 node as root and calculate how many arrows are pointing towards it'''
    root = 1
    seen = {root, }
    stack = [root]
    count = 0
    while stack:
        #print('stack = ', stack)
        root = stack.pop()
        for node in tree[root]:
            if node not in seen:
                seen.add(node)
                
                #count += (root, node) in guess    # if root is parent of node
                if (root, node) in guess:
                    #print('node = ', node)
                    #print('count+=1')
                    count += 1
                    
                stack.append(node)
    #print('dfs1 count = ', count)
    return count

def dfs2(cost, k):
    '''now make every node as root and calculate how many nodes
       are pointed towards it; If u is the root node for which
       dfs1 calculated n (number of arrows pointed towards the root)
       then for v (adjacent node of u), it would be n-1 as v is the
       made the parent now in this step (only if there is a guess, if
       there is no guess then it would be not changed)'''
    root = 1
    seen = {root,}
    stack = [(root, cost)]
    t_win = 0
    while stack:
        (root, cost) = stack.pop() 
        t_win += (cost >= k)
        for node in tree[root]:
            if node not in seen:
                seen.add(node)
                
                #stack.append((node, cost - ((root, node) in guess) + ((node, root) in guess)))
                # Check if the current direction from root to node is in the guesses
                is_current_direction_guessed = (root, node) in guess

                # Check if the reverse direction from node to root is in the guesses
                is_reverse_direction_guessed = (node, root) in guess

                # Calculate the new cost based on the presence of guesses
                new_cost = cost
                if is_current_direction_guessed:
                    new_cost -= 1
                if is_reverse_direction_guessed:
                    new_cost += 1

                # Append the node with the updated cost to the stack
                stack.append((node, new_cost))
                
    return t_win


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    tree = defaultdict(list)

    for a1 in range(n-1):
        u,v = map(int, input().strip().split(' '))
        tree[u].append(v)
        tree[v].append(u)

    g,k = map(int, input().strip().split(' '))
    guess = {tuple(map(int, input().split())) for _ in range(g)}
    
    # # inputs: n,k,tree, guess
    # print()
    # print(n,k)
    # print(tree)
    # print(guess)
    # 4 2
    # defaultdict(<class 'list'>, {1: [2, 3], 2: [1], 3: [1, 4], 4: [3]})
    # {(1, 2), (3, 4)}

    cost = dfs1() # perform dfs node 1, and return number of correct guess for one node
    win = dfs2(cost, k) # dfs for diff node, return number of correct guess for all nodes
    print(Fraction(win,n))
    print('------------------------')