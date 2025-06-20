Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import datetime

def kira_kalori_protein(nasi, daging, ayam, ikan, telur, sayur):
    # Nasi
    if nasi.lower() == "half":
        nasi_kcal, nasi_prot = 100, 2
    else:
        nasi_kcal, nasi_prot = 200, 4

    # Daging
    daging_kcal = daging * 2.5
    daging_prot = daging * 0.22

    # Ayam
    ayam_kcal = ayam * 2.2
    ayam_prot = ayam * 0.20

    # Ikan
    ikan_kcal = ikan * 2.0
    ikan_prot = ikan * 0.22

    # Telur
    telur_kcal = telur * 90
    telur_prot = telur * 6

    # Sayur/Sambal
    if sayur.lower() == "yes":
        sayur_kcal, sayur_prot = 30, 1
...     else:
...         sayur_kcal, sayur_prot = 0, 0
... 
...     total_kcal = sum([nasi_kcal, daging_kcal, ayam_kcal, ikan_kcal, telur_kcal, sayur_kcal])
...     total_prot = sum([nasi_prot, daging_prot, ayam_prot, ikan_prot, telur_prot, sayur_prot])
... 
...     return round(total_kcal), round(total_prot, 1)
... 
... 
... def log_makan():
...     print("📋 Log Makan Harian")
...     nasi = input("Nasi (Half / Full): ")
...     daging = float(input("Daging (g): "))
...     ayam = float(input("Ayam (g): "))
...     ikan = float(input("Ikan (g): "))
...     telur = int(input("Telur (biji): "))
...     sayur = input("Sayur/Sambal (Yes / No): ")
... 
...     kalori, protein = kira_kalori_protein(nasi, daging, ayam, ikan, telur, sayur)
... 
...     print("\n✅ Log Berjaya:")
...     print(f"📅 Tarikh: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
...     print(f"🔥 Kalori: {kalori} kcal")
...     print(f"💪 Protein: {protein} g")
... 
...     # Optional: Simpan ke fail
...     save = input("Simpan ke log file? (y/n): ")
...     if save.lower() == "y":
...         with open("log_makan.csv", "a") as f:
...             f.write(f"{datetime.now()},{nasi},{daging},{ayam},{ikan},{telur},{sayur},{kalori},{protein}\n")
...         print("🗂️ Disimpan ke log_makan.csv")
... 
... 
... if __name__ == "__main__":
...     log_makan()
