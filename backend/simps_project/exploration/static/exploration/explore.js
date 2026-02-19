document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".amountSlider");
    const amountValue = document.querySelector(".amountValue");
    const buyBtn = document.getElementById("buyBtn");
    const skipBtn = document.getElementById("skipBtn");
    const hiddenAmount = document.getElementById("hiddenAmount");
    const form = document.getElementById("buyForm");
    const card = document.querySelector(".card");


    if (!slider) return;

    slider.addEventListener("input", () => {
        amountValue.textContent = slider.value;
    });

    // Helper function for animations
    function animateThen(cls, callback) {
        const card = document.querySelector(".card"); 
        card.classList.add(cls);
        card.addEventListener("animationend", callback, { once: true });
    }

    buyBtn.addEventListener("click", async () => {
        buyBtn.disabled = true; // Prevent double clicks immediately

        
        animateThen("swipe-right", async () => {
            // Once animation ends, prepare the data
            const formData = new FormData(form);
            formData.set("amount", slider.value);

            try {
                const response = await fetch(form.action, {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-Requested-With": "XMLHttpRequest",
                        // Include the CSRF token for Fetch
                        "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value 
                    }
                });

                if (response.ok) {
                    // If successful, redirect to the next equity
                    window.location.href = "/explore/"; 
                } else {
                    const data = await response.json();
                    
                    // If error, bring the card back and alert
                    const card = document.querySelector(".card");
                    card.classList.remove("swipe-right"); 
                    alert("⚠️ " + (data.error || "Insufficient funds to invest."));
                    buyBtn.disabled = false;
                }
            } catch (error) {
                console.error("Error:", error);
                const card = document.querySelector(".card");
                card.classList.remove("swipe-right");
                alert("An unexpected error occurred.");
                buyBtn.disabled = false;
            }
        });
    });

    skipBtn.addEventListener("click", () => {
        animateThen("swipe-left",()=>{
            window.location.reload();
        });
    });
});