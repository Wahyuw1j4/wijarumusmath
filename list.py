
print("=================")
print("LIST atau ARRAY")
print("=================")
data1 = [1, 3, 5, 6, 8, 10, 12]

print("Array : ", data1)
print()
subdata1 = data1[-2]
print("Nilai dari  data[-2]   adalah", subdata1)
subdata2 = data1[2]
print("Nilai dari  data[2]    adalah", subdata2)
subdata3 = data1[2:-2]
# Artinya 2 awal sampai 2 terakhir
print("Nilai dari  data[2:-2] adalah", subdata3,)
subdata3 = data1[2] + data1[5]
print("Jumlah dari data[2] dan data[5] adalah",
      data1[2], "+", data1[5], " = ", subdata3)
# menambahkan data pada array
data1.append(14)
print("tambah data1 menggunakan .append : ", data1)
# melihat panjang array
panjang = len(data1)
print("Panjang array adalah ", panjang)
# Merubah array menggunakan slice
data1[2] = 4
print("hasil dari slice diatas adalah", data1)

print()
print("====================")
print("Array multidemsional")
print("====================")
data2 = [10, 20, 30, 40, 50]
data3 = [data1, data2]
print("Array Multideminsion :", data3)
print()
print("Nilai dari data3[1][1] adalah ", data3[1][1])
print("Nilai dari data3[0][5] adalah ", data3[0][5])

print()
print("====================")
print("IF ELSE")
print("====================")

x = 26

if 25 <= x >= 35:
    print("halo")
elif x >= 15:
    print("ya")
else:
    print("Wow")

print()
print("====================")
print("FOR LOOP")
print("====================")


arr = [10, 15, 17, 18, 23, 23]

for i in arr:
    print(i, end=' ')
print()
print("====================")

for i in range(0, 10):
    for j in range(0, i - 1):
        print('*', end=' ')
    print('')
for i in range(10, 0, -1):
    for j in range(0, i-1):
        print("*", end=' ')
    print('')


print("====================")
print("WHILE LOOP")
print("====================")

i = 0
while i < 12123120:  # Sampai ke
    print(i, end=' ')
    i += 1
    if i == 25:  # dihentikan
        break
print('')

print('')
print("====================")
print("FUNCTIONS")
print("====================")
print("")


def volume(p, l, t):
    vol = p * l * t
    print('Volume balok adalah', vol)


volume(5, 3, 1)


def kata(argu):
    print("")
    print("====================")
    print(argu)
    print("====================")
    print("")

kata('RETURN VELUE')
def tambah(x,y):
    tambah = x + y
    print(x, '+', y, '=', tambah)
    return tambah

def kali(x,y):
    kali = x * y
    print(x, '*', y, '=', kali)
    return kali
    
a = tambah(10,-2)
b = kali(3,-2)
print(a * b)

x = input('Masukan Nama Kamu : ')
print("Nama Kamu : ", x)