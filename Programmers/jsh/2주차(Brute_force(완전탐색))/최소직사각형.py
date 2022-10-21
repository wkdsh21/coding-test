'''
1.가로길이중 제일큰값과 세로길이중 제일큰값을 비교해서 큰값을 구하여
지갑의 한쪽면길이로 잡고 나머지 길이를 구한다(세로 가로 상관없이 제일 긴 값을 찾음)
2.나머지 길이는 모든 명함의 가로세로를 비교하여 작은길이들을 구한다음 그 길이들 중에
제일 큰값을 지갑의 나머지 면의길이로 정하면 최소넓이이다. 
'''

def solution(sizes):
    sizes.sort() #가로 기준으로 정렬
    max1=sizes[len(sizes)-1][0]
    sizes.sort(key=lambda x:x[1]) #세로 기준으로 정렬
    max2=sizes[len(sizes)-1][1]
    maxvalue=max1 if max1>=max2 else max2 #제일 긴 길이 대입
    minvalue=0
    for i in sizes: #2번과정을위해 모든 명함의 가로세로길이를 비교
        if i[0]>=i[1]:
            if minvalue<i[1]: #현재 명함의 가로세로길이중 짧은 값이 minvalue값보다 클경우 대입
                minvalue=i[1]
        else:
            if minvalue<i[0]:
                minvalue=i[0]
    
    answer = maxvalue*minvalue #면적 구하기
    return answer
