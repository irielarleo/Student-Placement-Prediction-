import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run():
    '''Membuat tampilan yang menampilkan grafik hasil Exploratory Data Analysis'''
    
    # Menambahkan tampilan title
    st.title('Placement Prediction Dataset')

    # Load data
    st.header('Data Loading')
    df = pd.read_csv(r"C:\Users\USER\Documents\Hacktiv8\Repeat P1\Milestone\p1-ftds027-hck-m2-irielarleo\placementdata.csv")
    st.write('Link dataset: https://www.kaggle.com/datasets/ruchikakumbhar/placement-prediction-dataset')
    st.dataframe(df)
    st.write('---')

    st.write('---')
    st.header("📌 Pertanyaan & Analisis EDA")

    # ====== Pertanyaan 1 ======
    st.markdown("### Apakah mahasiswa dengan **CGPA tinggi** lebih cenderung mendapatkan kerja?")
    with st.expander("Lihat analisis lengkap"):
        st.write("Distribusi CGPA berdasarkan status penempatan kerja:")
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        sns.boxplot(x='PlacementStatus', y='CGPA', data=df, ax=ax1)
        ax1.set_title("Distribusi CGPA berdasarkan Placement Status")
        ax1.set_xlabel("Placement Status")
        ax1.set_ylabel("CGPA")
        st.pyplot(fig1)

        cgpa_means = df.groupby('PlacementStatus')['CGPA'].mean().reset_index()
        cgpa_means.columns = ['PlacementStatus', 'Rata-rata CGPA']
        st.dataframe(cgpa_means)

        st.markdown("### 🔍 Insight:")
        st.write("""
        Mahasiswa dengan nilai akademik tinggi memiliki peluang kerja yang lebih besar. Rata-rata CGPA mahasiswa yang *Placed* adalah **8.02**, 
        sedangkan *NotPlaced* adalah **7.47**. Sebaran nilainya juga lebih stabil dan terkonsentrasi di nilai tinggi.

        Kampus dapat menggunakan insight ini untuk menyusun strategi penguatan akademik sebagai bagian dari program peningkatan *employability*.
        """)

    # ====== Pertanyaan 2 ======
    st.markdown("### Bagaimana perbandingan **PlacementStatus** antara mahasiswa yang mengikuti dan tidak mengikuti pelatihan?")
    with st.expander("Lihat analisis lengkap"):
        st.write("Visualisasi perbandingan status penempatan kerja berdasarkan keikutsertaan pelatihan:")
        placement_counts = df.groupby(['PlacementTraining', 'PlacementStatus']).size().reset_index(name='count')
        fig2 = px.bar(
            placement_counts,
            x='PlacementTraining',
            y='count',
            color='PlacementStatus',
            barmode='group',
            labels={'PlacementTraining': 'Placement Training', 'count': 'Jumlah Mahasiswa', 'PlacementStatus': 'Status Penempatan'},
            title='Perbandingan Status Penempatan Berdasarkan Placement Training'
        )
        st.plotly_chart(fig2, use_container_width=True)

        training_impact = df.groupby('PlacementTraining')['PlacementStatus'].value_counts(normalize=True).unstack()
        training_impact.columns = ['Not Placed (%)', 'Placed (%)']
        training_impact *= 100
        training_impact.reset_index(inplace=True)

        st.write("Proporsi mahasiswa yang berhasil ditempatkan berdasarkan pelatihan:")
        st.dataframe(training_impact)

        st.markdown("### 🔍 Insight:")
        st.write("""
        - **Tanpa pelatihan**: hanya sekitar **15.6%** yang berhasil mendapat pekerjaan  
        - **Dengan pelatihan**: sekitar **51.6%** berhasil mendapat pekerjaan

        Ini menunjukkan `PlacementTraining` berpotensi besar mendukung keberhasilan penempatan kerja. 
        Kampus bisa menjadikan pelatihan ini sebagai program wajib atau memperluas jangkauannya.
        """)
    
    # ====== Pertanyaan 3 ======
    st.markdown("### Apakah keikutsertaan dalam **kegiatan ekstrakurikuler** berpengaruh terhadap peluang kerja?")
    with st.expander("Lihat analisis lengkap"):
        st.write("Visualisasi perbandingan status penempatan kerja berdasarkan keaktifan ekstrakurikuler:")

        # Visualisasi interaktif dengan plotly
        ekskul_counts = df.groupby(['ExtracurricularActivities', 'PlacementStatus']).size().reset_index(name='count')
        fig3 = px.bar(
            ekskul_counts,
            x='ExtracurricularActivities',
            y='count',
            color='PlacementStatus',
            barmode='group',
            labels={
                'ExtracurricularActivities': 'Aktif Ekstrakurikuler',
                'count': 'Jumlah Mahasiswa',
                'PlacementStatus': 'Status Penempatan'
            },
            title='Perbandingan Status Penempatan Berdasarkan Keaktifan Ekstrakurikuler'
        )
        st.plotly_chart(fig3, use_container_width=True)

        # Proporsi yang placed berdasarkan keaktifan ekstrakurikuler
        ekskul_impact = df.groupby('ExtracurricularActivities')['PlacementStatus'].value_counts(normalize=True).unstack()
        ekskul_impact.columns = ['Not Placed (%)', 'Placed (%)']
        ekskul_impact *= 100
        ekskul_impact.reset_index(inplace=True)

        st.write("Proporsi mahasiswa yang berhasil ditempatkan berdasarkan keaktifan ekstrakurikuler:")
        st.dataframe(ekskul_impact)

        st.markdown("### 🔍 Insight:")
        st.write("""
        - **Tidak aktif**: hanya sekitar **13.7%** yang berhasil mendapat pekerjaan  
        - **Aktif**: sekitar **62.0%** berhasil mendapat pekerjaan

        Keaktifan dalam kegiatan kampus (organisasi, kepanitiaan, dll) tampaknya meningkatkan peluang kerja karena mendorong 
        keterampilan interpersonal, kepemimpinan, dan kerja tim.

        Kampus sebaiknya mendorong mahasiswa lebih aktif, misalnya melalui insentif beasiswa, pelatihan, atau memasukkan kegiatan ini 
        ke dalam SKPI. Ini bisa menjadi bagian strategis dari pembelajaran yang mendukung kesiapan kerja lulusan.
        """)

    # ====== Pertanyaan 4 ======
    st.markdown("### Seberapa besar risiko tidak mendapatkan pekerjaan bagi mahasiswa yang **tidak ikut pelatihan** dan **tidak aktif ekstrakurikuler**?")
    with st.expander("Lihat analisis lengkap"):
        st.write("Visualisasi berikut menunjukkan pengaruh kombinasi pelatihan dan aktivitas ekstrakurikuler terhadap status penempatan kerja:")

        # Crosstab kombinasi Training dan Ekstrakurikuler
        cross_tab = pd.crosstab(
            index=[df['PlacementTraining'], df['ExtracurricularActivities']],
            columns=df['PlacementStatus'],
            normalize='index'
        ) * 100

        cross_tab_reset = cross_tab.reset_index()
        cross_tab_reset['Kombinasi'] = cross_tab_reset['PlacementTraining'] + ' & ' + cross_tab_reset['ExtracurricularActivities']
        cross_tab_reset['Placed'] = cross_tab_reset['Placed'].round(2)
        # Gunakan plotly untuk visualisasi interaktif
        fig4 = px.bar(
            cross_tab_reset.sort_values('Kombinasi'),
            x='Kombinasi',
            y='Placed',
            title='Persentase Mahasiswa yang Ditempatkan Berdasarkan Kombinasi Training & Ekstrakurikuler',
            labels={'Placed': 'Persentase Ditempatkan (%)'},
            category_orders={'Kombinasi': ['No & No', 'No & Yes', 'Yes & No', 'Yes & Yes']},
            text='Placed'
        )
        fig4.update_layout(yaxis_range=[0, 100])
        st.plotly_chart(fig4, use_container_width=True)

        st.write("Tabel proporsi lengkap:")
        st.dataframe(cross_tab_reset)

        st.markdown("### 🔍 Insight:")
        st.write("""
        Mahasiswa yang **tidak mengikuti pelatihan** dan **tidak aktif dalam kegiatan ekstrakurikuler** berada dalam **kategori risiko tertinggi**:  
        hanya sekitar **6%** dari mereka yang berhasil mendapatkan pekerjaan, sedangkan **94% sisanya belum berhasil**.

        Sebaliknya, mahasiswa yang aktif di **keduanya** memiliki peluang terbaik dengan tingkat penempatan lebih dari **66%**.

        Kombinasi ketidakaktifan di dua aspek penting—akademik (pelatihan) dan non-akademik (kegiatan kampus)—dapat dijadikan indikator **risiko tinggi ketenagakerjaan**.

        🎯 **Rekomendasi Strategis untuk Kampus:**
        - Identifikasi mahasiswa kategori "No & No" sejak dini melalui sistem akademik
        - Prioritaskan mereka dalam program pembinaan intensif, seperti mentoring dan pelatihan wajib
        - Wajibkan minimal 1 partisipasi dalam kegiatan organisasi/non-akademik sebagai syarat SKPI
        - Sediakan bimbingan karier yang dirancang khusus untuk kelompok risiko tinggi ini

        Dengan pendekatan ini, kampus tidak hanya membantu meningkatkan daya saing lulusan secara umum, tetapi juga **mencegah risiko kegagalan penempatan** pada kelompok yang paling rentan.
        """)

        # ====== Pertanyaan 5 ======
    st.markdown("### Bagaimana perbandingan status penempatan kerja berdasarkan jumlah **internship** dan **project**?")
    with st.expander("Lihat analisis lengkap"):
        st.write("Visualisasi berikut menunjukkan pengaruh jumlah pengalaman praktikal (magang dan proyek) terhadap peluang kerja:")

        # Dua grafik interaktif side-by-side
        col1, col2 = st.columns(2)

        # Grafik Internships
        with col1:
            fig5a = px.histogram(
                df,
                x='Internships',
                color='PlacementStatus',
                barmode='group',
                text_auto=True,
                labels={'Internships': 'Jumlah Internship', 'PlacementStatus': 'Status Penempatan'},
                title='Status Penempatan vs Jumlah Internship'
            )
            fig5a.update_layout(yaxis_title='Jumlah Mahasiswa')
            st.plotly_chart(fig5a, use_container_width=True)

        # Grafik Projects
        with col2:
            fig5b = px.histogram(
                df,
                x='Projects',
                color='PlacementStatus',
                barmode='group',
                text_auto=True,
                labels={'Projects': 'Jumlah Project', 'PlacementStatus': 'Status Penempatan'},
                title='Status Penempatan vs Jumlah Project'
            )
            fig5b.update_layout(yaxis_title='Jumlah Mahasiswa')
            st.plotly_chart(fig5b, use_container_width=True)

        st.markdown("### 🔍 Insight:")
        st.write("""
        Mahasiswa dengan **lebih banyak internship dan project** menunjukkan **peluang kerja yang lebih tinggi**.

        - Untuk internship: mahasiswa dengan **2 kali magang** memiliki jumlah yang ditempatkan kerja lebih tinggi dibandingkan 0 atau 1.
        - Untuk project: mahasiswa dengan **3 proyek** lebih banyak yang berhasil ditempatkan kerja dibandingkan yang hanya memiliki 1 atau 2.

        📌 **Kesimpulan**:  
        **Pengalaman praktikal** memiliki pengaruh nyata terhadap keberhasilan penempatan kerja.

        🎯 **Rekomendasi untuk Kampus**:
        - Perluasan kemitraan industri untuk menyediakan lebih banyak slot magang
        - Integrasi proyek berbasis dunia nyata ke dalam kurikulum
        - Penilaian akademik yang mengapresiasi pengalaman aplikatif

        Dengan membekali mahasiswa melalui pengalaman praktis, lulusan akan lebih siap secara kompetensi dan bersaing di pasar kerja.
        """)

    # ====== Pertanyaan 6 ======
    st.markdown("### Apa ciri umum mahasiswa yang **tidak mendapatkan pekerjaan**? (Profil Risiko Tinggi)")
    with st.expander("Lihat analisis lengkap"):
        st.write("Distribusi lima fitur utama yang digunakan untuk membedakan mahasiswa *Placed* dan *Not Placed*:")

        fitur_penting = ['CGPA', 'AptitudeTestScore', 'SoftSkillsRating', 'Internships', 'Projects']

        # Buat subplot KDE
        fig6, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()

        for i, col in enumerate(fitur_penting):
            sns.kdeplot(
                data=df,
                x=col,
                hue='PlacementStatus',
                fill=True,
                common_norm=False,
                alpha=0.5,
                ax=axes[i]
            )
            axes[i].set_title(f'Distribusi {col}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Density')
            axes[i].grid(True)

        # Kosongkan subplot ke-6 jika tidak dipakai
        if len(fitur_penting) < 6:
            fig6.delaxes(axes[-1])

        plt.tight_layout()
        st.pyplot(fig6)

        st.markdown("### 🔍 Insight:")
        st.write("""
        Untuk menganalisis **profil risiko tinggi** mahasiswa yang tidak mendapatkan pekerjaan, digunakan lima fitur utama:
        - `CGPA`
        - `AptitudeTestScore`
        - `SoftSkillsRating`
        - `Internships`
        - `Projects`

        📊 **Pola distribusi menunjukkan:**
        - Mahasiswa *Not Placed* cenderung memiliki:
            - CGPA di bawah **8.0**
            - Skor aptitude di bawah **80**
            - Rating soft skill lebih rendah
            - Pengalaman internship dan proyek yang terbatas

        ✅ Ini menunjukkan bahwa **kegagalan penempatan** bukan karena satu faktor tunggal, tapi **gabungan berbagai aspek kesiapan kerja**.

        🎯 **Rekomendasi Strategis untuk Kampus:**
        - Identifikasi mahasiswa dengan kombinasi skor rendah pada fitur-fitur ini
        - Fokuskan program peningkatan keterampilan (soft skill, project coaching, pelatihan interview)
        - Berikan **pendampingan khusus** bagi mahasiswa berisiko tinggi secara sistematis

        Dengan pendekatan berbasis data ini, kampus dapat meningkatkan *employability* secara lebih **terarah, akurat, dan berdampak**.
        """)

    # ====== Pertanyaan 7 ======
    st.markdown("### Apakah terdapat ambang nilai pada **CGPA**, *Soft Skill*, atau *Aptitude Score* yang meningkatkan peluang kerja?")
    with st.expander("Lihat analisis lengkap"):
        st.write("""
        Analisis berikut melihat proporsi mahasiswa yang berhasil ditempatkan kerja berdasarkan rentang nilai tertentu pada fitur `CGPA`, `AptitudeTestScore`, dan `SoftSkillsRating`.  
        Ambang 50% digunakan sebagai batas peluang yang dianggap signifikan.
        """)

        threshold_bins = {
            'CGPA': [0, 7, 8, 9, 10],
            'SoftSkillsRating': [3.0, 3.5, 4.0, 4.5, 5.0],
            'AptitudeTestScore': [0, 70, 80, 85, 90, 100]
        }

        fig7, axes = plt.subplots(1, 3, figsize=(15, 4))

        for i, (feature, bins) in enumerate(threshold_bins.items()):
            binned = pd.cut(df[feature], bins=bins)
            proporsi = (
                df.groupby(binned)['PlacementStatus']
                .value_counts(normalize=True)
                .unstack()
                .fillna(0)
            )

            proporsi['Placed'].plot(
                kind='bar',
                color='skyblue',
                edgecolor='black',
                ax=axes[i]
            )
            axes[i].set_title(f'Proporsi Placed vs {feature}')
            axes[i].set_xlabel(f'{feature}')
            axes[i].set_ylabel('Proporsi Ditempatkan')
            axes[i].set_ylim(0, 1)
            axes[i].axhline(0.5, color='red', linestyle='--', label='Ambang 50%')
            axes[i].legend()

        plt.tight_layout()
        st.pyplot(fig7)

        st.markdown("### 🔍 Insight:")
        st.write("""
        Analisis proporsi menunjukkan bahwa peluang mendapatkan pekerjaan meningkat signifikan jika mahasiswa mencapai:
        - `CGPA` **> 8.0**
        - `AptitudeTestScore` **> 85**
        - `SoftSkillsRating` **> 4.5**

        📌 **Kesimpulan**:  
        Tiga fitur ini mewakili **kemampuan akademik**, **kognitif**, dan **interpersonal**. Nilai ambang tersebut dapat digunakan sebagai **indikator kesiapan kerja**.

        🎯 **Rekomendasi Strategis untuk Kampus**:
        - Identifikasi mahasiswa dengan nilai **di bawah ambang**
        - Sediakan pelatihan dan dukungan: akademik, simulasi tes, pengembangan soft skill
        - Gunakan ambang ini sebagai dasar intervensi dan pemantauan risiko employability

        Dengan pendekatan ini, institusi dapat menyusun **program pembinaan yang lebih fokus, terukur, dan berdampak langsung** terhadap peningkatan kesiapan kerja lulusan.
        """)
    st.write("---")

        # ====== Ringkasan Insight EDA ======
    st.write("---")
    st.subheader("📈 Ringkasan Insight Setelah EDA")

    st.markdown("""
    Berikut adalah beberapa insight utama yang dapat diambil setelah proses eksplorasi data (EDA):

    - Mahasiswa dengan **CGPA tinggi** memiliki peluang kerja yang jauh lebih besar.
    - **Keikutsertaan dalam pelatihan kerja** (*Placement Training*) secara nyata meningkatkan kemungkinan mendapatkan pekerjaan.
    - Mahasiswa yang **aktif dalam kegiatan ekstrakurikuler** menunjukkan peluang kerja yang lebih tinggi daripada yang tidak aktif.
    - Kombinasi **tidak ikut pelatihan** dan **tidak aktif kegiatan kampus** merupakan **profil risiko tertinggi** (hanya ~6% yang mendapat pekerjaan).
    - Pengalaman praktikal seperti **magang (internship)** dan **proyek (project)** sangat berpengaruh terhadap keberhasilan penempatan kerja.
    - Mahasiswa yang **tidak ditempatkan** umumnya memiliki skor lebih rendah pada kombinasi fitur: *CGPA*, *AptitudeTestScore*, *SoftSkills*, dan pengalaman praktikal.
    - Terdapat **ambang kritis** yang dapat digunakan sebagai indikator kesiapan kerja:
        - `CGPA` > 8.0
        - `AptitudeTestScore` > 85
        - `SoftSkillsRating` > 4.5

    📌 **Kesimpulan umum:**  
    Proses EDA berhasil mengungkap pola-pola penting yang dapat digunakan untuk **pemodelan prediktif**, **perencanaan intervensi kampus**, dan **peningkatan employability lulusan** secara lebih **berbasis data** dan **terarah**.
    """)
if __name__== '__main__':
    run()
