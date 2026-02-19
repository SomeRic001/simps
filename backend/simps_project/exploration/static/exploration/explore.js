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

    function animateThen(cls,callback){
        card.classList.add(cls);
        card.addEventListener("animationend",callback, {once:true});
    }

    buyBtn.addEventListener("click", () => {
        buyBtn.disabled = true;
        hiddenAmount.value = slider.value;
        animateThen("swipe-right",()=>{
            form.submit();
        });
    });

    skipBtn.addEventListener("click", () => {
        animateThen("swipe-left",()=>{
            window.location.reload();
        });
    });

});