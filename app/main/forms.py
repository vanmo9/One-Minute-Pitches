from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchesForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    category = StringField('Give Your Pitches' ,validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    title = StringField('Comment',validators=[Required()])
    comment = TextAreaField('Comment pitches',validators = [Required()])
    submit = SubmitField('Submit')
