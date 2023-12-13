from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key="secret key 123 super safe"


@app.route('/', methods=['GET','POST'])
def numero_formulario():
    if 'numrandom' not in session:
        session['numrandom']=random.randint(1,100)
        session['intentos'] = 0
    else:
        print(session['numrandom'])
    return render_template("index.html", random_number=session['numrandom'])

@app.route('/adivinar', methods=['POST'])
def intento_adivinar():
    session['intentos'] += 1
    if int(request.form['adivina-numbero']) == session['numrandom']:     #si se adivina el número
        session['fue-adivinado'] = 1
    elif int(request.form['adivina-numbero']) < session['numrandom']:                
        session['fue-adivinado'] = 2  
    else:
        session['fue-adivinado'] = 3
    return redirect("/guess")

@app.route('/guess')
def guess():
    intentos = session['intentos']
    if session['fue-adivinado'] == 1:
        resultado = "Es igual"
        resultado_id = "correcto"
        session.clear()
    elif session['fue-adivinado'] == 2:
        resultado = "Es menor"
        resultado_id = "incorrecto"
    else:
        resultado = "Es mayor"
        resultado_id = "incorrecto"
    return render_template("index.html", resultado=resultado, resultado_id=resultado_id, intentos=intentos)


if __name__=="__main__":
    app.run(debug=True)