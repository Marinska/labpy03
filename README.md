# **Bahasa pemrogaman Python**

## **Materi**
## Perulangan atau looping
* Perulangan (for/counted loop) adalah perintah yang dieksekusi secara berdasarkan jumlah perulangan tertentu

## While
* Perulangan (while/uncounted loop), adalah perintah perulangan yang dilakukan berdasarkan kondisi bernilai TRUE

## Latihan1
* Pada latihan kali ini, yang akan dibahas adalah bagimana penggunakan perulangan for maupun while
* pada latihan satu, kita akan membuat sebuah program yang berisi
* menampilkan bilangan sebanyak n kali, dan bernilai kurang dari 0.5
* disini kita akan menggunakan kombinasi for dan while

## Flowchart
* Untuk alur pengerjaan latihan1, akan seperti diagram flowchart dibawah ini

![github](https://github.com/Marinska/labpy03/blob/master/7.PNG)

## Source code latihan1.py
* Berikut source code dari latihan1.py, beserta dengan comment dari setiap line order
```
from random import random                               ## mengimport fungsi random
n = int(input("Masukan nilai n = "))                    ## mengenalkan nilai n sebagai integer, dan menginputkan nilainya
for i in range(n):                                      ## perulangan sebanyak n kali
    data=random()                                       ## menentukan nilai data, sesuai dengan nilai random dari fungsi random
    while data > 0.5:                                   ## looping while, dimana program akan berjalan apabila nilai data lebih dari 0.5
        data=random()                                   ## program while yang akan berjalan yaitu, merequest nilai baru untuk variabel data dengan fungsi random
    print('Nilai data ke ', i+1,' adalah => ', data)    ## laporan nilai data
```

* Silahkan tuliskan source code pada lembar kerja kalian, kemudian save dan test program
![github](https://github.com/Marinska/labpy03/blob/master/1.PNG)


* Hasil menjalankan program latihan1.py
![github](https://github.com/Marinska/labpy03/blob/master/2.PNG)


## Latihan2
* Untuk latihan kedua, kita akan membuat sebuah program mengenai menentukan bilangan terbesar dari bilangan yang diinputkan
* nilai bilangan akan terus diinputkan, sampai nilai 0 terinput sebagai pemberhenti perulangan
* program yang akan kita buat akan menentukan bilangan terbesar dari semua bilangan yang telah kita inputkan

## Flowchart
* penjelasan mengenai flowchart dapat dilihat pada diagram flowchart dibawah
![github](https://github.com/Marinska/labpy03/blob/master/8.PNG)

## Source code latihan2.py
* source code latihan2.py terdapat dibawah ini beserta comment dari setiap line order
```
x = 0                                       ## memperkenalkan variabel x dengan nilai 0
n = int(input('Masukkan bilangan: '))       ## memperkenalkan variabel n sebagai integer, kemudian menginputkan nilainya
while n != 0:                               ## looping while apabila nilai n tidak sama dengan 0, dan untung memberhentikan looping apabila nilai n adalah 0
    n = int(input('Masukkan bilangan: '))   ## program yang akan dilooping
    if(n>x):                                ## if kondisi apabila nilai n lebih besar dari nilai x
        x=n                                 ## nilai x sama dengan nilai n
print('Bilangan terbesar adalah ', x)       ## nilai x sebagai bilangan n yang terbesar
```

* dalam penulisan dilembar kerja python
![github](https://github.com/Marinska/labpy03/blob/master/3.PNG)

* Save dan jalankan program untuk mengecek keberhasilan
![github](https://github.com/Marinska/labpy03/blob/master/4.PNG)


## Program1
* pada program satu kita akan membuat program perulangan sederhana
* pada program ini kita akan mengitung keuntungan dari usaha yang dimiliki oleh seorang pengusaha

## Kejelasan soal
* seorang pengusaha menginvestasikan uangnya sebesar Rp. 100.000.000 untuk modal awal
* disini kita mengetahui bahwa kita dapat membuat sebuah variabel modal dengan nilai 100000000
* kemudian pengusaha tersebut belum mendapatkan sebuah keuntungan maupun laba pada bulan pertama dan kedua
* pada bulan ke tiga, pengusaha sudah mendapatkan sebuah keuntungan, keuntungan tersebut berasal dari laba usaha sebesar 1% dari modal
* kita dapat membuat sebuah variabel laba dengan nilai dari modal*1%
* pada bulan kelima keuntungan pengusaha tersebut naik hingga 5%, yang tentu laba yang didapat berubah
* kita dapat merubah nilai variabel laba dengan nilai sesuai dengan kondisi yaitu laba sama dengan modal*5%
* namun tak disangka pada bulan ke delapan, keuntungan pengusaha tersebut berkurang
* ia memiliki penurunan laba sebesar 2%, dimana saat ini laba hanya sebesar 3%
* variabel laba harus disesuaikan dengan keadaan yang terjadi

## Flowchart
* untuk kejelasan alur pengerjaan, dapat dilihat dari flowchart dibawah ini
![github](https://github.com/Marinska/labpy03/blob/master/9.PNG)


## Source code program1
* source code beserta penjelasan setiap line order
```
modal = 100000000                                   ## memperkenalkan nilai modal
laba=0                                              ## nilai laba sama dengan 0
untung=0                                            ## demikian juga untung
for i in range(1,9,1):                              ## perulangan i dengan nilai awal 1, nilai akhir 9 dan step 1
    if(i<3):                                        ## kondisi apabila belum bulan ke-3, lama masih 0%
        laba=0
        untung=untung+laba
    elif(i<5):                                      ## kondisi apabila belum memasuki bulan ke-5, mendapat laba sebesar 1%
        laba=modal*1/100
        untung=untung+laba
    elif(i<8):                                      ## kondisi apabila belum memasuki bulan ke-8, mendapat laba sebesar 5%
        laba=modal*5/100
        untung=untung+laba
    else:                                           ## pada bulan ke-8 laba menurun 2% sehingga laba bulan ke-8 sebesar 3%
        laba=modal*3/100
        untung=untung+laba
    print('laba bulan ke-', i,' sebesar ', laba)    ## mencetak laporan laba tiap bulan
print('Total laba adalah: ', untung)                ## menghitung total laba selama 8 bulan
```

* Save lembar kerja

![github](https://github.com/Marinska/labpy03/blob/master/5.PNG)

* Jalankan program

![github](https://github.com/Marinska/labpy03/blob/master/6.PNG)

## Terima kasih
* Name : Umar Ibnu Zainal Muttaqin
* NIM : 311810909
* Kelas : TI.18.B.2