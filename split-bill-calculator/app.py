from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Rute untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk menangani perhitungan
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        total_bill = float(request.form['total_bill'])
        tip = int(request.form['tip'])
        people = int(request.form['people'])

        bill_per_person = (total_bill * (1 + tip / 100)) / people
        final_result = round(bill_per_person, 2)

        # Tampilkan hasil dengan format mata uang
        return render_template('index.html', result=f"Rp {final_result:,.2f}")

    except (ValueError, ZeroDivisionError):
        error_message = "Input tidak valid. Pastikan semua kolom diisi dengan angka."
        return render_template('index.html', error=error_message)

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)