from flask import Flask, render_template
app=Flask(__name__)

@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    weight=int(weight)
    height=int(height)
    bmi=weight/(height**2)
    return str(bmi) and render_template('bmi.html')
    

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)



