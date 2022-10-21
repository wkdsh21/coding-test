'''
단순히 정답과 비교하여 점수계산하는 문제
사람마다의 찍는 규칙에따라 계속 순환되게하는게 포인트
'''
def solution(answers):
    one=[1, 2, 3, 4, 5]
    two=[2, 1, 2, 3, 2, 4, 2, 5]
    three=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score=[[0,1],[0,2],[0,3]] #점수기록
    for i,value in enumerate(answers): #규칙 순환을위한 enumerate
        if(one[i%5]==value): #5개씩 반복되기 때문에 5로나눈나머지값을 인덱스로 사용
            score[0][0]+=1 #맞추면 점수증가
        if(two[i%8]==value):
            score[1][0]+=1
        if(three[i%10]==value):
            score[2][0]+=1
    score.sort() #정렬하여 제일큰값을 가진 사람 찾기 max()를 사용하면 더 간단해짐
    result=[score[2][1]]
    if(score[2][0]==score[1][0]): #만약 점수가 같다면 같이 넣어주기 
        result.insert(0,score[1][1])
    if(score[2][0]==score[0][0]):
        result.insert(0,score[0][1])
    '''
    maxv=max(score)
    for i,value in enumerate(score):
        if value==maxv:
            result.append(i+1)
    '''
    answer = result
    return answer
