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

        experiencia_laboral_count = int(request.form.get('experienciaLaboralCount', 0))
        formacion_count = int(request.form.get('formacionCount', 0))
        idiomas_count = int(request.form.get('idiomasCount', 0))

        experiencia_laboral = []
        for i in range(1, experiencia_laboral_count + 1):
            empleador = request.form.get(f'empleador{i}')
            cargo = request.form.get(f'cargo{i}')
            fecha_inicio = request.form.get(f'fechaInicio{i}')
            fecha_fin = request.form.get(f'fechaFin{i}')
            descripcion = request.form.get(f'descripcion{i}')
            experiencia_laboral.append({'empleador': empleador, 'cargo': cargo, 'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'descripcion': descripcion})

        formacion = []
        for i in range(1, formacion_count + 1):
            institucion = request.form.get(f'institucion{i}')
            titulo = request.form.get(f'titulo{i}')
            fecha_inicio = request.form.get(f'fechaInicio{i}')
            fecha_fin = request.form.get(f'fechaFin{i}')
            descripcion = request.form.get(f'descripcion{i}')
            formacion.append({'institucion': institucion, 'titulo': titulo, 'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'descripcion': descripcion})
         
        idiomas = []
        for i in range(1, idiomas_count + 1):
            idioma = request.form.get(f'idioma{i}')
            nivel_idioma = request.form.get(f'nivel_idioma{i}')
            idiomas.append({'idioma': idioma, 'nivel_idioma': nivel_idioma})

        if not name or not last_name or not phone or not email or not born:
            return render_template("index.html", error="Por favor, completa todos los campos obligatorios.")

    return render_template("cv.html", name=name, last_name=last_name, occupation=occupation, phone=phone, email=email,
                               born=born, nationality=nationality, english_level=english_level, aptitudes=aptitudes,
                               habilities=habilities, programing_languagues=programing_languagues, perfil=perfil, experiencia_laboral=experiencia_laboral, formacion=formacion, idiomas=idiomas)


if __name__ == "__main__":
    app.run(debug=True)

