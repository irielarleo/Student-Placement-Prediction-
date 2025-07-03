# Milestone Project 2

## Repository Outline
1. description.md - Penjelasan gambaran umum project.
2. P1M2_Iriel_Aureleo.ipynb - Notebook yang berisi pengolahan data dengan python.
3. P1M2_Iriel_Aureleo_inf.ipynb - Notebook berisi hasil prediksi data inference.
4. P1M2_Iriel_Aureleo_conceptual - file berisi jawaban dari conceptual problem .
5. placementdata.csv - Dataset yang digunakan pada program pengolahan data.
6. deployment - folder berisi file yang digunakan untuk deployment ke website huggingface.com
    - app.py - File python yang menjadi main page dari webpage.
    - eda.py - File python yang berisikan hasil analisis eda yang dilakukan dalam sebuah webpage.
    - prediction.py - File python yang berupa form untuk memasukan data baru untuk prediksi apakah mahasiswa diprediksi akan berhasil mendapat pekerjaan atau tidak berhasil mendapat pekerjaan.
    - bestmodel.pkl - File ini menyimpan hasil model terbagus yaitu model Gradient Boosting Classifier yang telah dilakukan Hyperparameter Tuning.
    - requirements.txt - File yang berisikan semua library yang digunakan pada folder deployment.

## Problem Background
Dalam upaya meningkatkan permasalahan rendahnya tingkat penempatan kerja lulusan dan belum optimalnya alokasi program pengembangan karier, proyek ini menawarkan solusi berupa dashboard prediksi employability yang mampu mengidentifikasi mahasiswa dengan risiko tidak mendapatkan pekerjaan. Dengan alat ini, kampus dan Career Center dapat melakukan intervensi lebih awal secara tepat sasaran serta mengevaluasi efektivitas program pelatihan dan pengembangan soft skill secara berbasis data, guna merumuskan strategi peningkatan daya saing lulusan secara lebih terukur.


## Project Output
Output project ini adalah sebuah model prediksi yang dapat melakukan prediksi apakah student akan berpotensi mendapatkan pekerjaan atau tidak yang akan di deploy menggunakan huggingface.co

## Data
Dataset ini berasal dari keggle dengan detail sebegai berikut :

1. Columns and Their Significance:
- StudentID: Serves as a unique identifier for tracking individual students, important for merging or referencing data.
- CGPA: A crucial metric reflecting academic performance; higher CGPA typically correlates with better placement chances.
- Internships: Practical experience often enhances employability; the number of internships may indicate a student's commitment to gaining real-world experience.
- Projects: Involvement in projects demonstrates practical skills and application of knowledge, which are attractive to employers.
- Workshops/Certifications: Additional qualifications can differentiate students in competitive job markets.
- AptitudeTestScore: Standardized scores often used by employers to gauge problem-solving and analytical skills.
- SoftSkillsRating: Soft skills are increasingly valued by employers; this rating can help predict a student's interpersonal effectiveness.
- ExtracurricularActivities: Participation can indicate a well-rounded candidate; students engaged in extracurriculars may show leadership and teamwork abilities.
- PlacementTraining: Indicates whether students received specific training to enhance their employability.
- SSC_Marks: Secondary education marks that may impact initial job opportunities or perceptions by employers.
- HSC_Marks: Higher secondary education marks that can also influence placement status.
- PlacementStatus: The target variable for prediction, showing whether a student was successfully placed after graduation.

2. Data Characteristics:
- The dataset consists of 10,000 entries, making it a substantial size for analysis.
- Each entry includes 12 fields, which provide a mix of categorical and numerical data.

## Method

Metode yang digunakan adalah **supervised learning untuk klasifikasi**, dengan beberapa algoritma sebagai baseline model: **K-Nearest Neighbors, Support Vector Classifier, Decision Tree, Random Forest**, dan **Gradient Boosting Classifier**. Evaluasi dilakukan dengan **cross-validation (ROC-AUC)**, **classification report dengan fokus pada recall**, serta **ROC-AUC score dan visualisasinya**. Model terbaik dipilih berdasarkan performa dan sensitivitas terhadap kelas risiko (`NotPlaced`), dan dilakukan **hyperparameter tuning** untuk mengoptimalkan hasil akhir.

## Stacks
- **Bahasa Pemrograman**: Python
- **Tools**: Jupyter Notebook, Streamlit, Hugging Face Spaces
- **Library Python**:
  - `pandas`, `numpy`, `matplotlib`, `seaborn` – untuk eksplorasi dan visualisasi data
  - `scikit-learn` – untuk preprocessing, modeling, evaluasi, dan tuning
  - `joblib` – untuk model serialization
  - `streamlit` – untuk deployment model dalam bentuk aplikasi interaktif

## Reference

- ### Dataset :
    [Dataset]( https://www.kaggle.com/datasets/ruchikakumbhar/placement-prediction-dataset)

- ### Referensi:
    - [Tingkat Pengangguran Lulusan Perguruan Tinggi Masih Tinggi](https://www.detik.com/edu/detikpedia/d-7902527/daftar-lulusan-dengan-tingkat-pengangguran-tertinggi-menurut-data-bps-2025-smk-s1?utm_source=chatgpt.com)
    - [Peningkatan Proporsi Pengangguran dari Lulusan Pendidikan Tinggi](https://ntbsatu.com/2025/05/09/krisis-tenaga-kerja-terdidik-awal-tahun-2025-pengangguran-sarjana-di-indonesia-melonjak.html?utm_source=chatgpt.com)
    - [Pentingnya Perencanaan Karier Bagi Mahasiswa](https://careercenter.unesa.ac.id/page/pentingnya-perencanaan-karier-bagi-mahasiswa)

- ### Deployment
    [Link Deployment](https://huggingface.co/spaces/irel/Milestone_2)

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
