def solution(citations):
    answer = 0
    num=0
    li=[]
    originlen=len(citations)
    #원소의개수보다 인용횟수가 큰값은 절대 H-index가 될 수 없기때문에 pop해주고 그 개수만큼 num증가(li의 원소개수를 줄이기위해)
    for i in range(originlen):
        if citations[-1]<=originlen:
            li.append(citations.pop())
        else:
            citations.pop()
            num+=1
    #처음엔 뽑아낸리스트중에서 제일 큰 값부터 줄여나갔지만 오류가뜸 원래의 원소의개수부터 H-index가 될수있었음
    for i in range(originlen,-1,-1):
        count=0
        for j in li: #뽑아낸 리스트중에 같거나 큰값 개수 증가
            if i<=j:
                count+=1
        if count+num>=i: #i번이상 인용된논문의 개수가 i개이상일때(num을 더해주는이유는 제외된 원소들은 무조건 i번이상 인용됐으므로)
            answer=i
            break
    return answer
