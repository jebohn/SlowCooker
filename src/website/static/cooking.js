// blah blah blah
const cookDuration = Number(window.cookDuration);

const tempElement = document.getElementById("current_temperature");
const timeElement = document.getElementById("time_remaining");
const pythonUpdate = new EventSource(`/log/stream/${cookDuration}`);


pythonUpdate.onmessage = (event) => {
    const data = JSON.parse(event.data);

    const time_of_start = data[1];
    const status = data[0];


    tempElement.textContent = status.curr_temp;
    timeElement.textContent = Math.round(cookDuration - (status.timestamp - time_of_start));
}

pythonUpdate.onerror = (e) => {
  console.error("SSE error", e);
};