import random

class GenerateData:
  def generate_inn():
      # Первые 10 цифр — случайные, но первая не 0
      digits = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(9)]
    
      # Расчёт 11-й контрольной цифры
      weights_11 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
      control_11 = sum(d * w for d, w in zip(digits, weights_11)) % 11 % 10
      digits.append(control_11)
    
      # Расчёт 12-й контрольной цифры
      weights_12 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
      control_12 = sum(d * w for d, w in zip(digits, weights_12)) % 11 % 10
      digits.append(control_12)

      valid_inn = ''.join(map(str, digits))
    
      return valid_inn
  
  
def generate_passport():
    # Серия: код региона (01–99) + год выпуска (00–24) с спецификатором формата
    region_code = f"{random.randint(1, 99):02d}"
    year = f"{random.randint(0, 24):02d}"
    series = region_code + year
    
    # Номер: 6 цифр, не все нули
    number = f"{random.randint(1, 999999):06d}"
    
    return series, number
