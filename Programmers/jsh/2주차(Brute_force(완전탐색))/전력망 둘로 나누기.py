def solution(n, wires):
    answer = -1
    max=n
    for j in range(len(wires)):
        #초기화 단계 matrix=인접행렬 check=방문했는지 확인
        matrix=[[] for _ in range(n+1)]
        check=[0 for _ in range(n+1)]
        check[0]=-1 #index가 1부터시작하기위해
        wire=wires[:j]+wires[j+1:] #j원소를 제외한 리스트 복사
        for i in wire: #인접행렬 생성
            matrix[i[0]].append(i[1])
            matrix[i[1]].append(i[0])
        num=0
        #방문을 다 했는지 확인 DFS로작성
        while check.count(0)!=0:
            stack=[]
            stack.append(check.index(0))#방문하지않은 곳이있다면 스택에 넣어줌
            '''
            분리된 그래프를 식별하기위해 1증가 ex)check=[-1,1,2,1,1,1,2,2,2] 
            2개의 분리된 그래프가존재함
            '''
            num+=1
            check[check.index(0)]=num #그래프 식별을 위해 num을대입
            while stack: #스택이 빌때까지
                x=stack.pop()
                for i in matrix[x]: #행렬안의 방문하지않은 원소 스택에 추가
                    if check[i]!=num:
                        stack.append(i)
                        check[i]=num #추가할때 방문체크를해야 중복 추가 막을수있음
        if num==2: #그래프가 두개로 분리 되었을때만
            if max>abs(check.count(1)-check.count(2)): #송전탑의 개수의 차 비교
                max=abs(check.count(1)-check.count(2))
    return max
