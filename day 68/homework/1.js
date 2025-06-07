//2
let a = Number(prompt("Enter first number:"));
let b = Number(prompt("Enter second number:"));

if (a > 10 && b > 10) {
    console.log("Both numbers are greater than 10.");
} else {
    console.log("At least one number is not greater than 10.");
}

//3
let nu = Number(prompt("Enter age:"));
let viki = confirm("Do you have permission?");

if (nu >= 18 || viki) {
    console.log("Access granted.");
} else {
    console.log("Access denied.");
}


//4
let isSunny = true;
let isNotSunny = !isSunny;

console.log(isSunny); // true
console.log( isNotSunny); // false

//5
let score = Number(prompt("Enter your score (0–100):"));

if ((score >= 50 && score <= 100) || score === 0) {
    console.log("Valid score: Passed or zero.");
} else {
    console.log("Invalid or failing score.");
}

//6
let num = 123;
let strNum = String(num);

console.log( strNum);         // "123"
console.log(typeof strNum);       // string


//7
let boolVal = true;
let strBool = String(boolVal);

console.log( strBool);        // "true"
console.log( typeof strBool);      // string

//8
let str = "456";
let convertedNum = Number(str);

console.log("Converted:", convertedNum);   // 456
console.log("Type:", typeof convertedNum); // number


//9
let boolTrue = true;
let boolFalse = false;

console.log("true →", Number(boolTrue));   // 1
console.log("false →", Number(boolFalse)); // 0


//10
let nonNumeric = "hello";
let result = Number(nonNumeric);

console.log("Converted:", result);         // NaN (Not a Number)
console.log("Type:", typeof result);       // number



//11
let number = Number(prompt("Enter a number:"));

if (number > 0) {
    console.log("The number is positive.");
} else if (number < 0) {
    console.log("The number is negative.");
} else {
    console.log("The number is zero.");
}


//12
let age = Number(prompt("Enter your age:"));

if (age >= 18) {
    console.log("You can vote!");
} else {
    console.log("You are not eligible to vote.");
}

//13
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));

if (num1 > num2) {
    console.log(num1 + " is greater than " + num2);
} else if (num2 > num1) {
    console.log(num2 + " is greater than " + num1);
} else {
    console.log("Both numbers are equal.");
}





