import math
def solution(progresses, speeds):
    day=[] #남은 날짜 리스트
    answer=[] 
    for i in range(len(progresses)):
            #ceil은 소숫점을 무조건 올려주는 함수 ex)3.2->4, 3.6->4
            day.append(math.ceil((100-progresses[i])/speeds[i]))
    max=day[0] #처음값을 비교를위해 넣어줌
    count=0 #한번 배포할때 배포되는 기능의수
    while(1): #Queue 이용
        if(max>=day[0]): #최대값보다 작거나같을경우엔
            day.pop(0) #day의 맨처음값을 뽑음
            count+=1 #뽑아낼때마다 1증가
            if day==[]: #while 종료조건 day리스트가 빌 때까지
                answer.append(count)
                break
        else: #max보다 큰 날짜를 발견했을경우
            answer.append(count) #그 전의 기능개수를 답에 추가
            max=day[0] #max값 초기화
            count=0 #count 초기화
    return answer

    '''
    ex) day=[7,3,9,4,5]
    1. answer=[] count=1 day=[3,9,4,5]
    2. answer=[] count=2 day=[9,4,5]
    3. answer=[2] count=0 day=[9,4,5] #더 큰날짜 발견 7<9
    4. answer=[2] count=1 day=[4,5]
    5. answer=[2] count=2 day=[5]
    6. answer=[2] count=3 day=[] #day리스트가 비었음
    7. answer=[2,3] count=3 day=[] #while문 종료
    '''