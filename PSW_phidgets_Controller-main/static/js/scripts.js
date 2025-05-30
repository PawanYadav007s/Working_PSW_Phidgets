document.getElementById("startBtn").addEventListener("click", async () => {
    try {
        // Get logs and job status areas
        const logsBox = document.getElementById("logs");
        const jobStatusEl = document.getElementById("jobResultStatus");
        const progressBar = document.getElementById("progressBar");

        // Clear previous logs
        logsBox.value = "";
        jobStatusEl.innerText = "Processing...";
        jobStatusEl.style.color = "orange";

        // Fetch settings from backend
        const response = await fetch("/start_loop", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({})  // No body needed; settings are read from settings.json
        });

        const result = await response.json();

        if (result.status === "Completed") {
            const readings = result.readings;
            const jobStatus = result.job_status;
            const duration = result.duration;

            let logsText = "";

            readings.forEach((reading, index) => {
                logsText += `Cycle ${reading["Cycle"]}: Voltage = ${reading["Voltage (V)"]}V, Current = ${reading["Current (A)"]}A, Status = ${reading["Status"]}\n`;

                // Update progress bar
                const percentage = Math.round(((index + 1) / readings.length) * 100);
                progressBar.style.width = `${percentage}%`;
            });

            logsText += `\nJob Status: ${jobStatus}\nTotal Time: ${duration} seconds`;
            logsBox.value = logsText;

            // Show result
            jobStatusEl.innerText = `Job ${jobStatus}`;
            jobStatusEl.style.color = jobStatus === "OK" ? "green" : "red";
        } else {
            logsBox.value = `Error: ${result.message}`;
            jobStatusEl.innerText = "Error";
            jobStatusEl.style.color = "red";
        }
    } catch (error) {
        console.error("Start Error:", error);
        document.getElementById("logs").value = "Error: Could not start job.";
        document.getElementById("jobResultStatus").innerText = "Error";
        document.getElementById("jobResultStatus").style.color = "red";
    }
});
