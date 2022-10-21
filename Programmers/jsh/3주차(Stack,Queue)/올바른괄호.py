def solution(s):
    '''
    sum=0
    answer=True
    for i in s:
        if i=='(':
            sum+=1
        else:
            sum-=1
        if sum<0:
            answer=False
            break
    if sum>0:
        answer=False
    '''
    answer = True
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack!=[]:
                stack.pop()
            else:
                answer=False
                break
    if stack!=[]:
        answer=False
    return answer