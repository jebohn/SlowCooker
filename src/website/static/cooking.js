const cookDuration = Number(window.cookDuration);

const tempElement = document.getElementById("current_temperature");
const timeElement = document.getElementById("time_remaining");
const pythonUpdate = new EventSource(`/log/stream/${cookDuration}`);


pythonUpdate.onmessage = (event) => {
    const data = JSON.parse(event.data);

    const time_of_start = data[1];
    const status = data[0];


    tempElement.textContent = status.curr_temp;
    const time_diff = status.timestamp - time_of_start;
    console.log("status.timestamp = " + status.timestamp + 
        ",\n time_of_start = " + time_of_start + 
        ",\n time_diff = " + time_diff)
    timeElement.textContent = Math.round(cookDuration - time_diff);
}

pythonUpdate.onerror = (e) => {
  console.error("SSE error", e);
};