print("본 프로그램은 2024년 05월 26일 달러를 원화, 엔화 계산해주는 프로그램입니다.")
print("교환할 달러 값을 입력해주세요:")

cel_value = float(input())
fel_value = (cel_value * 1368)
eel_value = (cel_value * 156.95)

print(f"미국 화폐 : {cel_value:.2f}달러")
print(f"한국 화폐 : {fel_value:.2f}원")
print(f"일본 화폐 : {eel_value:.2f}엔")
