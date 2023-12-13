print('praktikum-d1')
print()
print('Nama Lengkap : Muhammmad Arisal Sawal')
print('NIM          : 231031107')
print('Prodi        : Sistem Informasi')

angkatan = 2023
print('Angkatan adalah',angkatan)

print()
a = 20
print('Data adalah =',a)
print('Tipenya adalah =',type(a))

print()
b = 20.0
print('Dta adalah =',b)
print('Tipenya adalah =',type(b))

print()
kampus = 'Institut Teknologi BJ Habibie'
print('Data adalah =',kampus)
print('Tipenya adalah =',type(kampus))

print()
log = True
print('Data adalah =',log)
print('Tipenya adalah =',type(log))

print()
c = complex(5,8)
print('Data adalah =',c)
print('Tipenya adalah =',type(c))

print()
p = 20
q = 5
hasil = p + q
print('Hasil',p,'+',q,'=',hasil)

print()
p = 20
q = 5
hasil = p - q
print('Hasil',p,'-',q,'=',hasil)

print()
p = 20
q = 5
hasil = p * q
print('Hasil',p,'x',q,'=',hasil)

print()
p = 20
q = 3
hasil = p / q
print('Hasil',p,'/',q,'=',hasil)

print()
p = 3
q = 2
hasil = p ** q
print('Hasil',p,'**',q,'=',hasil)

print()
p = 30
q = 31
hasil = p % q
print('Hasil',p,'%',q,'=',hasil)

print()
p = 30
q = 31
hasil = p // q
print('Hasil',p,'//',q,'=',hasil)

print()
a = 20
print('Nilai a adalah', a)
a = a + 1
print('Nilai a menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a += 1  #ini perintah a = a + 1
print('Nilai a menjadi', a)

print()
a = 25
print('Nilai a adalah', a)
a -= 2  #ini perintah a = a - 2
print('Nilai a menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a *= 2  #ini perintah a = a * 2
print('Nilai a*=2 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a /= 5  #ini perintah a = a / 5
print('Nilai a*=5 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a **= 2  #ini perintah a = a ** 2
print('Nilai a**=2 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a %= 7  #ini perintah a = a % 7
print('Nilai a%=7 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a //= 7  #ini perintah a = a // 7
print('Nilai a//=2 menjadi', a)

print() #ini operasi &
log = True
print('Nilai log adalah',log)
log |=False #ini perintah log= False log
print('Nilai log|=False menjadi',log)

print() #ini operasi OR
log = True
print('Nilai log adalah',log)
log |=False #ini perintah log= False log | False
print('Nilai log|=False menjadi',log)

print() #ini operasi AND
log = True
print('Nilai log adalah',log)
log |=False #ini perintah log= False log & False
print('Nilai log|=False menjadi',log)

print() #ini operasi XOR
log = True
print('Nilai log adalah',log)
log ^=True #ini perintah log= log ^ True
print('Nilai log|=False menjadi',log)

print() # ini operasi shifting
bi = 0b0100
print('Nilai bi =',format(bi,'04b'))
bi <<= 1 #menggeser digit ke kanan 1 kali
print('Nilai bi <<=1 menjadi',format(bi,'04b'))

print()
a = 20
hasil = a>15
print('hasil',a,'>15 adalah', hasil)

print()
a = 20
hasil = a==15
print('hasil',a,'==15 adalah', hasil)             

a=4
b=3
c=5
d=8
print('Diketahui Bilangan\n a =',a,'\n b =',b,'\n c =',c,'\n d =',d)
print()

hasil=a<b
print('Perbadingan antara a<b adalah',hasil)

hasil=a>b
print('Perbadingan antara a>b adalah',hasil)

hasil=a<b>c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

print()
a='berapakah'
b='jumlah'
c='nilai'
d='kamu'
hasil=a is 'dia'

print('a adalah "berapakah"',hasil)

print('a tidak "berapakah"', a is not "aku" )

print(a,b,c,d,'berapakah', a is c)