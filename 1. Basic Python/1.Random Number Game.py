import random as rd

random_number = rd.randint(1, 100)
print(random_number)
count = 0

while True:
    try:
        my_number = int(input())

        if my_number < random_number:
            print("업\n")
        elif my_number > random_number:
            print("다운\n")
        else:
            print(f"{count}회만에 정답을 맞췄습니다")
            break
        count = count + 1
    except:
        print("에러, 숫자를 입력하세요.")
