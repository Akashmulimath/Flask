from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


@app.route('/hello')
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route('/greet', methods=['POST', 'GET'])
def greeter():
    flash("Hello " + str(request.form['name_input']) + ", great to see you!\n" "ಕರ್ನಾಟಕ ನಿಮ್ಮನ್ನು ಸ್ವಾಗತಿಸುತ್ತಿದೆ!")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)