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
         """SELECT AlbumId AS id, Title AS album 
         FROM albums
         ORDER BY Title ASC """
    ).fetchall()
    return render_template('albumes/index.html', album=album)