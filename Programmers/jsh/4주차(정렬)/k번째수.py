def solution(array, commands):   
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]
'''
sorted(array[i:j])[k]
array 리스트를 슬라이싱
ex)2번째부터 5번째 -> array[1:5]->array[1]~array[4]부분을 잘라 새로 리스트를만듬
슬라이싱된 리스트들을 정렬후 commands의 마지막원소 k를 인덱스에 넣음
for문을 활용하여 반복 리스트에 대입후 리턴
'''
