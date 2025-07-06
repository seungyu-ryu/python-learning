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

# 온도 변환 예제 
print("\n1. 온도 변환 (섭씨 → 화씨)")
celsius_temps = [0, 25, 50, 75, 100]

for temp_c in celsius_temps:
  temp_f = (temp_c * 9/5) + 32
  print(f"섭씨 {temp_c}°C = 화씨 {temp_f}°F")

# 압력 감소 시물레이션
print ("\n2. 압력 감소 시물레이션")
pressure = 10.0  # 초기 압력(atm)
time = 0         # 시간 (분)

print("시간(분)\t압력(atm)")
while pressure > 1.0:                      # 압력이 1atm 이상일 때
  print(f"{time}\t\t{pressure:.2f}")
  if pressure <= 0.99:
    print(위험! 압력이 1atm 이하 입니다.)
  pressure = pressure * 0.9                # 매분 10% 감소
  time += 1

print(f"{time}\t\t{pressure:.2f} (종료)")

# 농도 메트릭스 
print("\n3. 농도 메트릭스 (mol/L)")
concentrations = []                 # 농도 데이터를 저장할 리스트 생성

for i in range(3):                  # 용액 3개   
  row = []                          # 각각의 용액마다 새로운 리스트(행) 생성 
  for j in range(4):                # 성분 4개 
    conc = (i+1) * 0.1 * (j+1)      # 용액(0,1,2 +1), 성분(0,1,2,3 +1)/ 현실적인 몰농도를 위해 0.1곱하기
    row.append(conc)                # 해당 성분의 농도 추가(빈 리스트에 4개 성분 농도 추가 됨)
  concentrations.append(row)        # 한 용액의 모든 성분 농도 리스트를 큰 리스트에 추가(최종적으로 2차원의 리스트 완성)
                                    
print("용액\\성분\tA\tB\tC\tD")
for i, row in enumerate(concentrations):
  print(f"용액{i+1}\t\t", end="")
  for conc in row:
    print(f"{conc:.1f}\t", end="")
  print()

# row = [] 한 행 만들 준비
# row.append() 성분 농도 하나씩 추가
# concentrations.append(row) 전체 메트릭스에 추가
 






















