class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol =[] 
        target=n
        def recur( value, totalbrac, netbrac):

            if totalbrac == target:
                st=[]
                for _ in range(netbrac):
                    st.append(")")
                print(netbrac)
                sol.append("".join(value)+"".join(st))
                return
            

            if netbrac == 0:
                value.append("(")
                totalbrac +=1
                netbrac +=1
                recur(value, totalbrac, netbrac)
                value.pop()
                totalbrac -=1
                netbrac -=1
            
            elif netbrac >0 :
                value.append("(")
                totalbrac +=1
                netbrac +=1
                recur(value, totalbrac, netbrac)
                value.pop()
                totalbrac -=1
                netbrac -=1

                value.append(")")
                netbrac -=1
                recur(value, totalbrac, netbrac)
                netbrac +=1
                value.pop()
        recur([],0,0)
        return sol


                     
            