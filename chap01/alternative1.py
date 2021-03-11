# 실습 1-12
print('+와-를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2:
        print('-', end='') # 홀수인 경우 - 출력
    else:
        print('+', end='') # 짝수인 경우 + 출력

print()

# 프로그램의 문제점 2가지 
# - loop를 돌때 마다 if 문이 수행됨. \
# 즉, n이 50,000이라면 if문도 50,000번 수행됨
# - 상황에 따라 유연하게 수정(X)
# 카운터용 변수 i를 0에서 n-1까지 1씩 증가시킴. 만약 i를 1부터 n까지 1씩 증가시키고 싶다면 다음과 같이
# range()함수로 전달하는 값과 for문의 print() 함수 호출 순서를 바꿔야 합니다. 

# +와-를 번갈아 출력하기1 (loop수정)

print('+와-를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(1, n+1):
    if i % 2:
        print('-', end='') # 홀수
    else:
        print('+', end='') # 짝수

print()