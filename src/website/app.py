from flask import Flask, Response, request, redirect, url_for, session, render_template
from threading import Thread
import json
import time
from queue import Queue
from src.SlowCookerMain import SlowCookerMain
from src.Logger import Logger


app = Flask(__name__)

logger = Logger()
status = {}

def log_listener():
	while True:
		log_entry = logger.log_queue.get()
		status.update(log_entry)

Thread(target=log_listener, daemon=True).start()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        cook_duration = int(request.form["cook_duration"])
        target_temp = int(request.form["target_temp"])
        intervals = int(request.form["intervals"])

        session["cook_duration"] = cook_duration
        session["target_temp"] = target_temp
        session["intervals"] = intervals
        

        slow_cooker = SlowCookerMain(target_temp, cook_duration, logger)
        slow_cooker.run()

        return redirect(url_for("cook_session"))
    return render_template("home.html")
    

@app.route("/log", methods=["POST"])
def start_cook():
    cook_duration = session.get("cook_duration")
    target_temp = session.get("target_temp")
    intervals = session.get("intervals")

    interval_duration = cook_duration / intervals
    interval_duration_str = f"{interval_duration:.2f}"

    return render_template("cooking.html", cook_duration = cook_duration, target_temp = target_temp, 
                           intervals = intervals, interval_duration = interval_duration_str)
    
    
@app.route("/log/stream")
def log_stream(cook_duration):
	def event_stream():
		last_timestamp = status.get("timestamp", cook_duration)
		yield f"data: {json.dumps(status)}\n\n"
		while True:
			if status.get("timestamp", 0) > last_timestamp:
				last_timestamp = status.get("timestamp")
				yield f"data: {json.dumps(status)}\n\n"
			time.sleep(0.5)
	return Response(event_stream(), mimetype="text/event_stream")


# Without this if statement, the program will automatically run the web server if this class is imported
if __name__ == "__main__":
    app.run(debug=True)