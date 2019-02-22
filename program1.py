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
