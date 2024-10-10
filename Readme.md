Necesita instalar nodeJS, python
Luego instalar las librerias

#crear el archivo de bibliotecas
pip freeze > requirements.txt or
python -m pip freeze > requirements.txt

#instalar archivo de bibliotecas
pip install -r requirements.txt

#o instalas individual
pip install flask psycopg2 flask-cors bcrypt fpdf pandas