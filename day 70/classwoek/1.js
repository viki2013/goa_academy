function changeColor() {
    let color = prompt("შეიყვანე ფერი:");
    document.getElementById("colorButton").style.backgroundColor = color;
}


 function checkLogin() {
    let value = document.getElementById("loginInput").value;
    if (value === "true") {
      alert("logged in");
    } else {
      alert("try again");
    }
 }


 function changeColors() {
    document.body.style.color = document.getElementById("textColor").value;
    document.body.style.backgroundColor = document.getElementById("bgColor").value;
  }