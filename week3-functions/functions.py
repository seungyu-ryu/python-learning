# 함수 연습

# 기본 함수
def greet(name):
  """인사하는 함수"""
  return f"안녕하세요, {name}님!"

# 반환값이 있는 함수
def add_number(a, b):           # a, b 는 parameter
  """두 수를 더해서 결과를 반환하는 함수"""
  result = a + b
  return result
sum_result = add_number(5, 3)   # 5, 3은 argument
print(f"5+3={sum_result}")
print()

#화학공학 관련 함수
def celsius_to_fahrenheit(celsius):
  """섭씨를 화씨로 변환"""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f}°F = {temp_c:.1f}°C")
print()

def calculate_molarity(moles, volume_L):
  """몰농도 계산 (mol/L)"""
  molarity = mole /volume_L
  return molarity

def calculate_mass_percent(solute_mass, solution_mass):
  """질량 퍼센트 계산"""
  mass_percent = (solute_mass / solution_mass) * 100
  return mass_percent
moles = 2.5
volume = 1.0
molarity = calculate_molarity(moles, volume)
print(f"몰농도 : {moles}mol / {volum}L = {molarity}M")

solute = 50     # 용질 질량 g
solution = 250  # 용액 질량 g
mass_percent = calculate_mass_percent(solute, solution)
print(f"질량 퍼센트: {solute}g / {solution}g = {mass_percent}%")
print()

def calculate_density(mass, volume):
  """밀도 계산 함수 (kg/m³)"""
  if volume == 0:
    return f"부피가 0이면 계산할 수 없습니다."
  density = mass / volume
  return f"밀도: {density:.2f} kg/m³"
  
def reynolds_number(density, velocity, diameter, viscosity):
 """레이놀즈 수 계산"""
  if viscosity == 0:
    return "점성도가 0이면 계산할 수 없습니다."
  re = (density * velocity * diameter) / viscosity
  return f"레이놀즈 수: {re:.2f}"

def flow_regime(re_number):
  """유동 상태 판정"""
  if re_number < 2100:
    return "층류 (Laminar flow)"
  elif re_number > 4000:
    return "난류 (Turbulent flow)"
  else:
    return "전이 영역(Transition zone)"

# 함수 사용 예제 
print("=== 함수 연습 ===")
print(greet("승유"))

# 밀도 계산 
print(calculate_density(1000, 2))   # 물의 밀도 근사값

# 레이놀즈 수 계산 예제
density = 1000     # kg/m³
velocity = 2       # m/s
diameter = 0.1     # m
viscosity = 0.001  # Pa·s

re = reynolds_number(density, velocity, diameter, viscosity)
print(re)

# 추출한 레이놀즈 수로 유동 상태 판정
re_value = 20000
print(flow_regime(re))

def ideal_gas_pressure(n, R, T, P):
  """이상기체 방정식으로 부피 계산"""
  V = (n * R * T) / P
  return V

def ideal_gas_pressure(n, R, T, V):
  """이상기체 방정식으로 압력 계산"""
  P = (n * R * T) / V
  return P

#조건: 1mol 기체, 25°C, 1atm
n = 1.0  # mol
R = 0.0821  # L·atm/(mol·K)
T = 25 + 273.15  # K
P = 1.0  # atm

volume = ideal_gas_volume(n, R, T, P)
print(f"이상기체 부피: {volume:.2f}L")

def reaction_rate(concentration, temperature, rate_constanr=1.0):
  """반응 속도 계산 (간단한 1차 반응)"""
  rate = rate_constant * concentrate * (temperature/298.15)
  return rate
conc = 0.1
temp = 323.15
rate1 = reation_rate(conc, temp)
rate2 = reaction_rate(conc, temp, 2.5) # 다른 속도 상수
print(f"반응 속도 (k=1.0): {rate1:.4f}") 
print(f"반응 속도 (k=1.0): {rate2:.4f}")
print()

def calculate_heat(mass, specific_heat, delta_temperature):
  













