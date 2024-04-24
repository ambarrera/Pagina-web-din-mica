from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index", methods=["POST"])
def cv():
    if request.method== 'POST':
        name=request.form['name']
        last_name = request.form['last_name']
        occupation = request.form['occupation']
        phone = request.form['phone']
        email = request.form['email']
        born = request.form['born']
        nationality = request.form['nationality']
        english_level = request.form['english_level']
        aptitudes = request.form['aptitudes']
        habilities = request.form['habilities']
        programing_languagues = request.form['programing_languagues']
        perfil = request.form['perfil']

        if not name or not last_name or not phone or not email or not born:
            return render_template("index.html", error="Por favor, completa todos los campos obligatorios.")

    return render_template("cv.html", name=name, last_name=last_name, occupation=occupation, phone=phone, email=email,
                               born=born, nationality=nationality, english_level=english_level, aptitudes=aptitudes,
                               habilities=habilities, programing_languagues=programing_languagues, perfil=perfil)


if __name__ == "__main__":
    app.run(debug=True)

