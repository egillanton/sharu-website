import os

from flask import Flask, render_template


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only

    # ======== Routing ============================= #
    # -------- Home -------------------------------- #
    @app.route('/', methods=['GET'])
    @app.route('/isl', methods=['GET'])
    def index_isl():
        return render_template('layouts/index_isl.html')
    
    @app.route('/eng', methods=['GET'])
    def index_eng():
        return render_template('layouts/index_eng.html')

    return app