document.addEventListener("DOMContentLoaded", () => {
    
    let close_message = document.querySelectorAll(".close")

    close_message.forEach(element => {
        let message = element.parentElement.parentElement;
        element.addEventListener('click', (e) => {
            e.preventDefault();
            message.style.display = 'none';
        });
    });
})