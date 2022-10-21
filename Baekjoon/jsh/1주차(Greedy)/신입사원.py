'''
서류성적을 정렬하고 1등부터 끝까지 탐색을 하며 1등의 면접등수보다 높은 지원자는 무조건 합격이므로
합격시키고 (바로전 합격된사람의 면접등수가 제일 높으므로) 그다음 지원자들과 비교 
계속반복하면 최적의 해가 무조건 나오므로 그리디알고리즘 만족  
'''
import sys #input() 함수사용시 시간초과

testcasenum=int(sys.stdin.readline()) #입력을받아 정수형으로 변환
for i in range(testcasenum): #testcase의 숫자만큼 반복
    result=1 #1등은 무조건 합격이므로 1부터시작
    applicantnum=int(sys.stdin.readline()) #지원자의 숫자 입력받음
    applicantlist=[] #지원자의 점수 리스트
    for j in range(applicantnum): #지원자의 숫자만큼 반복 하여 점수입력
        applicantlist.append(list(map(int,sys.stdin.readline().split(" ")))) 
    applicantlist.sort() #지원자의 점수를 정렬
    min=applicantlist[0][1] #최솟값으로 1등의 면접성적 대입
    for j in range(applicantnum): #지원자의 숫자만큼 반복
        #이미 지원자의 서류성적은 정렬되어있으므로 면접성적만 비교하여 순위가 높다면 합격시키고 min변수에 대입
        if(min>applicantlist[j][1]):
            result+=1
            min=applicantlist[j][1]
    print(result)