from random import random                               ## mengimport fungsi random
n = int(input("Masukan nilai n = "))                    ## mengenalkan nilai n sebagai integer, dan menginputkan nilainya
for i in range(n):                                      ## perulangan sebanyak n kali
    data=random()                                       ## menentukan nilai data, sesuai dengan nilai random dari fungsi random
    while data > 0.5:                                   ## looping while, dimana program akan berjalan apabila nilai data lebih dari 0.5
        data=random()                                   ## program while yang akan berjalan yaitu, merequest nilai baru untuk variabel data dengan fungsi random
    print('Nilai data ke ', i+1,' adalah => ', data)    ## laporan nilai data
