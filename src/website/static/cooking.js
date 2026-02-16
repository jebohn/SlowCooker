// blah blah blah
const tempElement = document.getElementById("temp");
const timeElement = document.getElementById("time");
const pythonUpdate = new EventSource('/log/stream');


pythonUpdate.onmessage = (event) => {
    const data = JSON.parse(event.data);


    tempElement.textContent = event.curr_temp;
    timeElement.textContent = event.timestamp;
}
