'''
가능한 모든경우의수를 순열함수를 사용하여 만들어내고
소수 알고리즘을 이용하여 소수를찾음(중복 제거 포함)
'''
def permutation(arr, r,usednum): #순열 알고리즘 arr(배열),r(순열의 길이),usednum(만들어진 순열의 중복을피하기위해)
    arr = sorted(arr) #굳이 정렬안해도됨
    used = [0 for _ in range(len(arr))] #숫자가 사용되었는지 알려주는 배열
    def generate(chosen, used,usednum): #순열 만들기 알고리즘
        answer=0
        if len(chosen) == r: #종료조건:자신이원하는 길이(r)에 도달했을때
            chosen="".join(map(str,chosen)) #문자열로 합쳐줌
            chosen=int(chosen) #정수로 바꾸어줌
            if(chosen in usednum or chosen==1 or chosen==0): #중복된 숫자인지 검사 또는 1이나 0은 소수가아니므로 검사
                return 0
            usednum.append(chosen) #검사 통과시 usednum에 추가
            for i in range(2,int(chosen/2)+1): #소수가맞는지 검사
                if(chosen%i)==0: #1이 아닌 어떤수로 나눠질경우 소수가아님
                    return 0 #탈출
            return 1 #소수가맞으므로 개수 1개추가
	
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i]) #현재 선택된 숫자를 집어넣고
                used[i] = 1 #사용되었다고 1 표시
                #재귀함수 실행 ex)12345 일경우 1이 첫번째에들어간 1 _ _ _ _ 의 숫자중에 소수인개수를 answer에 더해줌
                answer+=generate(chosen, used,usednum) 
                used[i] = 0 #다시 초기화
                chosen.pop() #다시 초기화 후 다음숫자 넣고 재귀함수실행 ex)2 _ _ _ _ 
        return answer #소수의개수 반환
    return generate([], used,usednum)


def solution(numbers):
    answers=0
    numberes=list(numbers)
    usednum=[]
    for i in range(1,len(numbers)+1): #순열의 길이 1~리스트의 길이만큼 반복하여 뽑아냄
        answers+=permutation(numbers, i,usednum)
                
    return answers