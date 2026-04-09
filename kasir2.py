from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    nama_toko = '=== Warung Kevin ==='
    alamat_toko = 'Panji Lor'
    no_hp = '012345678910'
    
    print(nama_toko)
    print(alamat_toko)
    print(no_hp)
    print('-' * 30)


# fungsi format rupiah
def format_rupiah(angka):
    return f"Rp.{angka:,}".replace(",", ".")


# data menu
data_menu = {
    1: ('nasi goreng', 12000),
    2: ('nasi padang', 10000),
    3: ('rendang', 15000),
    4: ('bakso', 10000),
}


# fungsi menampilkan menu
def tampil_menu():
    print('Daftar Menu Warung\n')
    for key, (nama, harga) in data_menu.items():
        print(f'{key}. {nama} - {format_rupiah(harga)}')
    print('-' * 30)


# Fungsi Input pesanan / menyimpan pesanan
daftar_pesanan = []

def input_pesanan():
    while True:
        try:
            pilih_menu = int(input('Masukkan nomor menu (0 untuk selesai): '))
            
            if pilih_menu == 0:
                if not daftar_pesanan:
                    print('Belum ada pesanan')
                    continue
                break
            
            if pilih_menu not in data_menu:
                print('Menu tidak tersedia')
                continue
            
            jumlah_menu = int(input('Masukkan jumlah pesanan: '))
            
            if jumlah_menu <= 0:
                print('Jumlah harus lebih dari 0')
                continue
            
            daftar_pesanan.append((pilih_menu, jumlah_menu))
        
        except ValueError:
            print('Input harus angka')


# fungsi untuk menghitung total harga dari pesanan 
def total_pesanan():
    print('\nTOTAL PESANAN\n')
    total_semua = 0

    for nomor, jumlah in daftar_pesanan:
        nama, harga = data_menu[nomor]
        total = jumlah * harga
        total_semua += total
        
        print(f'{nama} x{jumlah} = {format_rupiah(total)}')
    
    print('-' * 30)
    print(f'Total Semua: {format_rupiah(total_semua)}')
    return total_semua


# fungsi input bayar
def pembayaran(total):
    while True:
        try:
            bayar = int(input(f'\nTotal yang harus di bayar: {format_rupiah(int(total))}: '))
            
            if bayar >= total:
                return bayar
            else:
                print('Uang tidak cukup')
        
        except ValueError:
            print('Input harus angka')


# fungsi hitung diskon
def hitung_diskon(total):
    if total >= 100000:
        return total * 0.2
    elif total >= 50000:
        return total * 0.1
    else:
        return 0


# fungsi pajak
def hitung_pajak(setelah_diskon):
    return setelah_diskon * 0.1


# fungsi struk
def struk(total, bayar, diskon, setelah_diskon, pajak, total_akhir, waktu_transaksi, id_transaksi):
    
    teks = ''
    teks += 'Struk pembayaran\n'
    teks += f'ID Transaksi : {id_transaksi}\n'
    
    teks += f'Tanggal : {waktu_transaksi.strftime("%d-%m-%Y")}\n'
    teks += f'Waktu : {waktu_transaksi.strftime("%H:%M:%S")}\n'
    teks += '-'*30 + '\n'
    
    for nomor, jumlah in daftar_pesanan:
        nama, harga = data_menu[nomor]
        total_item = jumlah * harga
        teks += f'- {nama} x{jumlah} = {format_rupiah(total_item)}\n'
    
    teks += '-' * 30 + '\n'
    teks += f'Total           : {format_rupiah(total)}\n'
    teks += f'Diskon          : {format_rupiah(int(diskon))}\n'
    teks += f'Setelah diskon  : {format_rupiah(int(setelah_diskon))}\n'
    teks += f'Pajak (10%)     : {format_rupiah(int(pajak))}\n'
    teks += f'Total akhir     : {format_rupiah(int(total_akhir))}\n'
    teks += f'Bayar           : {format_rupiah(int(bayar))}\n'
    teks += f'Kembali         : {format_rupiah(int(bayar - total_akhir))}\n'
    teks += '-' * 30 + '\n'
    teks += 'TERIMA KASIH SUDAH BELI\n'

    return teks


# Fungsi Menyimpan struk pembayaran
def simpan_struk(teks):
    with open('riwayat.txt', 'a') as file:
        file.write(teks + '\n')
        file.write('=' * 40 + '\n')
        

# PROGRAM UTAMA
while True:
    clear()
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
    
    waktu_sekarang = datetime.now()
    id_transaksi = waktu_sekarang.strftime('TRX-%Y%m%d-%H%M%S')
    
    hasil_struk = struk(total, bayar, diskon, setelah_diskon, pajak, total_akhir, waktu_sekarang, id_transaksi)
    print(hasil_struk)
    
    simpan_struk(hasil_struk)
    
    ulang = input('Transaksi lagi (y/n): ').lower()
    if ulang != 'y':
        print('Program selesai')
        break