from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Tp.db import get_db

bp = Blueprint('musica', __name__, url_prefix='/musica/')

@bp.route('/')
def index():
    db = get_db()
    track = db.execute(
        """SELECT name AS nombre
         FROM tracks
         ORDER BY name ASC """
    ).fetchall()
    return render_template('musica/index.html', track=track)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def detalle(id, check_author=True):
    post = get_db().execute(
        """SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?""",
        (id,)
    ).fetchone()



    return render_template('musica/index.html', track=track)