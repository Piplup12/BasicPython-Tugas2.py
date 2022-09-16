nama_kontak=['Farhan', 'Joko']
nomor_telepon=['08123456789', '08987654321']
def daftar_kontak():
    print('Daftar Kontak: ')
    for i in range(len(nama_kontak)):
        print('Nama: {}'.format(nama_kontak[i]))
        print('Nomor Telepon: {}'.format(nomor_telepon[i]))

def tambah_kontak():
    nama_kontak.append(input('Nama: '))
    nomor_telepon.append(input('No Telepon: '))
    print('Kontak berhasil ditambahkan')

print('Selamat Datang!')
while True:
    print('---Menu---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('2. Keluar')
    menu=int(input('Pilih Menu: '))
    if menu==1:
        daftar_kontak()
    elif menu==2:
        tambah_kontak()
    elif menu==3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia.')