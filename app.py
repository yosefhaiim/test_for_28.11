from flask import Flask, Blueprint, render_template_string

from main import phone_blueprint

app = Flask(__name__)


# הרצה
if __name__ == "__main__":
    app.register_blueprint(phone_blueprint, url_prefix='/api')
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)



