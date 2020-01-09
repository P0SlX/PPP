const toggler = document.getElementsByClassName("menu_deroulant");
let i;

for (i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener("click", function() {
        this.parentElement.querySelector(".imbrication").classList.toggle("imbrication_active");
        this.classList.toggle("menu_deroulant_bas");
    });
};