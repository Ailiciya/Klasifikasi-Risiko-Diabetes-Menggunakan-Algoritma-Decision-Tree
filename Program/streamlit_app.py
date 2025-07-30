# streamlit_app.py

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Prediksi Risiko Diabetes",
    layout="centered"
)

st.markdown("""
    <style>
        body {
            background-color: #f4fdf8;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        }
        .stButton > button {
            background-color: #00b894;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 1em;
        }
        .stButton > button:hover {
            background-color: #019875;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("**📅 Tanggal:**")
    st.write(datetime.today().strftime("%d %B %Y"))
    st.markdown("**👨‍⚕️ Dibuat oleh:**")
    st.write("Mahasiswa Proyek Data Mining")

st.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #00b894;'>🩺 Sistem Prediksi Risiko Diabetes</h2>
        <p style='color: grey;'>RS Digital Sehat • Ujian Akhir Semester</p>
    </div>
""", unsafe_allow_html=True)


st.subheader("📋 Form Pemeriksaan Pasien")
umur = st.number_input("Umur (tahun)", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, value=22.5, format="%.2f")
glukosa = st.number_input("Kadar Glukosa (mg/dL)", min_value=50, max_value=300, value=110)

if st.button("🔍 Prediksi Risiko"):
    if glukosa > 125:
        hasil = "Risiko Tinggi Diabetes"
        warna = "#d63031"
        ikon = "🚨"
    elif bmi > 30 and umur > 45:
        hasil = "Risiko Sedang Diabetes"
        warna = "#fdcb6e"
        ikon = "⚠️"
    else:
        hasil = "Risiko Rendah Diabetes"
        warna = "#00b894"
        ikon = "✅"

    st.markdown(f"""
        <div style='background-color: {warna}; padding: 1.2rem; border-radius: 12px; text-align: center; color: white;'>
            <h3 style='margin:0;'>{ikon} {hasil}</h3>
        </div>
    """, unsafe_allow_html=True)

    st.success("Analisis selesai. Gunakan hasil ini sebagai referensi awal, bukan diagnosis pasti.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <hr style='border: 1px solid #e0e0e0;'>
    <p style='text-align: center; font-size: 0.8rem; color: grey;'>
        &copy; 2025 RS Digital Sehat | Sistem Prediksi Diabetes
    </p>
""", unsafe_allow_html=True)
