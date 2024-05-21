# def solution(phone_book):
#     for i in phone_book:
#         check=2
#         for j in phone_book:
#             if j[0:len(i)]==i:
#                 check-=1
#         if check==0: return False
#     return True
def solution(phone_book):
    phoneDic = {phone: 0 for phone in phone_book}
    for phone in phone_book:
        num=""
        for c in phone:
            num+=c
            if phoneDic.get(num)==0 and phone !=num:
                print(num)
                return False
    return True
        
                
#     answer = True
#     for p in phone_book:
#         ch=0
#         for c in phone_book:
#     if ch>1:
#         answer=False
#     return answer