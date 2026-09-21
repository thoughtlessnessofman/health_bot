
# имт
def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / height_m ** 2
    bmi_value = round(bmi, 1)

    if bmi_value <= 16.0:
        category = "Выраженный дефицит массы тела"
    elif bmi_value < 18.5:
        category = "Недостаточная (дефицит) масса тела"
    elif bmi_value < 25.0:
        category = "Норма"
    elif bmi_value < 30.0:
        category = "Избыточная масса тела (предожирение)"
    elif bmi_value < 35.0:
        category = "Ожирение первой степени"
    elif bmi_value < 40.0:
        category = "Ожирение второй степени"
    else:
        category = "Ожирение третьей степени (морбидное)"

    return bmi_value, category

#калории
def calculate_bmr(weight, height, age, gender, activity_level = 1.2):
    bmr = 10 * weight + 6.25 * height - 5 * age
    bmr += 5 if gender == "male" else - 161
    bmr = bmr * activity_level
    return int(bmr)

# давление
def evaluate_pressure(systolic, diastolic):
    if systolic >= 180 or diastolic >= 110:
        return "Высокое (АГ 3 степени)"
    elif systolic >= 160 or diastolic >= 100:
        return "Высокое (АГ 2 степени)"
    elif systolic >= 140 or diastolic >= 90:
        return "Высокое (АГ 1 степени)"
    elif systolic >= 130 or diastolic >= 85:
        return "Высокое нормальное (предгипертония)"
    elif systolic >= 120 or diastolic >= 80:
        return "Нормальное"
    else:
        return "Оптимальное (идеальное)"




if __name__ == "__main__":
    imt_spisok = [(183, 75), (177, 55), (191, 191), (200, 100)]
    for h, w in imt_spisok:
        bmi_v, bmi_cat = calculate_bmi(h, w)
        print(f"ИМТ: {bmi_v}, Категория: {bmi_cat}")

    print("\nТест BMR (калории):")
    print("Мужчина 75кг, 183см, 18 лет:", calculate_bmr(75, 183, 18, "male"))
    print("Женщина 60кг, 165см, 20 лет:", calculate_bmr(60, 165, 20, "female"))

    print("\nТест давления:")
    print("115/75 ->", evaluate_pressure(115, 75))
    print("135/85 ->", evaluate_pressure(135, 85))
    print("150/95 ->", evaluate_pressure(150, 95))

