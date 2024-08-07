# Plan Alimenticio

## Descripción
Este proyecto es un sistema experto que genera planes alimenticios personalizados basados en las respuestas del usuario a un cuestionario nutricional. Utiliza Flask como backend, HTML y CSS para el frontend, creando una aplicación web interactiva para proporcionar recomendaciones de planes alimenticios.

## Características
- Cuestionario interactivo sobre hábitos de salud y objetivos nutricionales.
- Generación de planes alimenticios personalizados.
- Interfaz de usuario responsiva.
- Backend en Python con Flask.

## Tecnologías Utilizadas
- Python 3
- Flask
- HTML5
- CSS3

## Instalación
1. Clona este repositorio:
git clone https://github.com/Aldair2003/plan-alimenticio.git

2. Navega al directorio del proyecto:
cd plan-alimenticio

3. Instala las dependencias necesarias:
pip install flask

## Uso
1. Ejecuta la aplicación Flask:
python app.py

2. Abre un navegador y visita `http://localhost:5000`.
3. Completa el cuestionario y obtén tu plan alimenticio personalizado.

## Archivos Principales
- `app.py`: Contiene la lógica principal de la aplicación Flask.
- `planes_alimenticios.py`: Define los planes alimenticios y la lógica para seleccionarlos.
- `templates/index.html`: Página principal con el formulario del cuestionario.
- `templates/resultado.html`: Página que muestra el plan alimenticio generado.
- `static/style.css`: Estilos CSS para la aplicación.

