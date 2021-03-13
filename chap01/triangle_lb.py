#  90 degree trangle is on the left bottom with printing *

print('print 90 degree traiangle on the left bottom side')
n = int(input('input a length of short-side: '))

for i in range(n):
    for j in range(i + 1): # i가 증가 함에 따라 별표의 개수(i+1)이 카운터 변수 j에 대응하여 출력된다.
        print('*', end='')
    print()