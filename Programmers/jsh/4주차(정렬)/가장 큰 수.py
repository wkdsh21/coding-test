import functools
def comparator(a,b):
    if a+b<b+a: #ex) '6','10' '610'과 '106'을 비교하여 순서를 바꿀지 정함 
        return -1 #-1 반환시 순서 바꿈
    else:
        return 0 #그대로 둠 (처음에 else를 설정안했다가 오류가뜸 무조건 반환값이있어야함)

def solution(numbers):
    n = [str(x) for x in numbers] #정렬을하기위해 정수를 문자로 변경
    #cmp_to_key를 사용, 직접만든 함수 사용하여 정렬
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    #문자리스트를 문자열로 합치고 앞에 붙는 '0'들을 제거하기위해 정수 변환후 다시 문자열로 변환
    return str(int(''.join(n)))
