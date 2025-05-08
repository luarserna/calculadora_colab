from flask import Flask, render_template, jsonify, request
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import io
import base64

matplotlib.use('agg')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Front.html')


def desarrollar_grafico(bio = True, hi = True):
    """
        Función que devuelve un gráfico compatible con
        Estructura Json
        Entradas: bio (Bool): Habilita gráfico generación por biomasa
                  hi (Boll): Habilita gráfico generación por hidroeléctrica
    """
    file_path = '02 modern-renewable-energy-consumption.csv'
    df = pd.read_csv(file_path)
    Grupos = df.groupby('Entity')
    DataColombia = Grupos.get_group('Colombia')
    if bio:
        plt.plot(DataColombia['Year'], 
                 DataColombia['Geo Biomass Other - TWh'],
                 label = 'Biomasa')
    if hi:
        plt.plot(DataColombia['Year'], 
                 DataColombia['Hydro Generation - TWh'],
                 label = 'Hidroeléctrica')
    plt.legend()
    plt.title('Generación de energía por año')
    plt.grid()
    buf = io.BytesIO() 
    plt.savefig(buf, format='png') 
    buf.seek(0) 
    imagen = base64.b64encode(buf.getvalue()).decode('utf-8') 
    buf.close() 
    plt.close()
    return imagen

     
@app.route('/grafico')
def grafico():
    # Se crea el Query String
    biomasa = 'biomasa' in request.args
    hidro = 'hidro' in request.args
    imagen = desarrollar_grafico(biomasa, hidro)
    return jsonify({'imagen': imagen})  
if __name__ == '__main__':
    app.run(debug=True)
    
