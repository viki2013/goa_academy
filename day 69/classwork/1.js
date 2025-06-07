function usingWhileLoop() {
  let i = 0;
  while (i < 100) {
    console.log(i);
    i++;
  }
}

function usingWhileLoop() {
  let i = 0;
  while (i < 100) {
    console.log(i);
    i++;
  }
}

function correctUserPassword() {
  const correctPassword = "12345"; // სწორ პაროლი
  let userInput;
  let attempts = 0;

  do {
    userInput = prompt("შეიყვანეთ პაროლი:");
    attempts++;
  } while (userInput !== correctPassword);

  console.log("correct guess");
  console.log(`ცდაების რაოდენობა: `);
}


