def solution(sizes):
    width=0
    height=0
    for a, b in sizes:
        if b>a:
            a, b = b, a
        width = max(a, width)
        height = max(b, height)
        
    return width*height