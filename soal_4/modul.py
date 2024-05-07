berat_badan = int(input("Masukan Berat Badan Anda (kg): "))
tinggi_badan = int(input("Masukan Tinggi Badan Anda (m) : "))

bmi = berat_badan / tinggi_badan * tinggi_badan

print('-'*10, 'Laporan Perhitungan BMI Anda', '-'*10)
print(f'Berat Badan : {berat_badan}')
print(f'Tinggi Badan : {tinggi_badan}')
print(f'Nilai BMI Anda : {bmi}')

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


