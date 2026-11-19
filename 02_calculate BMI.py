def calculate_bmi(weight, height):
    w = weight
    h = height
    return float(w) / (float(h) ** 2)

def calculate_sector(central_angle,radius):
    sector_area=float(central_angle)/360*radius**2*3.14
    print(f"the square of sector is {sector_area}")


calculate_sector(180,1)

user_weight = input("how much is your weight(kg):")
user_height = input("how much is your height(m):")
result = calculate_bmi(user_weight, user_height)
print(f"your BMI is:{result} ", end="")
