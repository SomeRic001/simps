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

    buyBtn.addEventListener("click", () => {
        buyBtn.disabled = true;
        hiddenAmount.value = slider.value;
        form.submit();
    });

    skipBtn.addEventListener("click", () => {
        window.location.reload();
    });

});