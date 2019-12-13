function ChangeCSS() {
    var checkBox = document.getElementByID("toggle");
    if (checkBox.checked == true) {
        document.getElementById('pagestyle').setAttribute('href', './style/dark.css');
    } else {
        document.getElementById('pagestyle').setAttribute('href', './style/light.css');
    }
}

<
script type = "text/javascript" >
    document.getElementById("myLink").onclick = function() {
        document.getElementById("abc").href = "xyz.php";
        return false;
    }; <
/script>