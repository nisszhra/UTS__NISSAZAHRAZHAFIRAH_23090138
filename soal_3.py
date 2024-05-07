jumlah_barang = int(input('Masukan Jumlah Barang : '))

total = 0

for i in range(jumlah_barang):
    harga_barang = int(input('Masukan Harga : '))
    total += harga_barang

print(f'Total Belanja : Rp {total:,.2f}')