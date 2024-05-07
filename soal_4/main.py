import modul

berat_badan = int(input("Masukan Berat Badan Anda (kg): "))
tinggi_badan = int(input("Masukan Tinggi Badan Anda (m) : "))

bmi = berat_badan / tinggi_badan * tinggi_badan

print('-'*10, 'Laporan Perhitungan BMI Anda', '-'*10)
print(f'Berat Badan : {berat_badan}')
print(f'Tinggi Badan : {tinggi_badan}')
print(f'Nilai BMI Anda : {bmi}')

modul.kategoribmi(bmi)