from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        ans = []
        graph = defaultdict(list)
        deq = deque(supplies)

        # Create a graph mapping ingredients to recipes
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])

        # Initialize a count of ingredients required for each recipe
        count = {recipes[i]: len(ingredients[i]) for i in range(len(recipes))}

        # deq
        # graph
        # count
        # Process the supplies using BFS
        while deq:
            cur = deq.popleft() # cur = each supplies
            for recipe in graph[cur]:
                count[recipe] -= 1 # all recipes that need "curr" now -=1
                if count[recipe] == 0:
                    ans.append(recipe)
                    deq.append(recipe) # this can-be-made recipe is added to deque as it is considered a "supply" too

        return ans