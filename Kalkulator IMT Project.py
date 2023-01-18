print ("Selamat Datang di Kalkulator IMT Mokleters")
print ('''\nHalo mokleters!! Gunakan kalkulator ini untuk memeriksa
Indeks Massa Tubuh(IMT)kalian dan mengecek apakah berat badan Anda
ideal atau tidak. Mempertahankan berat badan ideal juga sangat
penting bagi kesehatan. Jadi kita sebagai mokleters terlebih lagi
yang menjadi anak rantau harus menjaga berat badan agar terus sehat''')
gender1= ["Perempuan","perempuan"]
gender2= ["Laki laki","laki laki"]
print ("\nJenis kelamin")
print ("1. Perempuan \n2. Laki-laki")
jenis_kelamin=input ("\nApa jenis kelamin anda? ")
if jenis_kelamin=="Perempuan":
    jenis_kelamin=gender1[0]
    data_usia=input ("Berapa usia Anda? (tahun): ")
    data_tb=input ("Berapa tinggi Anda? (cm): ")
    data_bb=input ("Berapa berat badan Anda? (kg): ")
    a= float(data_tb)/float(100)
    b= (int(data_tb)-int(100))*int(15/100)
    total1=(int(data_tb)-int(100))-int(b)
    total2=float(data_bb)/(float(a)*float(a))
    print ("\nBerat badan ideal Anda adalah ", total1)
    print ("IMT Anda adalah ", total2)
    
if jenis_kelamin=="perempuan":
    jenis_kelamin=gender1[1]
if jenis_kelamin=="Laki laki":
    jenis_kelamin=gender2[0]
    data_usia=input ("Berapa usia Anda? (tahun): ")
    data_tb=input ("Berapa tinggi Anda? (cm): ")
    data_bb=input ("Berapa berat badan Anda? (kg): ")
    a= float(data_tb)/float(100)
    b= (int(data_tb)-int(100))*int(15/100)
    total1=(int(data_tb)-int(100))-int(b)
    total2=float(data_bb)/(float(a)*float(a))
    print ("\nBerat badan ideal Anda adalah ", total1)
    print ("IMT Anda adalah ", total2)
    
if jenis_kelamin=="laki laki":
    jenis_kelamin=gender2[1]


