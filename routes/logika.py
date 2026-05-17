from flask import Blueprint, render_template, request
from utils.history import add_history, get_history

logika_bp = Blueprint('logika_bp', __name__)

@logika_bp.route('/logika', methods=['GET', 'POST'])
def logika():
    hasil = None
    rumus = ""
    langkah = []
    
    if request.method == "POST":
        try:
            bool1_str = request.form.get("bool1")
            bool2_str = request.form.get("bool2")
            operator = request.form.get("operator")
            
            b1 = (bool1_str == "1")
            b2 = (bool2_str == "1")
            
            langkah.append(f"1. Ambil input B1: {b1}")
            if operator != "not":
                langkah.append(f"2. Ambil input B2: {b2}")
            langkah.append(f"3. Lakukan gerbang logika {operator.upper()}")
            
            if operator == "and":
                hasil = b1 and b2
                rumus = f"{b1} AND {b2} = {hasil}"
            elif operator == "or":
                hasil = b1 or b2
                rumus = f"{b1} OR {b2} = {hasil}"
            elif operator == "not":
                hasil = not b1
                rumus = f"NOT {b1} = {hasil}"
            elif operator == "xor":
                hasil = b1 ^ b2
                rumus = f"{b1} XOR {b2} = {hasil}"
            elif operator == "nand":
                hasil = not (b1 and b2)
                rumus = f"{b1} NAND {b2} = {hasil}"
            elif operator == "nor":
                hasil = not (b1 or b2)
                rumus = f"{b1} NOR {b2} = {hasil}"
                
            langkah.append(f"4. Didapatkan nilai kebenaran akhir: {hasil}")
            add_history({"tipe": "Logika", "rumus": rumus, "hasil": hasil})
        except:
            hasil = "Error"
            rumus = "Input Logika Tidak Valid"

    return render_template("logika.html", hasil=hasil, rumus=rumus, langkah=langkah, history=get_history())
