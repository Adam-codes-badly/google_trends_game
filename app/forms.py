from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PlayerForm(FlaskForm):
    player_name = StringField('Player Name', validators=[DataRequired()])
    word_1 = StringField('Word', validators=[DataRequired()])
    submit = SubmitField('Submit')
