from flask import Flask
from fiu_controller import fiu_blueprint
from fip_controller import fip_blueprint
from aa_controller import aa_blueprint

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(fiu_blueprint, url_prefix='/v1/FIU')
app.register_blueprint(fip_blueprint, url_prefix='/v1/FIP')
app.register_blueprint(aa_blueprint, url_prefix='/v1/AA')


if __name__ == '__main__':
    app.run(debug=True, port=5000)