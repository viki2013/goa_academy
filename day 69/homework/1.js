// 2) Even or Odd
let num = Number(prompt("2) Enter a number (Even or Odd):"));
if (num % 2 === 0) {
  console.log("2) Even");
} else {
  console.log("2) Odd");
}

// 3) Grade Assignment
let score = Number(prompt("3) Enter your score (Grade A–F):"));
if (score >= 90) console.log("3) Grade A");
else if (score >= 80) console.log("3) Grade B");
else if (score >= 70) console.log("3) Grade C");
else if (score >= 60) console.log("3) Grade D");
else console.log("3) Fail");

// 4) Largest of Three Numbers
let a = Number(prompt("4) Enter first number:"));
let b = Number(prompt("4) Enter second number:"));
let c = Number(prompt("4) Enter third number:"));

if (a === b && b === c) {
  console.log("4) All numbers are equal");
} else if (a >= b && a >= c) {
  console.log("4) Largest is: " + a);
} else if (b >= a && b >= c) {
  console.log("4) Largest is: " + b);
} else {
  console.log("4) Largest is: " + c);
}

// 5) Vowel or Consonant
let ch = prompt("5) Enter a letter (a-z):").toLowerCase();
if ("aeiou".includes(ch)) {
  console.log("5) Vowel");
} else {
  console.log("5) Consonant");
}

// 6) Divisible by 3 and 5
let n = Number(prompt("6) Enter a number (divisible by 3/5?):"));
if (n % 3 === 0 && n % 5 === 0) console.log("6) Divisible by both 3 and 5");
else if (n % 3 === 0) console.log("6) Divisible by 3 only");
else if (n % 5 === 0) console.log("6) Divisible by 5 only");
else console.log("6) Not divisible by 3 or 5");

// 7) Age Category
let age = Number(prompt("7) Enter your age (age group):"));
if (age >= 0 && age <= 12) console.log("7) You are a Child");
else if (age <= 19) console.log("7) You are a Teenager");
else if (age <= 59) console.log("7) You are an Adult");
else console.log("7) You are a Senior");
