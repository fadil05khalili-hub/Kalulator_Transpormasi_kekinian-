from flask import Blueprint, render_template
from utils.history import get_history

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template("index.html", history=get_history())

@main_bp.route('/riwayat')
def riwayat():
    return render_template("riwayat.html", history=get_history())
