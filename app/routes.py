from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Player, db
from .forms import PlayerForm

app = Blueprint('app', __name__)

@app.route('/')
def home():
    return redirect(url_for('app.index'))

@app.route('/index')
def index():
    players = Player.query.all()
    return render_template('index.html', players=players)



@app.route('/input', methods=['GET', 'POST'])
def input():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(player_name=form.player_name.data, word_1=form.word_1.data)
        db.session.add(player)
        db.session.commit()
        flash('Player data submitted successfully!', 'success')
        return redirect(url_for('app.index'))
    return render_template('input.html', form=form)

