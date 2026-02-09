from flask import Flask, Response, request, render_template
import json
from src.SlowCookerMain import SlowCookerMain

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/start_cook", methods=["POST"])
def start_cook():
    cook_duration = int(request.form["cook_duration"])
    target_temp = int(request.form["target_temp"])
    intervals = int(request.form["intervals"])

    interval_duration = cook_duration / intervals
    interval_duration_str = f"{interval_duration:.2f}"

    slow_cooker = SlowCookerMain(target_temp, cook_duration)
    slow_cooker.run()

    return render_template('cooking.html', time = cook_duration, temp = target_temp, 
                           segments = intervals, segment_duration = interval_duration_str)

@app.route("/log")
def log():
    return '<h1>Cook Log</h1>'
    
# Without this if statement, the program will automatically run the web server if this class is imported
if __name__ == '__main__':
    app.run(debug=True)