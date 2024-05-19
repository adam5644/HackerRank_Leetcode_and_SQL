# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:

#         # def compute(left, right, operation):
#         #     results = []

#         #     for l in left:
#         #         for r in right:
#         #             results.append(eval(str(l) + operation + str(r)))
#         #     return results

#         # if expression.isdigit():
#         #     return [int(expression)]

#         # results = []
#         # op = ["*", "-", "+"]

#         # for index, value in enumerate(expression):
#         #     if value in op:
#         #         left = self.diffWaysToCompute(expression[:index])
#         #         right = self.diffWaysToCompute(expression[index + 1:])

#         #         results += compute(left, right, value)

#         # return results
#         # -----------------------------------------------------------

#         def calc(a, b, operator):
#             if operator == "+": return a + b
#             if operator == "-": return a - b
#             if operator == "*": return a * b

#         @cache
#         def solve(expr):
#             if expr.isdigit():
#                 return [int(expr)]

#             res = []
#             for i in range(len(expr)):
#                 if expr[i] not in "+-*":
#                     continue
#                 left = solve(expr[:i])
#                 right = solve(expr[i+1:])
#                 for a in left:
#                     for b in right:
#                         res += [calc(a, b, expr[i])]

#             return res

#         return solve(expression)


class Solution:
    @functools.lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        if "+" not in expression and "-" not in expression and "*" not in expression:
            return [int(expression)]

        for i, c in enumerate(expression):
            if c in "+-*":
                for a in self.diffWaysToCompute(expression[:i]):
                    for b in self.diffWaysToCompute(expression[i + 1 :]):
                        #ans.append(eval(str([a,c,b])))
                        #ans.append(eval(str(a),c,str(b)))
                        ans.append(eval(str(a) + c + str(b)))

        # print('ans = ', ans)
        #return ans or [int(expression)]
        if ans: 
            return ans
