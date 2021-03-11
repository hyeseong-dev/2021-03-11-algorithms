# +와-를 번갈아 출력 2
print('+와-를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n//2): #  range() 안의 인자를 통해서 
    print('+-', end='') # +-를 ㅜ//2개의 출력

if n % 2:
    print('+', end='')

print()
