x = 0                                       ## memperkenalkan variabel x dengan nilai 0
n = int(input('Masukkan bilangan: '))       ## memperkenalkan variabel n sebagai integer, kemudian menginputkan nilainya
while n != 0:                               ## looping while apabila nilai n tidak sama dengan 0, dan untung memberhentikan looping apabila nilai n adalah 0
    n = int(input('Masukkan bilangan: '))   ## program yang akan dilooping
    if(n>x):                                ## if kondisi apabila nilai n lebih besar dari nilai x
        x=n                                 ## nilai x sama dengan nilai n
print('Bilangan terbesar adalah ', x)       ## nilai x sebagai bilangan n yang terbesar
