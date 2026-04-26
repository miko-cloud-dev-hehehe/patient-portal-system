document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".toast-message");
    messages.forEach((message, index) => {
        setTimeout(() => {
            message.style.opacity = "0";
            message.style.transition = "all 0.3s ease";
            setTimeout(() => message.remove(), 300);
        }, 3200 + (index * 250));
    });
});
