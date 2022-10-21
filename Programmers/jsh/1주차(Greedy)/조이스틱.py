#그리디로 풀려다 몇몇 최적의 해가 나오지 않는 케이스때문에 dfs로변경
'''
#1.먼저 오른쪽으로 움직여 제일먼저 나오는 a가아닌문자까지 도달하기위한 횟수와
#2.왼쪽으로 움직여 제일먼저나오는 a가아닌문자까지 도달하기위한 횟수를 비교
#3.작은횟수를가진 자리로 이동 하여 그 자리의 문자를 'A'로변경
#4.현재자리에서 123단계반복
#5.모두 A로 변경되었을때 종료

def solution(name):
    count=0
    x=0 #현재위치 인덱스
    notacount=0
    post=[0,0] #[인덱스,움직인 횟수]
    back=[0,0]
    name=list(name)
    #a가 아닌 갯수 count(변경되어야할 갯수)
    for i in range(1,len(name)):
        if(ord(name[i])!=65):
            notacount+=1
    #▲ ▼의 count숫자 미리계산
    for i in name:
        if(ord(i)<=78):
            count+=ord(i)-65
        else:
            count+=91-ord(i)
    name[0]='A' #처음시작부분 A로변환
    for i in range(notacount): #notacount만큼 반복(a가아닌 다른 문자로 변경되어야하는 자리의 개수)
        postcount=0
        for i in range(len(name)-1): #오른쪽으로 이동할때
            if(i+x+1<len(name)): #현재위치가 최대범위를 넘지않을때
                #i+x+1인이유 -> 현재위치부터 탐색을 하기위해
                if(ord(name[i+x+1])!=65): #'A'가 아닌 문자가나올때
                    post[0]=i+x+1
                    postcount+=1
                    post[1]=postcount
                    break
                else:
                    postcount+=1 #움직인 횟수 증가
            else: #현재위치가 최대범위를 넘을때
                if(ord(name[i+x+1-len(name)])!=65):
                    post[0]=i+x+1-len(name)
                    postcount+=1
                    post[1]=postcount
                    break
                else:
                    postcount+=1
        backcount=0
        for i in range(len(name)-1): #왼쪽으로 이동할때
            if(x-i-1>-1):
                if(ord(name[x-i-1])!=65):
                    back[0]=x-i-1
                    backcount+=1
                    back[1]=backcount
                    break
                else:
                    backcount+=1
            else:
                if(ord(name[x-i-1+len(name)])!=65):
                    back[0]=x-i-1+len(name)
                    backcount+=1
                    back[1]=backcount
                    break
                else:
                    backcount+=1
        #오른쪽으로 이동한 결과와 왼쪽으로 이동한 결과중 최소값 대입
        if(post[1]>=back[1]):
            x=back[0] #현재위치 변경
            count+=back[1] #최종적으로 count 변경
            name[x]='A' #현재자리 A로변경(이미 문자를 바꾸는횟수는 위에서 계산함)
        else:
            x=post[0]
            count+=post[1]
            name[x]='A'
    answer = count
    return answer
'''

'''
dfs로 모든경우의수를 계산하여 최소값 반환
'''
import copy #깊은복사를 위해
def dfs(name,i,count): #재귀함수 형태로 코딩 
    count+=1 #움직일때마다 count 1증가
    name[i]='A' #현재위치를 'A'로변경
    '''
    재귀함수의 종료조건 모두'A'로 변경됐거나 
    (count-1인 이유는 처음 dfs를호출할때 1이 증가하기때문) 
    최대 횟수를 넘어설때 종료
    '''
    if(len(name)==name.count('A') or count-1==len(name)-1):
        return count
    name1=copy.deepcopy(name) #깊은복사(서로 영향이 없어야 하므로)
    name2=copy.deepcopy(name)
    #최솟값 반환
    return min(dfs(name1,i+1 if i!=len(name)-1 else 0,count),dfs(name2,i-1 if i!=0 else len(name)-1,count))
    
    
def solution(name):
    count=0
    name=list(name) #문자열을 리스트로 변환 "asdf" -> ['a','s','d','f']
    #▲ ▼의 횟수를 미리계산
    for i in name:
        if(ord(i)<=78):
            count+=ord(i)-65
        else:
            count+=91-ord(i)
    answer = dfs(name,0,0)+count-1 #총 count횟수계산(count-1인 이유는 처음 dfs를호출할때 1이 증가하기때문)
    return answer