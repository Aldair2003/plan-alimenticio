from flask import Flask, render_template, request
from planes_alimenticios import obtener_plan_alimenticio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        peso_actual = float(request.form['peso_actual'])
        horas_ejercicio = float(request.form['horas_ejercicio'])
        objetivo = request.form['objetivo']
        peso_ideal = float(request.form['peso_ideal'])
        compromiso = request.form['compromiso']

        plan = obtener_plan_alimenticio(peso_actual, horas_ejercicio, objetivo, peso_ideal, compromiso)
        return render_template('resultado.html', plan=plan)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)