from flask import Blueprint, render_template, request
import math
from utils.history import add_history, get_history

bonus_bp = Blueprint('bonus_bp', __name__)

@bonus_bp.route('/bonus', methods=['GET', 'POST'])
def bonus():
    hasil = None
    rumus = ""
    langkah = []
    
    if request.method == "POST":
        try:
            jenis = request.form.get("jenis_bonus")
            angka = int(request.form.get("angka_bonus"))
            
            if angka < 0 or angka > 100:
                raise ValueError("Batas angka wajar")
                
            if jenis == "faktorial":
                hasil = math.factorial(angka)
                rumus = f"{angka}! (Faktorial)"
                langkah = [f"1. Cek angka: {angka}", "2. Kalikan menurun (ex: 3x2x1)"]
            else: 
                deret = [0, 1]
                for i in range(2, angka):
                    deret.append(deret[i-1] + deret[i-2])
                
                if angka == 1: deret = [0]
                if angka == 0: deret = []
                    
                hasil = str(deret[:angka])
                rumus = f"Deret Fibonacci sejumlah {angka}"
                langkah = [
                    "1. Siapkan 0 dan 1 dulu", 
                    "2. Jumlahkan dua nilai belakang untuk yang baru", 
                    f"3. Lakukan hingga dapet list ada {angka} angka."
                ]
            
            add_history({"tipe": "Bonus", "rumus": rumus, "hasil": hasil})
        except:
            hasil = "Error"
            rumus = "Angka terlalu besar atau invalid."

    return render_template("bonus.html", hasil=hasil, rumus=rumus, langkah=langkah, history=get_history())
