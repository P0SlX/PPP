function ChangeCSS(){
  /*
  Cette fonction change le lien href de la page html quand elle est appelée.
  */
  var checkBox = document.getElementById('toggle'); //le bouton
  var link = document.getElementById('pagestyle'); //la balise link
  if (checkBox.checked == true){ //si le bouton est checké
    link.href='./style/dark.css'; //href prend la page de style './style/dark.css'
  }
  else { //sinon
      link.href='./style/light.css'; //href prend la page de style './style/light.css'
  }
}