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
  concentrations.append(row)        # 한 용액의 모든 성분 농도 리스트를 큰 리스트에 추가(최종적으로 2차원의 리스트 즉, 메트릭스 완성)
                                    
print("용액\\성분\tA\tB\tC\tD")
for i, row in enumerate(concentrations):      # 인덱스 i:용액번호(0..), 값 row:성분 리스트를 같이 불러옴
  print(f"용액{i+1}\t\t", end="")             # 용액1, 용액2.. , 줄바꿈 없이 바로 다음 출력
  for conc in row:
    print(f"{conc:.1f}\t", end="")            # 성분별 농도 출력
  print()                                     # 줄바꿈
# row = [] 한 행 만들 준비
# row.append() 성분 농도 하나씩 추가
# concentrations.append(row) 전체 메트릭스에 추가

# 반복문 제어 - break & continue
print("\n4. 반응 온도 최적화")
temperatures = [150, 200, 250, 300, 350, 400, 450]

print("최적 온도 범위 찾기 (250-350°C)")
for temp in temperatures:
  if temp < 250:
    continue   # 너무 낮은 온도는 건너뛰기
  if temp > 350:
    print(f"온도 {temp}°C: 너무 높음 - 반응 중단")
    break      # 너무 높은 온도에서 중단

  # 반응 속도 계산 - 가짜 선형 모델
  rate = 0.01 * (temp - 200)
  print(f"온도 {temp}°C: 반응속도 = {rate:.2f}")
  # 반응 속도 계산 - 간단한 아레니우스 방정식
  import math

  A = 1e13       # 빈도 인자
  Ea = 80000     # 활성화 에너지 (J/mol)
  R = 8.314      # 기체 상수
  T = 298        # 절대온도 (K)

  k = A * math.exp(-Ea / (R * T))
  print(f"온도 {temp}K: 반응 속도 상수 = {k:.2e}")

# list comprehension
print("\n5. 분자량 계산 (리스트 컴프리헨션)")

compounds = ["H2O", "CO2", "NH3", "CH4", "C2H6"]
molecular_weights = [18.02, 44.01, 17.03, 16.04, 30.07]

# 리스트 컴프리헨션으로 몰수 계산: 몰수 = 질량 / 분자량 (여기선 질량 1g 고정)
moles = [1.0/mw for mw in molcular_weights]

print("화합물\t분자량(g/mol)\t몰수(1g 기준)")
print("-" * 30)           # 구분선
for i in range(len(compounds)):
  print(f"{compoundsp[i]}\n{molecular_weights[i]}\t\t{moles[i]:.4f}")

 # zip 사용
 for compound, mw, mol in zip(compounds, molcular_weights, moles):
   print(print(f"{compound}\t{mw}\t\t{mol:.4f}"))
 #enumerate 사용
 for i, compound in enumerate(compounds):
   mw = molecular_weights[i]
   mol = moles[i]
   print(f"{compound}\t{mw}\t\t{mol:.4f}")
 # dictionary 사용
 data = dictionary(zip(compounds, zip(molecular_weights, moles)))
 for compound, (mw, mol) in data.items():
   print(f"{compound}\t{mw}\t\t{mol:.4f}")

# enumerate & zip 예제
print("\n6. 실험 데이터 처리")
experiment_time = [0, 30, 60, 90, 120]   # 분
conversion_rates = [0, 15, 35, 60, 78]   # %

print("실험 결과")
for time, conversion in zip(experiment_times, conversion_rates):
  print(f"시간: {time}분, 전환율: {conversion}%")

print("\n최고 전환율 찾기:")
for index, (time, conversion) in enumerate(zip(experiment_times, conversion_rates))
  if conversion == max(conversion_rates):   # 목적에 맞는 최고 전환율만 출력하기 위함
    print(f"최고 전환율 : {conversion}% (실험 {index+1}번째, {time}분)")

print("\n===반복문 학습 종료===")
















