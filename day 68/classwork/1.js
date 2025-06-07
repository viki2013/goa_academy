// 1
function logicalFunc(bool1, bool2) {
  console.log( bool1 && bool2); // && ნიშნავს "და"
  console.log(bool1 || bool2);  // || ნიშნავს "ან"
}

// ფუნქციის გამოძახება 3-ჯერ სხვადასხვა არგუმენტით
logicalFunc(true, true);
logicalFunc(true, false);
logicalFunc(false, false);

//2
function typeConvert() {
  let userInput = prompt("შეიყვანე რიცხვი:");  
  console.log( userInput);
  console.log(typeof userInput);

  let convertedNumber = Number(userInput);   
  console.log(convertedNumber);
  console.log(typeof convertedNumber);
}

// ფუნქციის გამოძახება
typeConvert();

//3
function forConditions() {
    let userNum = Number(prompt("Enter number:"));

    if (userNum >= 0 && userNum < 18) {
        console.log("not adult");
    } else if (userNum >= 18 && userNum < 65) {
        console.log("adult & not old");
    } else if (userNum >= 65 && userNum <= 113) {
        console.log("retired");
    } else if (userNum > 113) {
        console.log("lie");
    } else {
        console.log("invalid input"); 
    }
}
