class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image

        starting = image[sr][sc]

        def dp(sr,sc):
            if sr<0 or sc<0 or sc > (len(image[0])-1) or sr > len(image)-1:
                return
            print(sr,sc)
            if image[sr][sc] == starting:
                image[sr][sc] = color

                dp(sr+1,sc)
                dp(sr-1,sc)
                dp(sr,sc+1)
                dp(sr,sc-1)

        dp(sr,sc)
        return image