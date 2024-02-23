gaji_pokok = int(input("Masukan jumlah gaji : "))
hari_kerja = int(input("Masukan jumlah hari kerja : "))
jam_lembur = int(input("Masukan jumlah jam lembur : "))

uang_transport = 100_000 * hari_kerja
uang_makan = 50_000 * hari_kerja

upah_lembur = 0
if jam_lembur <=2 :
    upah_lembur = jam_lembur *100_000
else :
    upah_lembur = 2 * 100_000 + (jam_lembur -2) * 150_000

    print ("Honor",gaji_pokok + uang_transport + uang_makan + upah_lembur)