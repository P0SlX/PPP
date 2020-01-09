function ChangeCSS() {
    /*
    Cette fonction change le lien href de la page html quand elle est appelée.
    */
    let checkBox = document.getElementById('toggle');
    let link = document.getElementById('pagestyle');
    if (checkBox.checked) { //si le bouton est checké
        link.href = './style/dark.css'; //href prend la page de style './style/dark.css'
    } else { //sinon
        link.href = './style/light.css'; //href prend la page de style './style/light.css'
    }
};