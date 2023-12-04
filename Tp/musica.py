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
        """SELECT name as nombre
         FROM tracks
         ORDER BY name ASC """
    ).fetchall()
    return render_template('musica/index.html', track=track)