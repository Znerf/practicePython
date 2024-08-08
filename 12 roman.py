class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary={
            1:"I",
            5:"V",
            10 : "X",
            50 : "L",
            100:"C",
            500:"D",
            1000:"M"
        }

        m=1000
        string=""
        while num >0:
            index= num //m
            if index <=3 :
                text= dictionary[m]*index
            elif index == 4 or index == 9:
                text = dictionary[m]+dictionary[(index+1)*m]  
            elif index == 5 :
                text = dictionary[m*index]
            else:
                
                text = dictionary[5*m] + dictionary[m]*(index-5)
            string +=  text
            num = num %m
            m=m//10
        return string