document.getElementById("browse-btn").addEventListener("click", async () => {
    const directory = prompt("Enter the directory path:");
    if (directory) {
        document.getElementById("directory-path").value = directory;
    }
});

document.getElementById("organizer-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const directoryPath = document.getElementById("directory-path").value;
    if (!directoryPath) {
        alert("Please select a directory.");
        return;
    }

    try {
        const response = await fetch("/organize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ directory: directoryPath })
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById("status").textContent = result.success;
            document.getElementById("status").style.color = "green";
        } else {
            document.getElementById("status").textContent = result.error;
            document.getElementById("status").style.color = "red";
        }
    } catch (error) {
        document.getElementById("status").textContent = "An unexpected error occurred.";
        document.getElementById("status").style.color = "red";
    }
});
