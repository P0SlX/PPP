const ScrollBackBouton = document.getElementById("ScrollBack");

window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    /*
    Dès que l'utilisateur va scrol de 80px, le bouton s'affiche.
    */
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        ScrollBackBouton.style.display = "block";
    } else {
        ScrollBackBouton.style.display = "none";
    }
}

function topFunction() {
    /*
    Quand l'utilisateur clique sur le bouton, cela le renvoie vers le haut de la page.
    */
    document.body.scrollTop = 0; // Ligne de code supportée par Safari
    document.documentElement.scrollTop = 0; // Ligne de code supportée par Chrome, Firefox, IE et Opera
}