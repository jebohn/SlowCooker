from flask import Flask, request, jsonify
from hardware.ssr import SSR

app = Flask(__name__)
hardware = SSR()

@app.route("/")
def home():
    return """
    <h1>Remote Cook Home</h1>
    <p>Use the form below to set cook time and temperature.</p>
    <form action="/start_cook" method="post">
        Total cook time (minutes): <input type ="number" name="total_time" required><br><br>
        Temperature (C): <input type ="number" name="temperature" required><br><br>
        Segments:
        <select name="segments">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
        </select><br><br>
        <input type="submit" value="Start Cook">
    </form>
    """
    
@app.route("/start_cook", methods=["POST"])
def start_cook():
    total_time = int(request.form["total_time"])
    temperature = int(request.form["temperature"])
    segments = int(request.form["segments"])

    segment_duration = total_time / segments

    return f"""
    <h1>Cooking Started!</h1>
    <p>Total time: {total_time} minutes</p>
    <p>Temperature: {temperature} C</p>
    <p>Segments: {segments}, each segment: {segment_duration:.2f} minutes</p>
    <p>(Send commands to SSR hardware)</p>
    <a href="/home">Back</a>
    """

@app.route("/log")
def log():
    return '<h1>Cook Log</h1>'
    
# Without this if statement, the program will automatically run the web server if this class is imported
if __name__ == '__main__':
    app.run(debug=True)