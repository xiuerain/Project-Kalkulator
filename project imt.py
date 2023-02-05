print ("ˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉ")
print ("\t\tSelamat Datang di Kalkulator IMT Mokleters")
print ("ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ")
print ('''\nHalo mokleters!!
Berat badan ideal tentunya adalah impian semua orang.
Mempertahankan berat badan ideal juga sangat penting bagi kesehatan.
kita sebagai mokleters yang sedang merantau harus menjaga berat badan
ideal agar tetap sehat. Gunakan kalkulator ini untuk memeriksa apakah
berat badan kalian ideal atau tidak. Kami akan memberikan beberapa
Tips and Tricks yang tepat untuk kalian <3''')
gender1= ["Perempuan","perempuan"]
gender2= ["Laki laki","laki laki"]
print ("\nJenis kelamin")
print ("1. Perempuan \n2. Laki laki")
jenis_kelamin=input ("\nApa jenis kelamin anda? ")
if jenis_kelamin=="Perempuan":
    jenis_kelamin=gender1[0]
    data_usia=input ("Berapa usia Anda? (tahun): ")
    data_tb=input ("Berapa tinggi Anda? (cm): ")
    data_bb=input ("Berapa berat badan Anda? (kg): ")
    a= float(data_tb)/float(100)
    b= int(data_tb)-int(100)
    c= float(b)*float(15/100)
    total1= int(b)-int(c)
    total2=float(data_bb)/(float(a)*float(a))
    print ("\nBerat badan ideal Anda adalah ", total1)
    print ("IMT Anda adalah ", (round (total2, 2)) )
    if (total2 < 18.5):
        print ('''\n\t\tKekurangan Bobot 
\nKondisi
ˉˉˉˉˉˉˉ
Nilai IMT anda di bawah 18.5 menandakan berat badan anda kurang (underweight).

Saran
ˉˉˉˉˉˉ
Untuk meningkatkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Saat jam istirahat, makan makanan yang bergizi dan tinggi nutrisi seperti sayur-sayuran,
buah-buahan, dan kacang-kacangan di kantin sekolah. Selain itu, makan juga makanan tinggi
protein seperti daging merah, tahu, tempe, daging ayam tanpa kulit, dll.
- Jika jajan di kopsis (koperasi siswa) sering memakan cemilan sehat diantara makan utama
seperti buah-buahan, salad, kacang-kacangan, dll.
- Rajin meminum susu dan jus yang dijual di kantin maupun kopsis (koperasi siswa).
- Minum air putih cukup sekitar 2 liter per hari.
- Ketika di hadapan kulkas kopsis (koperasi siswa) harap hindari minuman yang mengandung
kafein dan bersoda
- Jangan minum terlalu banyak saat makan karena akan cepat kenyang. Sebaiknya minum ditengah
makan atau setelah makan.
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Jangan merokok dan minum alkohol
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat menambah berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')
    if (total2 > 18.5 and total2 <= 22.9):
        print ('''\n\t\tNormal 
\nKondisi
ˉˉˉˉˉˉˉ
Jika IMT anda 18.5 sampai 22.9 artinya anda memiliki berat badan yang normal.

Saran
ˉˉˉˉˉˉ
Jika Anda ingin menjaga berat badan, penting untuk mengetahui berapa banyak kalori yang dibutuhkan
per harinya, agar tubuh mampu melakukan fungsinya dalam beraktivitas sehari-hari. Anda perlu mengonsumsi
makanan dan minuman dengan jumlah kalori harian yang sesuai dengan kebutuhan tubuh!! Pertahankan ฅ^•ﻌ•^ฅ ''')
    if (total2 > 23):
        print ('''\n\t\tKelebihan bobot
\nKondisi
ˉˉˉˉˉˉˉ
Anda dianggap memiliki kelebihan berat badan, jika indeks massa tubuh (IMT) lebih dari 23

Saran
ˉˉˉˉˉˉ
Untuk menurunkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Disarankan untuk mengonsumsi makanan berprotein dan berserat.
- Saat jam istirahat, batasi makanan yang kurang sehat.
- Makan dalam porsi kecil dan secara perlahan.
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat mengurangi berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')

if jenis_kelamin=="perempuan":
    jenis_kelamin=gender1[1]
    data_usia=input ("Berapa usia Anda? (tahun): ")
    data_tb=input ("Berapa tinggi Anda? (cm): ")
    data_bb=input ("Berapa berat badan Anda? (kg): ")
    a= float(data_tb)/float(100)
    b= int(data_tb)-int(100)
    c= float(b)*float(15/100)
    total1= int(b)-int(c)
    total2=float(data_bb)/(float(a)*float(a))
    print ("\nBerat badan ideal Anda adalah ", total1)
    print ("IMT Anda adalah ", (round (total2, 2)) )
    if (total2 < 18.5):
        print ('''\n\t\tKekurangan Bobot 
\nKondisi
ˉˉˉˉˉˉˉ
Nilai IMT anda di bawah 18.5 menandakan berat badan anda kurang (underweight).

Saran
ˉˉˉˉˉˉ
Untuk meningkatkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Saat jam istirahat, makan makanan yang bergizi dan tinggi nutrisi seperti sayur-sayuran,
buah-buahan, dan kacang-kacangan di kantin sekolah. Selain itu, makan juga makanan tinggi
protein seperti daging merah, tahu, tempe, daging ayam tanpa kulit, dll.
- Jika jajan di kopsis (koperasi siswa) sering memakan cemilan sehat diantara makan utama
seperti buah-buahan, salad, kacang-kacangan, dll.
- Rajin meminum susu dan jus yang dijual di kantin maupun kopsis (koperasi siswa).
- Minum air putih cukup sekitar 2 liter per hari.
- Ketika di hadapan kulkas kopsis (koperasi siswa) harap hindari minuman yang mengandung
kafein dan bersoda
- Jangan minum terlalu banyak saat makan karena akan cepat kenyang. Sebaiknya minum ditengah
makan atau setelah makan.
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Jangan merokok dan minum alkohol
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat menambah berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')
    if (total2 > 18.5 and total2 <= 22.9):
        print ('''\n\t\tNormal 
\nKondisi
ˉˉˉˉˉˉˉ
Jika IMT anda 18.5 sampai 22.9 artinya anda memiliki berat badan yang normal.

Saran
ˉˉˉˉˉˉ
Jika Anda ingin menjaga berat badan, penting untuk mengetahui berapa banyak kalori yang dibutuhkan
per harinya, agar tubuh mampu melakukan fungsinya dalam beraktivitas sehari-hari. Anda perlu mengonsumsi
makanan dan minuman dengan jumlah kalori harian yang sesuai dengan kebutuhan tubuh!! Pertahankan ฅ^•ﻌ•^ฅ ''')
    if (total2 > 23):
        print ('''\n\t\tKelebihan bobot
\nKondisi
ˉˉˉˉˉˉˉ
Anda dianggap memiliki kelebihan berat badan, jika indeks massa tubuh (IMT) lebih dari 23

Saran
ˉˉˉˉˉˉ
Untuk menurunkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Disarankan untuk mengonsumsi makanan berprotein dan berserat.
- Saat jam istirahat, batasi makanan yang kurang sehat.
- Makan dalam porsi kecil dan secara perlahan.
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat mengurangi berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')

    
if jenis_kelamin=="Laki laki":
    jenis_kelamin=gender2[0]
    data_usia=input ("Berapa usia Anda? (tahun): ")
    data_tb=input ("Berapa tinggi Anda? (cm): ")
    data_bb=input ("Berapa berat badan Anda? (kg): ")
    a= float(data_tb)/float(100)
    b= int(data_tb)-int(100)
    c= float(b)*float(10/100)
    total1= int(b)-int(c)
    total2=float(data_bb)/(float(a)*float(a))
    print ("\nBerat badan ideal Anda adalah ", total1)
    print ("IMT Anda adalah ",(round (total2, 2)) )
    if (total2 < 18.5):
        print ('''\n\t\tKekurangan Bobot 
\nKondisi
ˉˉˉˉˉˉˉ
Nilai IMT anda di bawah 18.5 menandakan berat badan anda kurang (underweight).

Saran
ˉˉˉˉˉˉ
Untuk meningkatkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Saat jam istirahat, makan makanan yang bergizi dan tinggi nutrisi seperti sayur-sayuran,
buah-buahan, dan kacang-kacangan di kantin sekolah. Selain itu, makan juga makanan tinggi
protein seperti daging merah, tahu, tempe, daging ayam tanpa kulit, dll.
- Jika jajan di kopsis (koperasi siswa) sering memakan cemilan sehat diantara makan utama
seperti buah-buahan, salad, kacang-kacangan, dll.
- Rajin meminum susu dan jus yang dijual di kantin maupun kopsis (koperasi siswa).
- Minum air putih cukup sekitar 2 liter per hari.
- Ketika di hadapan kulkas kopsis (koperasi siswa) harap hindari minuman yang mengandung
kafein dan bersoda
- Jangan minum terlalu banyak saat makan karena akan cepat kenyang. Sebaiknya minum ditengah
makan atau setelah makan.
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Jangan merokok dan minum alkohol
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat menambah berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')
    if (total2 > 18.5 and total2 <= 22.9):
        print ('''\n\t\tNormal 
\nKondisi
ˉˉˉˉˉˉˉ
Jika IMT anda 18.5 sampai 22.9 artinya anda memiliki berat badan yang normal.

Saran
ˉˉˉˉˉˉ
Jika Anda ingin menjaga berat badan, penting untuk mengetahui berapa banyak kalori yang dibutuhkan
per harinya, agar tubuh mampu melakukan fungsinya dalam beraktivitas sehari-hari. Anda perlu mengonsumsi
makanan dan minuman dengan jumlah kalori harian yang sesuai dengan kebutuhan tubuh!! Pertahankan ฅ^•ﻌ•^ฅ ''')
    if (total2 > 23):
        print ('''\n\t\tKelebihan bobot
\nKondisi
ˉˉˉˉˉˉˉ
Anda dianggap memiliki kelebihan berat badan, jika indeks massa tubuh (IMT) lebih dari 24

Saran
ˉˉˉˉˉˉ
Untuk menurunkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Disarankan untuk mengonsumsi makanan berprotein dan berserat.
- Saat jam istirahat, batasi makanan yang kurang sehat.
- Makan dalam porsi kecil dan secara perlahan.
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat mengurangi berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')
    
if jenis_kelamin=="laki laki":
    jenis_kelamin=gender2[1]
    data_usia=input ("Berapa usia Anda? (tahun): ")
    data_tb=input ("Berapa tinggi Anda? (cm): ")
    data_bb=input ("Berapa berat badan Anda? (kg): ")
    a= float(data_tb)/float(100)
    b= int(data_tb)-int(100)
    c= float(b)*float(10/100)
    total1= int(b)-int(c)
    total2=float(data_bb)/(float(a)*float(a))
    print ("\nBerat badan ideal Anda adalah ", total1)
    print ("IMT Anda adalah ",(round (total2, 2)) )
    if (total2 < 18.5):
        print ('''\n\t\tKekurangan Bobot 
\nKondisi
ˉˉˉˉˉˉˉ
Nilai IMT anda di bawah 18.5 menandakan berat badan anda kurang (underweight).

Saran
ˉˉˉˉˉˉ
Untuk meningkatkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Saat jam istirahat, makan makanan yang bergizi dan tinggi nutrisi seperti sayur-sayuran,
buah-buahan, dan kacang-kacangan di kantin sekolah. Selain itu, makan juga makanan tinggi
protein seperti daging merah, tahu, tempe, daging ayam tanpa kulit, dll.
- Jika jajan di kopsis (koperasi siswa) sering memakan cemilan sehat diantara makan utama
seperti buah-buahan, salad, kacang-kacangan, dll.
- Rajin meminum susu dan jus yang dijual di kantin maupun kopsis (koperasi siswa).
- Minum air putih cukup sekitar 2 liter per hari.
- Ketika di hadapan kulkas kopsis (koperasi siswa) harap hindari minuman yang mengandung
kafein dan bersoda
- Jangan minum terlalu banyak saat makan karena akan cepat kenyang. Sebaiknya minum ditengah
makan atau setelah makan.
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Jangan merokok dan minum alkohol
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat menambah berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')
    if (total2 > 18.5 and total2 <= 22.9):
        print ('''\n\t\tNormal 
\nKondisi
ˉˉˉˉˉˉˉ
Jika IMT anda 18.5 sampai 22.9 artinya anda memiliki berat badan yang normal.

Saran
ˉˉˉˉˉˉ
Jika Anda ingin menjaga berat badan, penting untuk mengetahui berapa banyak kalori yang dibutuhkan
per harinya, agar tubuh mampu melakukan fungsinya dalam beraktivitas sehari-hari. Anda perlu mengonsumsi
makanan dan minuman dengan jumlah kalori harian yang sesuai dengan kebutuhan tubuh!! Pertahankan ฅ^•ﻌ•^ฅ ''')
    if (total2 > 23):
        print ('''\n\t\tKelebihan bobot
\nKondisi
ˉˉˉˉˉˉˉ
Anda dianggap memiliki kelebihan berat badan, jika indeks massa tubuh (IMT) lebih dari 24

Saran
ˉˉˉˉˉˉ
Untuk menurunkan berat badan, Anda dapat melakukan hal-hal berikut edisi anak Mokleters:
- Selain olahraga dalam pelajaran sekolah dan jumat sehat, Mokleters juga harus rajin lahraga
teratur seperti bersepeda(TSCC) jogging, angkat beban, aerobik, berenang, dll. Olahraga dapat
membentuk otot serta menambah nafsu makan Anda.
- Meskipun memiliki tugas yang banyak, anak Mokleters juga harus istirahat yang cukup
- Disarankan untuk mengonsumsi makanan berprotein dan berserat.
- Saat jam istirahat, batasi makanan yang kurang sehat.
- Makan dalam porsi kecil dan secara perlahan.
- Kurangi stres

Semoga dengan melakukan hal-hal tersebut, Mokleters dapat mengurangi berat badan sehingga
mencapai berat badan yang ideal!! Semangat ฅ^•ﻌ•^ฅ''')

