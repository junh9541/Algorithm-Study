def solution(brown, yellow):
    answer = []
    heightPlusHight=(brown-4)//2
    for height in range(1, heightPlusHight//2+1):
        width = heightPlusHight-height
        if height*width==yellow:
            return [width+2, height+2]
                        