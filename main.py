from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, ValidationError
app = Flask(__name__)
app.secret_key = "123"


class Box(FlaskForm):
    number1 = IntegerField(name="Number1", validators=[InputRequired()])
    sel = SelectField(choices=["+", "-", "*", "/"])
    number2 = IntegerField(name="Number2", validators=[InputRequired()])
    submit = SubmitField(name="Result")
    res = IntegerField(name="m")


@app.route("/", methods=["GET", "POST"])
def hello_world():
    obj = Box()
    if obj.validate_on_submit():
        if obj.sel.data == "+":
            obj.res.data = obj.number1.data + obj.number2.data
        elif obj.sel.data == "-":
            obj.res.data = obj.number1.data - obj.number2.data
        elif obj.sel.data == "*":
            obj.res.data = obj.number1.data * obj.number2.data
        elif obj.sel.data == "/":
            if obj.number2.data == 0:
                return render_template("zero.html")
            else:
                obj.res.data = obj.number1.data / obj.number2.data
        elif obj.res == "None":
            obj.res.data = "0"
    print(obj.res.data)
    return render_template("calculate.html", var=obj)


if __name__ == "__main__":
    app.run(debug=True)
