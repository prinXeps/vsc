print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다")
print("변환하고 싶은 섭씨 온도를 입력해 주세요:")
cel_value = float(input()) #input받은 값을 메모리에 저장한다... 따라서 cel이름 붙여 만듬. 스트링이므로 플롯으로 바꾸기
fah_value = ((9/5) * cel_value) + 32 #input값을 계산하면 다른 메모리에 저장한다.

print(f"섭씨온도 : {cel_value:.2f}")
print(f"화씨온도 : {fah_value:.2f}")