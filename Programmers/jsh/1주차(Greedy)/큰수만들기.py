'''
앞에서부터 k+1만큼을 탐색하여 제일 큰 수N을 찾고 N의앞부분을 지우고 지운개수만큼 k값 감소
다시 N은 확정이므로 그다음 인덱스부터 탐색을 반복하면 최적의 해가 나온다는것을 보장할 수 있음
'''
def solution(number, k):
    number=list(map(int,number)) #"123"문자열을 [1,2,3] 숫자 리스트로 변경
    num=0 #확정된 숫자는 다시 탐색하지 않기위한 변수 반복할때마다 1씩증가함
    resultlen=len(number)-k #k만큼 숫자를 빼고난뒤 총 길이
    #더이상 뺄 숫자가 없거나 확정된 숫자의 개수가 resultlen 과 같을때
    while(k!=0 and num!=resultlen):
        max=[0,-1] #최대숫자 찾기위한 리스트 [인덱스,값]
        #num부터 탐색을 시작 k+1개의 숫자까지 탐색 만약 최대범위를 넘어서는것을 방지하기위해 if문사용
        for i in range(num,num+k+1 if num+k+1<len(number) else len(number)):
            if(max[1]<number[i]): #제일 큰 숫자 찾기
                max[1]=number[i]
                max[0]=i
                if(number[i]==9): #숫자가 9이면 제일 크기때문에 반복문 탈출
                    break
        del number[num:max[0]] #제일 큰 숫자의 앞부분 삭제
        k-=max[0]-num #삭제된 개수만큼 k 감소
        num+=1 #확정된 숫자의 개수 1증가
    if(k!=0): #k의 횟수가 남아있을 경우 그만큼 뒤에서부터 삭제
        del number[num:]
    number="".join(map(str,number)) #[1,2,3] 리스트를 다시 "123"문자열로 합침
    answer = number
    return answer