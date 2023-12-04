from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Tp.db import get_db

bp = Blueprint('artistas', __name__, url_prefix='/artistas/')

@bp.route('/')
def index():
    db = get_db()
    artistas = db.execute(
        """SELECT ar.ArtistId AS id, ar.Name AS artista 
         FROM artists ar 
         ORDER BY ar.Name DESC """
    ).fetchall()
    return render_template('artistas/index.html', artistas=artistas)