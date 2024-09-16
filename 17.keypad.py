class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        dic={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        sol=[]
        def backtrack(path,start):
            value=''.join(start)
            if len(start) == len(digits):
                sol.append(value)
                return
            
            for num in dic[path[0]]:
                start.append(num)
                backtrack(path[1:],start)
                start.pop()

                

        backtrack(digits,[])
        return sol