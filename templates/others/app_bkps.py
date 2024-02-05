# Import Flask and Flask-WTF
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
# Import WTForms fields and validators
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# Create a Flask app
app = Flask(__name__)
# Set a secret key for CSRF protection
app.secret_key = "1234"

# Create a contact form class
class ContactForm(FlaskForm):
    # Define the form fields and validators
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

# Create a route for the contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Create a form object
    form = ContactForm()
    # Check if the form is submitted and validated
    if form.validate_on_submit():
        # Get the form data
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Do something with the data (e.g. send an email, save to a database, etc.)
        print(f"Name: {name}, Email: {email}, Message: {message}")
        # Redirect to a thank you page
        return render_template("thank.html")
    # Render the contact page with the form
    return render_template("contact.html", form=form)

# Run the app
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
