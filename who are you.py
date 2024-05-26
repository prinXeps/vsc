print("당신이 태어난 년도를 입력하세요:")

cel_value = int(input())
fel_value = (2024 - cel_value + 1)

if fel_value >= 27: age = '어른입니다'
elif fel_value >= 20: age = '대학생입니다'
elif fel_value >= 17: age = '고등학생입니다'
elif fel_value >= 14: age = '중학생입니다'
elif fel_value >= 8: age = '초등학생입니다'
else: age = '학생이 아닙니다'

print("당신은",str(fel_value) + "살 입니다")
print(age)