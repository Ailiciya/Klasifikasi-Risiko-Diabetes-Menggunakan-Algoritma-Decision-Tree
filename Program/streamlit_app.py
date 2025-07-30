# streamlit_app.py

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Sistem Prediksi Risiko Diabetes",
    page_icon="🩺",
    layout="centered",
)

# Header
st.markdown("""
    <h2 style='text-align: center; color: #1a73e8;'>🩺 Sistem Prediksi Risiko Diabetes</h2>
    <p style='text-align: center; color: grey;'>Versi Beta | RS Sehat Selalu</p>
    <hr style='border: 1px solid #ddd;' />
""", unsafe_allow_html=True)

# Sidebar Info
with st.sidebar:
    st.markdown("**📅 Tanggal:**")
    st.write(datetime.today().strftime("25 07 2025"))
    st.markdown("**👨‍⚕️ Dibuat oleh:**")
    st.write("Kevin Rizki Irawan")

# Form input data
st.subheader("📋 Masukkan Data Pemeriksaan")
umur = st.number_input("Umur (tahun)", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, value=22.5, format="%.2f")
glukosa = st.number_input("Kadar Glukosa (mg/dL)", min_value=50, max_value=300, value=110)

# Tombol prediksi
if st.button("🔍 Prediksi Risiko"):
    if glukosa > 125:
        hasil = "Risiko Tinggi Diabetes"
        warna = "#d9534f"
        ikon = "🚨"
    elif bmi > 30 and umur > 45:
        hasil = "Risiko Sedang Diabetes"
        warna = "#f0ad4e"
        ikon = "⚠️"
    else:
        hasil = "Risiko Rendah Diabetes"
        warna = "#5cb85c"
        ikon = "✅"

    st.markdown(f"""
        <div style='background-color: {warna}; padding: 1.2rem; border-radius: 12px; text-align: center; color: white;'>
            <h3 style='margin:0;'>{ikon} {hasil}</h3>
        </div>
    """, unsafe_allow_html=True)

    st.success("Analisis selesai. Gunakan hasil ini sebagai referensi awal, bukan diagnosis pasti.")

# Footer
st.markdown("""
    <hr style='border: 1px solid #eee;'>
    <p style='text-align: center; font-size: 0.8rem; color: grey;'>
        &copy; 2025 Sistem Prediksi Diabetes | Ujian Akhir Semester Proyek Data Mining
    </p>
""", unsafe_allow_html=True)
