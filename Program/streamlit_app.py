# streamlit_app.py

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Healthcare AI - Prediksi Risiko Diabetes",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling for healthcare & AI feel
st.markdown("""
    <style>
        body {
            background-color: #f0fdf4;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }
        .stButton > button {
            background-color: #38b6ff;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 1em;
        }
        .stButton > button:hover {
            background-color: #2a9fd6;
        }
        h2, h3 {
            color: #38b6ff;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center;'>
        <h2>🤖 Healthcare AI System</h2>
        <p style='color: grey;'>Sistem Cerdas Prediksi Risiko Diabetes</p>
    </div>
    <hr style='border: 1px solid #e0e0e0;' />
""", unsafe_allow_html=True)

# Form input
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.subheader("📋 Form Pemeriksaan Pasien")
umur = st.number_input("Umur (tahun)", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, value=22.5, format="%.2f")
glukosa = st.number_input("Kadar Glukosa (mg/dL)", min_value=50, max_value=300, value=110)

if st.button("🔍 Prediksi Risiko dengan AI"):
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

    st.info("Hasil prediksi ini ditenagai oleh sistem AI berbasis aturan dan data medis.")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style='border: 1px solid #e0e0e0;'>
    <p style='text-align: center; font-size: 0.8rem; color: grey;'>
        &copy; 2025 Healthcare AI System | UAS Data Mining
    </p>
""", unsafe_allow_html=True)
