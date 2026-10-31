import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cargo = request.form.get('cargo')
        rh = request.form.get('rh')
        foto = request.files.get('foto')
        
        if foto and foto.filename:
            filename = secure_filename(foto.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            foto.save(filepath)
    
            return render_template('tarjeta.html', nombre=nombre, cargo=cargo, rh=rh, foto_url=filename)
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)