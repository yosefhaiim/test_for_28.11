from flask import Flask, Blueprint, render_template_string

app = Flask(__name__)

phone_blueprint = Blueprint('phone_blueprint', __name__)

# הרצה
if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)



