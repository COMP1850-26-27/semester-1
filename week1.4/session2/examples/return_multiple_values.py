# code example on slide 12 & 13
def return_constants():
    PI = 3.14159
    GRAVITY = 9.8
    SPEED_OF_LIGHT = 299792458
    return PI, GRAVITY, SPEED_OF_LIGHT


pi, gravity, light_speed = return_constants()
print(pi, gravity, light_speed, sep=", ")   # # 3.14159, 9.8, 299792458


# code example on slide 14
def person_info(name, age):
    upper_name = name.upper()
    age_in_10_years = age + 10
    is_adult = age >= 18
    return upper_name, age_in_10_years, is_adult


name, age, adult = person_info("Bob", 25)
print(f"Name: {name}")            # Name: BOB
print(f"Age in 10 years: {age}")  # Age in 10 years: 35
print(f"Is adult: {adult}")       # Is adult: True


# code example on slide 15
def person_info(name, age):
    info = {}
    info['name'] = name.upper()
    info['age_in_10_years'] = age + 10
    info['is_adult'] = age >= 18
    return info


adult = person_info("ali", 30)
print(adult)  # {'name': 'ALI', 'age_in_10_years': 40, 'is_adult': True}


# code example on slide 16
def demo(number):
    if number < 0:
        return "value1", "value2", "value3"
    else:
        return "value1"


print(demo(5))       # value1
print(demo(-1))      # ('value1', 'value2', 'value3')
