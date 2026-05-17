from flask import Blueprint, render_template, request
import math
from utils.history import add_history, get_history

aritmatika_bp = Blueprint('aritmatika_bp', __name__)

@aritmatika_bp.route('/aritmatika', methods=['GET', 'POST'])
def aritmatika():
    hasil = None
    rumus = ""
    langkah = []
    
    if request.method == "POST":
        try:
            angka1_str = request.form.get("angka1")
            angka2_str = request.form.get("angka2")
            operator = request.form.get("operator")
            
            angka1 = float(angka1_str) if angka1_str else 0
            angka2 = float(angka2_str) if angka2_str else 0
            
            langkah.append(f"1. Ambil angka pertama = {angka1}")
            if operator != "akar": 
                langkah.append(f"2. Ambil angka kedua = {angka2}")
            langkah.append(f"3. Lakukan operasi '{operator}'")
            
            if operator == "+":
                hasil = angka1 + angka2
                rumus = f"{angka1} + {angka2} = {hasil}"
            elif operator == "-":
                hasil = angka1 - angka2
                rumus = f"{angka1} - {angka2} = {hasil}"
            elif operator == "x":
                hasil = angka1 * angka2
                rumus = f"{angka1} × {angka2} = {hasil}"
            elif operator == "/":
                if angka2 == 0:
                    hasil = "Error"
                    rumus = "Tidak bisa membagi dengan 0!"
                else:
                    hasil = angka1 / angka2
                    rumus = f"{angka1} ÷ {angka2} = {hasil}"
            elif operator == "pangkat":
                hasil = angka1 ** angka2
                rumus = f"{angka1} pangkat {angka2} = {hasil}"
            elif operator == "akar":
                hasil = math.sqrt(angka1)
                rumus = f"Akar dari {angka1} = {hasil}"
            elif operator == "modulus":
                hasil = angka1 % angka2
                rumus = f"{angka1} modulus {angka2} = {hasil}"
            elif operator == "floor":
                if angka2 == 0:
                    hasil = "Error"
                    rumus = "Tidak bisa membagi dengan 0!"
                else:
                    hasil = angka1 // angka2
                    rumus = f"{angka1} floor divisi {angka2} = {hasil}"
                    
            langkah.append(f"4. Selesai, hasil didapat = {hasil}")
            
            add_history({"tipe": "Aritmatika", "rumus": rumus, "hasil": hasil})
        except Exception as e:
            hasil = "Error"
            rumus = "Format Penulisan Angka Salah"
            langkah = ["Input tidak valid"]

    return render_template("aritmatika.html", hasil=hasil, rumus=rumus, langkah=langkah, history=get_history())
