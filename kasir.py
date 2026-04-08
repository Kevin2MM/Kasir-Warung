import os

def header():
    nama_toko = '=== Warung Kevin ==='
    alamat_toko = 'Panji Lor'
    no_hp = '012345678910'
    
    print(nama_toko)
    print(alamat_toko)
    print(no_hp)
    print('-'*30)


# data menu
data_menu = {
    1:('nasi goreng', 12000),
    2:('nasi padang', 10000),
    3:('rendang', 15000),
    4:('bakso', 10000),
}
# fungsi fungsi yang mau di pakai
# fungsi untuk menampilkan daftar menu
def tampil_menu():
    print('Daftar Menu Warung \n')
    for key, (nama, harga) in data_menu.items():
        print(f'{key}. {nama} - Rp. {harga}')
    print('-'*30)
# Fungsi Input pesanan / menyimpan pesanan
daftar_pesanan = []
def input_pesanan():
    while True:
        try:
            pilih_menu = int(input('Massukkan nomor menu makan. ketik (0) jika sudah: '))
            
            if pilih_menu == 0:
                break
            
            if pilih_menu not in data_menu:
                print('Meu tidak tersedia')
                continue
            
            jumlah_menu = int(input('Masukkan jumlah pesanan: '))
            
            if jumlah_menu <= 0:
                print('Jumlah tidak boleh di bawah 0')
                continue
            
        except ValueError:
            print('Input harus angka')
        
        daftar_pesanan.append((pilih_menu, jumlah_menu))
# fungsi untuk menghitung total harga dari pesanan 

def total_pesanan():
    print('\nTOTAL PESANAN\n')
    total_semua = 0
    for nomor, jumlah in daftar_pesanan:
        nama, harga = data_menu[nomor]
        total = jumlah * harga
        total_semua += total
        
        print(f'{nama} x{jumlah} = Rp.{total}')
    
    print('-'*30)
    print(f'Total Semua: Rp.{total_semua}')
    return total_semua

# fungsi input bayar
def pembayaran(total):
    while True:
        try:
            bayar = int(input('Bayar: '))
            
            if bayar >= total:
                return bayar
            
            else:
                print('Uang tidak cukup')
        except ValueError:
            print('Input harus angka')
# fungsi hitung diskon
def hitung_diskon(total):
    if total >= 50000:
        return total * 0.1
    elif total >= 100000:
        return total * 0.2
    else:
        return 0
    

# fungsi pajak
def hitung_pajak(setelah_diskon):
    return setelah_diskon * 0.1


#fungsi struk
def struk(total, bayar, diskon, setelah_diskon, pajak, total_akhir):
    print('\nSTRUK PEMBAYARAN\n')
    
    for nomor, jumlah in daftar_pesanan:
        nama, harga = data_menu[nomor]
        total_item = jumlah * harga
        print(f'- {nama} x{jumlah} = Rp.{total_item}')
        
    print('-' * 30)
    print(f'Total           : Rp.{total}')
    print(f'Diskon          : Rp.{int(diskon)}')
    print(f'Setelah diskon  : Rp.{int(setelah_diskon)}')
    print(f'Pajak (10%)     : Rp.{int(pajak)}')
    print(f'Total akhir     : Rp.{int(total_akhir)}')
    print(f'Bayar           : Rp.{int(bayar)}')
    print(f'Kembali         : Rp.{int(bayar - total_akhir)}')
    print('-' * 30)
    print('TERIMA KASIH SUDAH BELI\n')
    
# PROGRAM UTAMA
while True:
    daftar_pesanan.clear()
    
    header()
    tampil_menu()
    input_pesanan()
    
    total = total_pesanan()
    
    diskon = hitung_diskon(total)
    setelah_diskon = total - diskon
    
    pajak = hitung_pajak(setelah_diskon)
    total_akhir = setelah_diskon + pajak
    
    bayar = pembayaran(total_akhir)
    
    struk(total, bayar, diskon, setelah_diskon, pajak, total_akhir)
    
    ulang = input('Transaksi lagi (y/n): ').lower()
    if ulang != 'y':
        print('program selesai')
        break
    