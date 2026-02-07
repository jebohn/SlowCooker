from flask import Flask, request, jsonify, render_template, url_for
# from hardware.ssr import SSR

app = Flask(__name__)
# hardware = SSR()

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/start_cook", methods=["POST"])
def start_cook():
    total_time = int(request.form["total_time"])
    temperature = int(request.form["temperature"])
    segments = int(request.form["segments"])

    segment_duration = total_time / segments
    segment_duration_str = f"{segment_duration:.2f}"

    return render_template('cooking.html', time = total_time, temp = temperature, segments = segments, segment_duration = segment_duration_str)

@app.route("/log")
def log():
    return '<h1>Cook Log</h1>'
    
# Without this if statement, the program will automatically run the web server if this class is imported
if __name__ == '__main__':
    app.run(debug=True)