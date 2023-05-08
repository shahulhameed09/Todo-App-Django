const icon1 = document.getElementById("icon1")
const icon2 = document.getElementById("icon2")
const li = document.querySelector("li")
var complete = document.forms["myForm"].elements[3];


complete.value="Incomplete"
function change(){
        icon2.style.display = "block";
        icon1.style.display = "none";
        complete.value="Completed"
}

function change2(){
        icon1.style.display = "block"
        icon2.style.display = "none"
        complete.value="Incomplete"
}

const radio = document.getElementById("checked")

function check(){
    if(radio.checked = true){
        radio.checked = false
    }
}
