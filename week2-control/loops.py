# 반복문 연습

# for 반복문
print("===for 반복문 연습===")
for i in range(1, 6):
  print(f"{i}번째 반복입니다.")

# 화학공학 관련 예제 - 반응기 온도 체크
print("\n===반응기 온도 모니터링===")
temperatures = [150, 200, 180, 220, 195]
for temp in temperatures:
  if temp > 200:
    print(f"온도{temp}°C: 경고! 온도가 너무 높습니다.")
  else: 
    print(f"온도{temp}°C: 온도가 정상입니다.")

# while 반복문 
print("\n===while 반복문 연습===")
pressure = 0                                #pressure 라는 변수에 처음 압력 값을 0으로 설정
while pressure < 10:                        #조건이 참일 동안 반복
  pressure += 2                             #변수 값을 증가시킴(반복 탈출을 위한 변화)
  print(f"현재 압력 : {pressure} bar")       #반복마다 결과 출력
