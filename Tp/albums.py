from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Tp.db import get_db

bp = Blueprint('albumes', __name__, url_prefix='/albumes/')

@bp.route('/')
def index():
    db = get_db()
    album = db.execute(
         """SELECT al.AlbumId AS id, al.Title AS album 
         FROM albums al
         ORDER BY al.Title ASC """
    ).fetchall()
    return render_template('albumes/index.html', album=album)


@bp.route('/<int:id>', methods=('GET', 'POST'))
def detalle(id):
    album = get_db().execute(
        """SELECT a.Title as titulo, ar.Name as nombre
            FROM albums a JOIN artists ar ON a.ArtistId = ar.ArtistId
            WHERE a.ArtistId = ?
            ORDER BY a.Title ASC"""
        (id,)
    ).fetchone()
    return render_template('albumes/index.html', album=album)

