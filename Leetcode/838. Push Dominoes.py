class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        # Apply forces going from left to right
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # maximum force
            elif dominoes[i] == 'L':
                force = 0  # no force after an 'L'
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        # Apply forces going from right to left
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n  # maximum force
            elif dominoes[i] == 'R':
                force = 0  # no force after an 'R'
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        
        # Determine the final state
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)