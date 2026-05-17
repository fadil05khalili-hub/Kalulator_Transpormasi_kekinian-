from flask import Blueprint, render_template, request
from utils.history import add_history, get_history

konversi_bp = Blueprint('konversi_bp', __name__)

@konversi_bp.route('/konversi', methods=['GET', 'POST'])
def konversi():
    hasil = None
    rumus = ""
    langkah = []
    
    if request.method == "POST":
        kategori = request.form.get("kategori")
        
        # 3A. KONVERSI BASIS BILANGAN
        if kategori == "basis":
            try:
                angka_str = request.form.get("angka_basis")
                basis_asal = request.form.get("basis_asal")
                
                langkah.append(f"1. Angka asli: {angka_str} ({basis_asal})")
                
                if basis_asal == "desimal":
                    angka_dec = int(angka_str)
                elif basis_asal == "biner":
                    angka_dec = int(angka_str, 2)
                elif basis_asal == "oktal":
                    angka_dec = int(angka_str, 8)
                elif basis_asal == "hexa":
                    angka_dec = int(angka_str, 16)
                    
                langkah.append(f"2. Konversi ke bentuk fungsi dasar python")
                
                biner_hasil = bin(angka_dec).replace("0b", "")
                oktal_hasil = oct(angka_dec).replace("0o", "")
                hexa_hasil = hex(angka_dec).replace("0x", "").upper()
                
                hasil = f"Dec: {angka_dec} | Bin: {biner_hasil} | Oct: {oktal_hasil} | Hex: {hexa_hasil}"
                rumus = f"Basis Konversi dari: {angka_str} [{basis_asal}]"
                add_history({"tipe": "Basis", "rumus": rumus, "hasil": hasil})
            except:
                hasil = "Error"
                rumus = "Karakter tidak cocok untuk basis yang dipilih."
                
        # 3B. KONVERSI SUHU 
        elif kategori == "suhu":
            try:
                c = float(request.form.get("suhu"))
                
                f = (c * 9/5) + 32
                k = c + 273.15
                r = c * 4/5
                
                hasil = f"F: {round(f,2)}° | K: {round(k,2)}° | R: {round(r,2)}°"
                rumus = f"{c} °Celcius Dikonversi"
                langkah = [
                    f"1. Celcius = {c}", 
                    "2. F = (C × 9/5) + 32", 
                    "3. K = C + 273.15", 
                    "4. R = C × 4/5"
                ]
                add_history({"tipe": "Suhu", "rumus": rumus, "hasil": hasil})
            except:
                hasil = "Error"
                rumus = "Salah input Suhu"
                
        # 3C. KONVERSI MATA UANG
        elif kategori == "uang":
            try:
                idr = float(request.form.get("uang_idr"))
                rate_usd = 16000
                rate_eur = 17500
                rate_sgd = 12000
                
                usd = idr / rate_usd
                eur = idr / rate_eur
                sgd = idr / rate_sgd
                
                hasil = f"USD: ${usd:.2f} | EUR: €{eur:.2f} | SGD: S${sgd:.2f}"
                rumus = f"Uang Awal: Rp {idr}"
                langkah = [
                    "1. Uang dibagi sesuai Rate Tetap (Statis)",
                    f"2. USD = Rp / {rate_usd}",
                    f"3. EUR = Rp / {rate_eur}",
                    f"4. SGD = Rp / {rate_sgd}"
                ]
                add_history({"tipe": "Uang", "rumus": rumus, "hasil": hasil})
            except:
                hasil = "Error"
                rumus = "Input harus berupa angka."

    return render_template("konversi.html", hasil=hasil, rumus=rumus, langkah=langkah, history=get_history())
