from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('homeo', __name__)


@bp.route('/')
def index():
    db = get_db()
    remedies = db.execute(
        'SELECT r.id, r.name, potency, created, updated, user_id, username, materia_medica_link'
        ' FROM remedy r '
        ' JOIN user u ON r.user_id = u.id'
        ' JOIN remedy_potency p ON r.potency_id = p.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('homeo/index.html', remedies=remedies)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        potency_id = request.form['potency']
        mlink = request.form['materia_medica_link']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO remedy (name, potency_id, user_id, materia_medica_link)'
                ' VALUES (?, ?, ?, ?)',
                (name, potency_id, g.user['id'], mlink)
            )
            db.commit()
            return redirect(url_for('homeo.index'))

    potency_list = get_db().execute('SELECT id, potency FROM remedy_potency').fetchall()

    return render_template('homeo/create.html', potency_list=potency_list)


def get_remedy(id, check_user=True):
    remedy = get_db().execute(
        'SELECT r.id, r.name, r.potency_id, potency, created, updated, user_id, username, materia_medica_link'
        ' FROM remedy r '
        ' JOIN user u ON r.user_id = u.id'
        ' JOIN remedy_potency p ON r.potency_id = p.id'
        ' WHERE r.id = ?',
        (id,)
    ).fetchone()

    if remedy is None:
        abort(404, f"Remedy id {id} doesn't exist.")

    if check_user and remedy['user_id'] != g.user['id']:
        abort(403)

    return remedy


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    remedy = get_remedy(id)
    potency_id = remedy['potency_id']

    if request.method == 'POST':
        name = request.form['name']
        potency_id = request.form['potency']
        mlink = request.form['materia_medica_link']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE remedy SET name = ?, potency_id = ?, materia_medica_link = ?'
                ' WHERE id = ?',
                (name, potency_id, mlink, id)
            )
            db.commit()
            return redirect(url_for('homeo.index'))

    potency_list = get_db().execute('SELECT id, potency FROM remedy_potency').fetchall()

    return render_template('homeo/update.html', remedy=remedy, potency_list=potency_list, sel_potency_id=potency_id)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_remedy(id)
    db = get_db()
    db.execute('DELETE FROM remedy WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('homeo.index'))


@bp.route('/list_p')
def list_p():
    db = get_db()
    potencies = db.execute(
        'SELECT id, potency'
        ' FROM remedy_potency p '        
        ' ORDER BY potency DESC'
    ).fetchall()

    return render_template('homeo/list_p.html', potencies=potencies)


@bp.route('/add_p')
@login_required
def add_p():
    db = get_db()
    potency = db.execute(
        'SELECT id, potency'
        ' FROM remedy_potency p '        
        ' ORDER BY potency DESC'
    ).fetchall()

    return render_template('homeo/list_p.html')


@bp.route('/update_p')
@login_required
def update_p():
    db = get_db()
    potency = db.execute(
        'SELECT id, potency'
        ' FROM remedy_potency p '        
        ' ORDER BY potency DESC'
    ).fetchall()

    return render_template('homeo/list_p.html')