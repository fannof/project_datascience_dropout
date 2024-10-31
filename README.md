# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Sekolah ingin menganalisis berbagai faktor yang mempengaruhi kinerja akademik dan kelulusan siswa. Berdasarkan data seperti status sosial ekonomi, kualifikasi orang tua, status beasiswa, pekerjaan orang tua, serta kinerja siswa pada semester sebelumnya, sekolah berusaha untuk memahami dan mengidentifikasi siswa yang berisiko gagal atau tidak lulus tepat waktu. Dengan demikian, sekolah dapat memberikan intervensi yang tepat kepada kelompok siswa yang membutuhkan serta menganalisis siswa yang memungkinkan dropout untuk diminimalisir dengan membuat sistem machine learning yang mampu memprediksi tingkat dropout. Berikut adalah pertanyaan bisnis yang dapat diuraikan:

1. Apa faktor-faktor utama yang memengaruhi kelulusan dan prestasi akademik mahasiswa?
2. Bagaimana faktor usia, pekerjaan orang tua, dan status internasional dapat mempengaruhi prestasi akademik siswa?
3. Apakah siswa yang mendapatkan beasiswa memiliki peluang lebih besar untuk lulus tepat waktu dibandingkan yang tidak?
4. Bagaimana pengaruh kualifikasi orang tua dan status pekerjaan terhadap performa siswa?
5. Berapa nilai rata-rata siswa yang melakukan dropout?
6. Apakah status pernikahan seperti belum menikah, menikah dan sudah bercerai mempengaruhi performa siswa dalam belajar?

### Cakupan Proyek
Untuk menjawab permasalahan bisnis diatas, akan dilakukan identifikasi terhadap faktor-faktor yang mengakibatkan tingkat dropout siswa tinggi yakni 32%. Sekolah ingin memanfaatkan data historis siswa untuk memprediksi kinerja akademik mereka dan mengidentifikasi siswa yang berpotensi mengalami kesulitan akademik, sehingga mengakibatkan dropout. Dengan pemahaman ini, intervensi dini dapat diberikan untuk meningkatkan peluang kelulusan dan kinerja siswa serta mengurangi presentase siswa yang akan dropout. Hal-hal yang dilakukan adalah menilai apakah ada hubungan langsung antara rata-rata nilai siswa dan keputusan untuk dropout apakah karena alasan dengan status pernikahan, dan apakah penyesuaian beasiswa dapat mengurangi tingkat dropout dikarenakan siswa kekurangan biaya. Dan membuat dashboard yang bersifat interaktif (menggunakan Metabase) yang menunjukkan metrik penting seperti tingkat dropout, distribusi siswa berdasarkan pendidikan, status pernikahan, dan pekerjaan orang tua, serta membangun model prediksi untuk mengetahui probabilitas siswa yang akan dropout dari sekolah, sehingga bisa diambil tindakan preventif menggunakan algoritma seperti decision tree, random forest dan gradien boosting lalu mengevaluasi performa model dengan beberapa metrik seperti accuracy, precision, dan recall.

### Persiapan

Sumber data: <a href="https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv">Dataset Student Jaya Jaya Insitute</a>

Setup environment:

- Buka terminal atau command prompt, lalu masukan perintah dibawah ini

```
conda create --name students_performance python=3.9
```

- Aktifkan environment yang baru dibuat

```
conda activate students_performance
```

- Download semua dependencies yang berada di file requirements.txt

```
pip install -r requirements.txt
```

- Buat kernel baru bernama 'students_performance' di jupyter

```
python -m ipykernel install --user --name students_performance --display-name "students_performance"
```
- Setelah semua selesai, buka Jupyter Notebook

```
jupyter notebook
```

## Business Dashboard
![dropout_analytics](https://github.com/user-attachments/assets/2880ab45-d7cb-497a-8677-090fbc273003)

Dashboard Dropout Analytics ini memberikan wawasan tentang berbagai faktor yang terkait dengan dropout dan kelulusan siswa dari institusi pendidikan. Berikut adalah deskripsi dari setiap bagian dashboard:

- Visualisasi pertama menampilkan distribusi jumlah siswa berdasarkan program studi (course). Kategori Business memiliki persentase siswa tertinggi (40%), diikuti oleh Engineering (26%), Health (15%), dan Other (18%).
- Visualisasi kedua menunjukkan distribusi gender dari seluruh siswa. Sebagian besar siswa adalah perempuan (65%), dan sisanya laki-laki (35%).
- Visualisasi ketiga menunjukkan persentase siswa internasional. Hanya 2.49% siswa yang berasal dari luar negeri, sementara 97.51% siswa berasal dari dalam negeri.
- Visualisasi keempat menunjukkan berbagai pekerjaan ibu dari siswa yang didaftarkan. Pekerjaan ibu yang paling umum adalah Manual Labor dengan 1.996 siswa, diikuti oleh Professional (921), Other (774), dan Student (233).
- Visualisasi kelima menampilkan pekerjaan ayah siswa dengan distribusi yang dominan pada pekerjaan Manual Labor (2.285 siswa), diikuti oleh Professional (730), dan Other (94).
- Visualisasi keenam membandingkan rata-rata nilai Admission Grade dan Total Units Grade antara siswa yang dropout dan yang lulus. Siswa yang dropout cenderung memiliki nilai yang lebih rendah baik pada Admission Grade maupun Total Units Grade dibandingkan siswa yang lulus.
- Visualisasi ketujuh menunjukkan hubungan antara status perkawinan siswa dengan jumlah yang dropout. Single (lajang) memiliki angka dropout tertinggi (2.015 siswa), diikuti oleh Married (634), dan status perkawinan lainnya seperti Divorced dan Other memiliki angka yang lebih kecil.
- Visualisasi kedelapan menampilkan distribusi jumlah dropout dan lulusan berdasarkan kelompok umur siswa. Dropout paling banyak terjadi pada siswa usia 22-24 tahun, dengan jumlah lebih dari 1.200 siswa.
- Visualisasi kesembilan menunjukkan hubungan antara status penerima beasiswa dengan dropout atau kelulusan. Siswa yang tidak menerima beasiswa memiliki dropout yang lebih tinggi dibandingkan dengan yang menerima beasiswa.
- Visualisasi kesepuluh memberikan gambaran persentase total siswa yang dropout, sedang terdaftar, atau sudah lulus. Dropout mencakup 32% dari total siswa (4.424), 18% masih terdaftar, dan 50% telah lulus.

## Menjalankan Sistem Machine Learning
- Aktifkan environment

```
conda activate students_performance
```

- Mengatur path ke file app.py

```
cd path/to/app.py
```

- Run streamlit di lokal

```
streamlit run app.py
```

## Conclusion
Proyek ini berfokus pada analisis faktor-faktor yang memengaruhi dropout siswa di institusi pendidikan. Melalui pengumpulan dan analisis data siswa yang mencakup informasi demografi, latar belakang keluarga, dan performa akademik, proyek ini memberikan wawasan mendalam tentang tren dan pola yang berkaitan dengan kelulusan dan dropout. Di bawah ini merupakan kesimpulan dari keseluruhan proyek ini:

- Siswa yang belum menikah (single) menunjukkan angka dropout yang paling tinggi, jauh melampaui siswa dengan status perkawinan lainnya. Ini menunjukkan bahwa status sosial dan dukungan personal dapat berperan dalam retensi siswa di institusi.
- Siswa dengan orang tua yang bekerja di sektor Manual Labor cenderung memiliki angka dropout lebih tinggi. Hal ini menunjukkan bahwa latar belakang ekonomi dan sosial keluarga berpotensi mempengaruhi keberhasilan akademik siswa. Sebaliknya, siswa dengan orang tua yang bekerja sebagai profesional atau berpendidikan tinggi cenderung memiliki angka dropout yang lebih rendah.
- Siswa yang memiliki nilai Admission Grade dan Total Units Grade yang rendah cenderung lebih mungkin dropout. Ini mengindikasikan bahwa siswa yang kurang berprestasi secara akademis sejak awal berisiko lebih besar untuk tidak menyelesaikan studi mereka. Nilai akademik merupakan salah satu indikator yang penting untuk mengidentifikasi siswa yang memerlukan intervensi tambahan.
- Siswa yang menerima beasiswa cenderung lebih sedikit dropout dibandingkan dengan yang tidak menerima beasiswa. Ini menunjukkan bahwa dukungan finansial dapat menjadi faktor penting dalam membantu siswa menyelesaikan studi mereka.
- Sistem machine learning yang telah dibuat menggunakan 3 algoritma yaitu decision tree, random forest, dan gradien boosting, belum ada model yang memiliki performa yang sangat baik. Namun, tetap diambil algoritma yang memiliki nilai accuracy yang paling tinggi yaitu random forest.

### Rekomendasi Action Items
- Membuat program dukungan sosial atau komunitas untuk siswa dengan status single atau tanpa dukungan keluarga yang signifikan. Program ini dapat berupa konseling, bimbingan, atau kelompok dukungan yang membantu mereka mengatasi tantangan pribadi.
- Mengimplementasikan sistem untuk memantau nilai akademik siswa secara berkelanjutan. Siswa dengan nilai Admission Grade atau Total Units Grade yang rendah bisa mendapatkan peringatan dini dan bimbingan akademik tambahan untuk membantu mereka memperbaiki kinerja mereka.
- Karena penerima beasiswa cenderung memiliki tingkat dropout lebih rendah, perluas cakupan program beasiswa untuk siswa dari keluarga berpenghasilan rendah. Hal ini dapat membantu meringankan beban finansial dan meningkatkan motivasi siswa untuk menyelesaikan studi mereka.
- Banyak siswa yang berasal dari keluarga dengan orang tua berpendidikan rendah atau bekerja di sektor Manual Labor mungkin kurang mendapatkan arahan karir yang tepat. Sediakan layanan bimbingan karir bagi siswa dan juga orang tua, untuk membantu mereka memahami potensi akademik dan peluang karir siswa.
