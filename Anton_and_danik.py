n=int(input())
S=input()
anton_w=S.count('A')
danik_w=S.count('D')
if anton_w > danik_w:
    print("Anton")
elif anton_w < danik_w:
    print("Danik")
else:
    print("Friendship")
