const cookDuration = Number(window.cookDuration);


const tempElement = document.getElementById("current_temperature");
const timeElement = document.getElementById("time_remaining");
const statusTableBody = document.getElementById("status_table").querySelector("tbody");
const pythonUpdate = new EventSource(`/log/stream/${cookDuration}`);


pythonUpdate.onmessage = (event) => {
    const data = JSON.parse(event.data);

    const time_of_start = data[1];
    const status = data[0];

    tempElement.textContent = status.curr_temp;
    const time_diff = status.timestamp - time_of_start;

    const row = document.createElement("tr");
    const timestampCell = document.createElement("td");
    const tempCell = document.createElement("td");

    const date = new Date(status.timestamp * 1000);     // might be wrong, idr the type of timestamp
    timestampCell.textContent = date.toLocaleTimeString();
    tempCell.textContent = status.curr_temp;            // in Celsius

    row.appendChild(timestampCell);
    row.appendChild(tempCell);

    if (statusTableBody.firstChild) {
        statusTableBody.insertBefore(row, statusTableBody.firstChild);
    }
    else {
        statusTableBody.appendChild(row);
    }

    console.log("status.timestamp = " + status.timestamp + 
        ",\n time_of_start = " + time_of_start + 
        ",\n time_diff = " + time_diff);
    timeElement.textContent = Math.round(cookDuration - time_diff);
};

pythonUpdate.onerror = (e) => {
  console.error("SSE error", e);
};