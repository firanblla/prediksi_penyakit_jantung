import pickle
import streamlit as st
import numpy as np

# Membaca model
try:
    Jantung_model = pickle.load(open('Jantung_model.sav', 'rb'))
except FileNotFoundError:
    st.error("File model tidak ditemukan. Pastikan path file sudah benar.")
    st.stop()

# Judul web
st.title('Data Mining Prediksi Jantung')

# Membagi kolom untuk input
col1, col2 = st.columns(2)

with col1:
    try:
        age = float(st.text_input('Input Usia (age)', value='0'))
    except ValueError:
        st.error("Usia harus berupa angka.")
        age = 0.0

with col2:
    try:
        sex = int(st.text_input('Jenis Kelamin (1: Laki-laki, 0: Perempuan)', value='0'))
    except ValueError:
        st.error("Jenis kelamin harus berupa 0 atau 1.")
        sex = 0

with col1:
    try:
        cigPDay = float(st.text_input('Rata-rata Rokok per Hari (CigPDay)', value='0'))
    except ValueError:
        st.error("Input rokok per hari harus berupa angka.")
        cigPDay = 0.0

with col2:
    try:
        totChol = float(st.text_input('Total Kolesterol (TotChol)', value='0'))
    except ValueError:
        st.error("Total kolesterol harus berupa angka.")
        totChol = 0.0

with col1:
    try:
        BPMeds = int(st.text_input('Penggunaan Obat Tekanan Darah (BPMeds)', value='0'))
    except ValueError:
        st.error("Input harus berupa 0 atau 1.")
        BPMeds = 0

with col2:
    try:
        sysBP = float(st.text_input('Tekanan Darah Sistolik (SysBP)', value='0'))
    except ValueError:
        st.error("Tekanan darah sistolik harus berupa angka.")
        sysBP = 0.0

with col1:
    try:
        prevHyp = int(st.text_input('Riwayat Hipertensi (PrevHyp)', value='0'))
    except ValueError:
        st.error("Riwayat hipertensi harus berupa 0 atau 1.")
        prevHyp = 0

with col2:
    try:
        glucose = float(st.text_input('Kadar Glukosa (Glucose)', value='0'))
    except ValueError:
        st.error("Kadar glukosa harus berupa angka.")
        glucose = 0.0

# Code untuk prediksi
jantung_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Jantung'):
    try:
        # Input fitur aktual
        input_data = [age, sex, cigPDay, totChol, BPMeds, sysBP, prevHyp, glucose]
        
        # Tambahkan dummy features untuk melengkapi 39 fitur
        while len(input_data) < 39:
            input_data.append(0)  # Anda bisa mengganti 0 dengan nilai rata-rata jika diperlukan

        # Konversi ke array 2D
        input_data = np.array(input_data).reshape(1, -1)

        # Prediksi
        jantung_prediction = Jantung_model.predict(input_data)

        if jantung_prediction[0] == 0:
            jantung_diagnosis = 'Pasien tidak terkena penyakit jantung.'
        else:
            jantung_diagnosis = 'Pasien terkena penyakit jantung.'
        
        st.success(jantung_diagnosis)
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
