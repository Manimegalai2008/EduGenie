const task = document.getElementById("task");
const inputText = document.getElementById("inputText");
const submitBtn = document.getElementById("submitBtn");
const result = document.getElementById("result");
const loading = document.getElementById("loading");

submitBtn.addEventListener("click", async () => {
    const selectedTask = task.value;
    const text = inputText.value.trim();

    if (!text) {
        result.textContent = "Please enter a question or topic.";
        return;
    }

    loading.classList.remove("hidden");
    result.textContent = "";
    submitBtn.disabled = true;

    try {
        let endpoint = "";

        if (selectedTask === "qa") {
            endpoint = "/qa";
        } else if (selectedTask === "explain") {
            endpoint = "/explain";
        } else if (selectedTask === "quiz") {
            endpoint = "/quiz";
        } else if (selectedTask === "summarize") {
            endpoint = "/summarize";
        } else if (selectedTask === "recommend") {
            endpoint = "/learn/recommendations";
        }

        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                question: text,
                topic: text
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        result.textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        result.textContent = "Error: " + error.message;
    } finally {
        loading.classList.add("hidden");
        submitBtn.disabled = false;
    }
});