from flask import redirect, request, render_template, url_for, Flask
#from fib import fb
import num2words
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/result", methods=["POST"])
def result():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
    number = num2words.final_word(int(u_input))
    return render_template("result.html", output = number, usr_input = u_input)

if __name__ == '__main__':
    app.run(debug=True)