harga_belanja = int(input("Masukkan total harga belanja: "))
diskon = 0
if harga_belanja > 60000:
    diskon = 10000
total_harga = harga_belanja - diskon
print("Jumlah yang harus dibayar: ", total_harga, "rupiah")