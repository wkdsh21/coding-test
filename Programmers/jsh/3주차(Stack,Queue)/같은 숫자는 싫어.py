def solution(arr):
    answer=[arr[0]] #처음 숫자를 넣고
    for i in arr: #i 에는 arr리스트의 숫자가 순서대로 들어감
        if answer[-1]!=i: #제일마지막에 들어간숫자와 다를때만
            answer.append(i) #정답 리스트에 추가함
    return answer
