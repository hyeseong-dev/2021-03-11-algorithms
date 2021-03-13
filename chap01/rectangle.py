# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area+1): # 1부터 사각형의 넓이를 계산
    if i * i > area: break  # 참이면 loop를 종료함. i가 가장 긴변의 길이가 되기 때문
    if area % i : continue # i 가 area의 약수가 아닐 경우 실행, 나머지가 있는 경우
    print(f'{i}*{area//i}')