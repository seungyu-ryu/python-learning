# 함수 연습

# 기본 함수
def greet(name):
  """인사하는 함수"""
  return f"안녕하세요, {name}님!"

# 반환값이 있는 함수
def add_number(a, b):
  """두 수를 더해서 결과를 반환하는 함수"""
  result = a + b
  return result
sum_result = add_number(5, 3)
print(f"5+3={sum_result}")

#화학공학 관련 함수
def celsius to fahrenheit(celsius):
  """섭씨를 화씨로 변환"""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius
  
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



