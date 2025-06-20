import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Log Makan Harian", layout="centered")
st.title("🍽️ Log Makan Harian Nurrish")

# --- Input ---
nasi = st.selectbox("Nasi", ["Half", "Full"])
daging = st.number_input("Daging (gram)", min_value=0.0, step=10.0)
ayam = st.number_input("Ayam (gram)", min_value=0.0, step=10.0)
ikan = st.number_input("Ikan (gram)", min_value=0.0, step=10.0)
telur = st.number_input("Telur (biji)", min_value=0, step=1)
sayur = st.selectbox("Sayur/Sambal", ["Yes", "No"])

# --- Kiraan ---
nasi_kcal, nasi_prot = (100, 2) if nasi == "Half" else (200, 4)
daging_kcal, daging_prot = daging * 2.5, daging * 0.22
ayam_kcal, ayam_prot = ayam * 2.2, ayam * 0.20
ikan_kcal, ikan_prot = ikan * 2.0, ikan * 0.22
telur_kcal, telur_prot = telur * 90, telur * 6
sayur_kcal, sayur_prot = (30, 1) if sayur == "Yes" else (0, 0)

total_kcal = nasi_kcal + daging_kcal + ayam_kcal + ikan_kcal + telur_kcal + sayur_kcal
total_prot = nasi_prot + daging_prot + ayam_prot + ikan_prot + telur_prot + sayur_prot

# --- Output ---
if st.button("💾 Simpan Log"):
    log = {
        "Tarikh": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Kalori (kcal)": round(total_kcal),
        "Protein (g)": round(total_prot, 1),
        "Nasi": nasi,
        "Daging (g)": daging,
        "Ayam (g)": ayam,
        "Ikan (g)": ikan,
        "Telur (biji)": telur,
        "Sayur/Sambal": sayur
        
    }

    try:
        df = pd.read_csv("log_makan.csv")
        df = pd.concat([df, pd.DataFrame([log])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([log])

    df.to_csv("log_makan.csv", index=False)
    st.success("✅ Log berjaya disimpan!")
    st.write(log)

# --- Show log terkini ---
if st.checkbox("📋 Tunjuk Log Terkini"):
    try:
        df = pd.read_csv("log_makan.csv")
        st.dataframe(df.tail(5))
    except FileNotFoundError:
        st.info("Tiada log lagi.")
