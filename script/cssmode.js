function ChangeCSS(){
  var checkBox = document.getElementById('toggle');
  var link = document.getElementById('pagestyle');
  if (checkBox.checked == true){
    link.href='./style/dark.css';
  }
  else { 
      link.href='./style/light.css';
  }
}
