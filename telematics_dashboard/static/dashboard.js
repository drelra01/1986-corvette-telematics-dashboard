function updateDashboard() {
    fetch("/data")
        .then(response => response.json())
        .then(data => {
            document.getElementById("rpm").textContent = data.rpm;
            document.getElementById("coolant").textContent = data.coolant_temp + " °F";
            document.getElementById("throttle").textContent = data.throttle + "%";
            document.getElementById("battery").textContent = data.battery + " V";
            document.getElementById("speed").textContent = data.speed + " MPH";
            document.getElementById("engine_load").textContent = data.engine_load + "%";
            document.getElementById("battery_health").textContent = data.battery_health;
            document.getElementById("coolant_status").textContent = data.coolant_status;
        });
}

setInterval(updateDashboard, 1000);