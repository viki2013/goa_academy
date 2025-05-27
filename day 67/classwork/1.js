 document.getElementById('myForm').addEventListener('submit', function(event) {
      event.preventDefault(); // არ მოხდეს გვერდის გადატვირთვა

      let form = event.target;
      let name = form.name.value;
      let email = form.email.value;
      let password = form.password.value;

      console.log( name);
      console.log( email);
      console.log(password);
    });