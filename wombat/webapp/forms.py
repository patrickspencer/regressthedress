from wtforms import Form, StringField, SubmitField, validators

class DescriptionForm(Form):
    description = StringField('Description', [validators.Length(min=1, max=5000)])
    submit = SubmitField(label='Submit')

