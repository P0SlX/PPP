function ChangeCSS(){
  var checkBox = document.getElementById('toggle');
  var link = document.getElementById('pagestyle');
  if (checkBox.checked == true){
    link.href='./style/dark.css';
    console.log('oui');
  }
  else { 
      link.href='./style/light.css';
  }
}