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

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
