

 

    // Task 1: Favorite Hobby
    let hobby = prompt("What is your favorite hobby?");
    alert("Your favorite hobby is: " + hobby);

    // Task 2: Full Name
    let  firstName = prompt("Enter your first name:");
    let lastName = prompt("Enter your last name:");
    let fullName = firstName + " " + lastName;
    alert("Your full name is: " + fullName);

    // Task 3: Update <p> with message
    let userMessage = prompt("Enter a message to display on the page:");
    document.getElementById("messageParagraph").textContent = userMessage;

    // Task 4: Favorite Emoji
    let emoji = prompt("What is your favorite emoji?");
    alert("Thanks! Your favorite emoji is: " + emoji);

    // Task 5: Change page title
    let newTitle = prompt("Enter a word to set as the page title:");
    document.title = newTitle;

    // Task 6: Form input alert
    function showTextInput() {
      let text = document.getElementById("textInput").value;
      alert("You entered: " + text);
    }

    // Task 7: Background color change
    document.getElementById("colorForm").addEventListener( function(e) {
      e.preventDefault();
      let color = document.getElementById("colorInput").value;
      document.body.style.backgroundColor = color;
    });
  
