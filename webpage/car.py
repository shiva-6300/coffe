from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Car Page</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
            }
            .box {
                margin-top: 100px;
                padding: 20px;
                background: white;
                display: inline-block;
                border-radius: 10px;
                box-shadow: 0 0 10px gray;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚗 Car Website Running on EC2</h1>
            <p>Deployed using Jenkins CI/CD</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
