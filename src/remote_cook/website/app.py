from flask import Flask, request, render_template, redirect

# class WebInterfaceAPI:
app = Flask(__name__)

@app.route('/')       
def home(): 
    return render_template('start.html')

@app.route("/start", methods=['POST'])
def start():
    temperature = request.form['temp']
    time = request.form['time']
    return render_template("cooking.html", temperature=temperature, time=time)

@app.route("/end", methods=['POST'])
def end():
    return redirect('/')

# Without this if statement, the program will automatically run the web server if this class is imported
if __name__ == '__main__':
    app.run(debug=True)