import os
import base64
from io import BytesIO  # Add this import
from static.scripts.qrcode import qrcode
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    data = "Your_QR_Code_Data"  # Replace with your data
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to a data URL
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    qr_data_url = f"data:image/png;base64,{img_str}"

    return render_template('index.html', qr_data_url=qr_data_url)

@app.route('/about/')
def about():
    return render_template('about.html')
