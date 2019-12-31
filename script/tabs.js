document.getElementById("DefaultTab").click(); //tab ouverte par défault

function SwitchTab(evt, tab) {
    let i, tabcontent
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none"; //on cache toutes les balises qui on la classe tabcontent
    }
    document.getElementById(tab).style.display = ""; //on affiche la balise qui à été selectionnée

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    evt.currentTarget.className += " active";
};