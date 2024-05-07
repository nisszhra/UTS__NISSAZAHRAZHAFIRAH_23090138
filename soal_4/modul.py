def kategoribmi(bmi):
    if bmi < 18.5:
        print(f'Kategori BMI : Berat Badan Kurang')
    elif bmi >= 18.5 < 24.9:
        print(f'Kategori BMI : Berat Badan Normal')
    elif bmi >= 25 < 29.9:
        print(f'Kategori BMI : Kelebihan Berat Badan')
    elif bmi >= 30:
        print(f'Kategori BMI : Obesitas')
    else:
        exit()


