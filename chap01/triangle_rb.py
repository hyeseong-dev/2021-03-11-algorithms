#  90 degree trangle is on the right bottom with printing *

print('print 90 degree traiangle on the right bottom side')
n = int(input('input a length of short-side: '))

for i in range(n):
    for _ in range(n-i-1): #
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()

# 포문 3개가 돌아감. 2번째 포문이 이단 다 돌고 다음 3번째 포문에서 별을 찍기 시작함. 
# 즉, 공백을 출력하고 마무리로 별을 찍는 로직임
