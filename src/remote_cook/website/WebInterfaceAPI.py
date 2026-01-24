import flask

class WebInterfaceAPI:
    app = flask(__name__)

    @app.route("/")
    def home():
        return '<h1>Flask REST API</h1>'
    
    # Without this if statement, the program will automatically run the web server if this class is imported
    if __name__ == '__main__':
        app.run(debug=True)