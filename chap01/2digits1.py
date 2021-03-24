# excercise 1C-3

# input 2 digit positive number

print('input 2digit positive number.: ')

while 1:
    no = int(input('input number.: '))
    # if no >=10 and no <=99:
        break
print(f'The positive Number you input is {no}')

# no >=10 and no <=99: 과 동일한 방법으로는  10 <= no <=99:

# 드모르간의 법칙을 이용하면 좋음 
# if not(no <10 or no > 99) <--> if not (10 <= no <=99):