from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/riwayat')
def riwayat():
    return render_template('riwayat.html')

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    if request.method == 'GET':
        return render_template('kalkulator.html')
    
    if request.method == 'POST':
        try:
            bangun_ruang = request.form['bangun_ruang']
            var1 = float(request.form['var1'])
            
            volume = 0
            data_untuk_riwayat = {} 

            if bangun_ruang == 'Tabung':
                var2 = float(request.form['var2'])
                volume = math.pi * (var1 ** 2) * var2
                data_untuk_riwayat = {
                    'nama': 'Tabung',
                    'label1': 'Jari-jari', 'val1': var1,
                    'label2': 'Tinggi', 'val2': var2
                }

            elif bangun_ruang == 'Kerucut':
                var2 = float(request.form['var2'])
                volume = (1/3) * math.pi * (var1 ** 2) * var2
                data_untuk_riwayat = {
                    'nama': 'Kerucut',
                    'label1': 'Jari-jari', 'val1': var1,
                    'label2': 'Tinggi', 'val2': var2
                }

            elif bangun_ruang == 'Bola':
                volume = (4/3) * math.pi * (var1 ** 3)
                data_untuk_riwayat = {
                    'nama': 'Bola',
                    'label1': 'Jari-jari', 'val1': var1
                }

            elif bangun_ruang == 'Kubus':
                volume = var1 ** 3
                data_untuk_riwayat = {
                    'nama': 'Kubus',
                    'label1': 'Sisi', 'val1': var1
                }
            
            elif bangun_ruang == 'Balok':
                var2 = float(request.form['var2'])
                var3 = float(request.form['var3'])
                volume = var1 * var2 * var3
                data_untuk_riwayat = {
                    'nama': 'Balok',
                    'label1': 'Panjang', 'val1': var1,
                    'label2': 'Lebar', 'val2': var2,
                    'label3': 'Tinggi', 'val3': var3
                }
            
            elif bangun_ruang == 'Limas Segiempat':
                var2 = float(request.form['var2'])
                var3 = float(request.form['var3'])
                volume = (1/3) * var1 * var2 * var3
                data_untuk_riwayat = {
                    'nama': 'Limas Segiempat',
                    'label1': 'Panjang Alas', 'val1': var1,
                    'label2': 'Lebar Alas', 'val2': var2,
                    'label3': 'Tinggi Limas', 'val3': var3
                }

            data_untuk_riwayat['hasil'] = round(volume, 2)
            
            return jsonify({
                'success': True,
                'data': data_untuk_riwayat
            })

        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)