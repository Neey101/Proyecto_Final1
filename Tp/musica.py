from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Tp.db import get_db

bp = Blueprint('musica', __name__, url_prefix='/musica/')

@bp.route('/')
def index():
    db = get_db()
    tracks = db.execute(
        """SELECT name AS nombre, trackId
         FROM tracks
         ORDER BY name ASC """
    ).fetchall()
    return render_template('musica/index.html', tracks=tracks)


@bp.route('/<int:id>', methods=('GET', 'POST'))
def detalle(id):
    track = get_db().execute(
        """SELECT t.name, t.milliseconds, g.Name as genero
	        FROM tracks t
            JOIN genres g ON g.GenreId = t.GenreId
            WHERE t.trackId = ?
		    ORDER BY t.Name ASC """,
        (id,)
    ).fetchone()
    return render_template('musica/detalle.html', track=track)

