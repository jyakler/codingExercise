sq,cal=map(int,input().split())
cube=[]
for _ in range(sq):
    cube.append(list(map(int,input().split())))
S=[]    
#구간합 구하기
for i in range(sq):
    temp=0
    templ=[]
    for j in range(sq):
        temp+=cube[i][j]
        templ.append(temp)
    S.append(templ)

for _ in range(cal):
    result=0
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1-1,x2):
        result+=(S[i][y2-1]-S[i][y1-1])
    print(result)