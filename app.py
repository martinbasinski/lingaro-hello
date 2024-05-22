from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
    <head>
        <title>Hello Lingaro</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <img src="https://lingarogroup.com/hubfs/Lingaro_June_2022/Images/logo_lingaro.svg" alt="Lingaro Logo" width="100" height="40">
        <p>Welcome to my Azure Web App!</p>
        <p>Thank you for the opportunity to complete the training exercise.</p>
        <p>made by Marcin Basinski ;).</p>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)