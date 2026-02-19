document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".amountSlider");
    const amountValue = document.querySelector(".amountValue");
    const buyBtn = document.getElementById("buyBtn");
    const skipBtn = document.getElementById("skipBtn");
    const hiddenAmount = document.getElementById("hiddenAmount");
    const form = document.getElementById("buyForm");

    if (!slider) return;

    slider.addEventListener("input", () => {
        amountValue.textContent = slider.value;
    });

    buyBtn.addEventListener("click", async () => {
        // Prepare form data
        const formData = new FormData(form);
        formData.set("amount", slider.value);

        try {
            buyBtn.disabled = true; // Prevent double clicks
            
            const response = await fetch(form.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest", // Tells Django this is an AJAX request
                }
            });

            if (response.ok) {
                // If successful, reload to show the next equity
                window.location.href = "{% url 'explore:home' %}"; 
            } else {
                const data = await response.json();
                alert("⚠️ " + (data.error || "Insufficient funds to invest."));
                buyBtn.disabled = false;
            }
        } catch (error) {
            console.error("Error:", error);
            alert("An unexpected error occurred.");
            buyBtn.disabled = false;
        }
    });

    skipBtn.addEventListener("click", () => {
        window.location.reload();
    });
});