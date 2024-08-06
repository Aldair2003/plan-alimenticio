from flask import Flask, render_template, request

app = Flask(__name__)

base_conocimiento = {
    "Plan 1": {
        "peso": "menos de 70",
        "ejercicio": "menos de 1 hora",
        "objetivo": "estéticos",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    "Plan 2": {
        "peso": "menos de 70",
        "ejercicio": "menos de 1 hora",
        "objetivo": "salud",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    "Plan 3": {
        "peso": "menos de 70",
        "ejercicio": "1 a 2 horas",
        "objetivo": "estéticos",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    "Plan 4": {
        "peso": "menos de 70",
        "ejercicio": "1 a 2 horas",
        "objetivo": "salud",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    "Plan 5": {
        "peso": "70 a 90",
        "ejercicio": "menos de 1 hora",
        "objetivo": "estéticos",
        "peso_ideal": "70 a 90",
        "compromiso": "sí"
    },
    "Plan 6": {
        "peso": "70 a 90",
        "ejercicio": "menos de 1 hora",
        "objetivo": "salud",
        "peso_ideal": "70 a 90",
        "compromiso": "sí"
    },
    "Plan 7": {
        "peso": "70 a 90",
        "ejercicio": "1 a 2 horas",
        "objetivo": "estéticos",
        "peso_ideal": "70 a 90",
        "compromiso": "sí"
    },
    "Plan 8": {
        "peso": "70 a 90",
        "ejercicio": "1 a 2 horas",
        "objetivo": "salud",
        "peso_ideal": "70 a 90",
        "compromiso": "sí"
    },
    "Plan 9": {
        "peso": "más de 90",
        "ejercicio": "menos de 1 hora",
        "objetivo": "estéticos",
        "peso_ideal": "más de 90",
        "compromiso": "sí"
    },
    "Plan 10": {
        "peso": "más de 90",
        "ejercicio": "menos de 1 hora",
        "objetivo": "salud",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    "Plan 11": {
        "peso": "más de 90",
        "ejercicio": "1 a 2 horas",
        "objetivo": "estéticos",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    "Plan 12": {
        "peso": "más de 90",
        "ejercicio": "1 a 2 horas",
        "objetivo": "salud",
        "peso_ideal": "menos de 70",
        "compromiso": "sí"
    },
    # Añade más combinaciones según sea necesario
}

def recomendar_plan(respuestas):
    print("Respuestas del usuario:", respuestas)
    for plan, condiciones in base_conocimiento.items():
        match = True
        print(f"Evaluando {plan} con condiciones {condiciones}")
        for clave, valor in condiciones.items():
            respuesta_usuario = respuestas.get(clave).strip().lower()
            valor_condicion = valor.strip().lower()
            if respuesta_usuario != valor_condicion:
                print(f"No coincide: {clave} (Usuario: {respuesta_usuario} vs Condición: {valor_condicion})")
                match = False
                break
        if match:
            return plan
    return "No se encontró un plan adecuado para tus respuestas."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        respuestas = {
            "peso": request.form.get("peso"),
            "ejercicio": request.form.get("ejercicio"),
            "objetivo": request.form.get("objetivo"),
            "peso_ideal": request.form.get("peso_ideal"),
            "compromiso": request.form.get("compromiso")
        }
        print(f"Respuestas recibidas: {respuestas}")
        plan_recomendado = recomendar_plan(respuestas)
        return render_template("index.html", plan=plan_recomendado, respuestas=respuestas)
    return render_template("index.html", plan=None, respuestas=None)

if __name__ == "__main__":
    app.run(debug=True)
