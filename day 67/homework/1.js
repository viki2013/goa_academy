
    // 1. Create an empty object
    let emptyObject = {};
    console.log("1. ცარიელი ობიექტი:", emptyObject);

    // 2. Create an object with your name, age, and city
    let person = {
      name: "ვიკი",
      age: 11,
      city: "Tbilisi"
    };
    console.log(person);

    // 3. Access the value of a property in an object
    console.log( person.name);

    // 4. Add a new property to an existing object
    person.country = "Georgia";
    console.log( person);

    // 5. Create a nested object (object inside object)
    let user = {
      username: "viki123",
      info: {
        name: "viki",
        age: 11,
        city: "Tbilisi"
      }
    };
    console.log( user);

    // 6. Change the value of an existing property in an object
    person.age = 26;
    console.log( person.age);
