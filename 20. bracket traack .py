class Solution:
    def isValid(self, st: str) -> bool:
        d=[]

        dicttion={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for each in st:
            # print (each)
            if each in ["(","[","{"]:
                d.append(each)
            if each in [")","]","}"]:
                if len(d) <1:
                    return False
                if d[-1] == dicttion[each]:
                    d.pop()
                else:
                    return False
            # print("sd",d)
        if len(d) != 0:
            return False
        return True

        