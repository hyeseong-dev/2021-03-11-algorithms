# print multiplication table

print('-' * 27)
for i in range(1, 10):
    for j in range(1,10):
        print(f'{i * j:5}', end="")
    print()
print('-' * 27)

# i의 값을 1부터 9까지 증가 시킵니다. 각 행은 1행, 2행, 9행에 해당 
# 즉, 바깥의 for문은 어찌보면 행과 열을 따진다면 열에 해당함

# j는 이와 반대되는 행에 해당하는 영역임.
# : 콜론 뒤에 붙은 숫자는 공백을 의미함