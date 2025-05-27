let student = {
  name: "გიორგი",
  surname: "აბაშიძე",
  academy: "თეთრი აკადემია",
  role: "მოსწავლე",
  city: "თბილისი",
  favColor: "ლურჯი",
  favLanguage: "JavaScript",
  
  sayHello: function() {
    console.log("Hello");
  },

  showProperty: function(propertyName) {
    console.log(this[propertyName]);
  }
};

// 1. დაბეჭდეთ მთლიანი ობიექტი
console.log(student);

// 2. დაბეჭდეთ ობიექტის რომელიმე კუთვნილების მნიშვნელობა
console.log(student.city);

// 3. ობიექტის რომელიმე კუთვნილებას შეუცვალეთ მნიშვნელობა და დაბეჭდეთ განახლებული მნიშვნელობა
student.city = "ბათუმი";
console.log(student.city);

// 4. გამოიძახეთ ობიექტის რომელიმე მეთოდი
student.sayHello();
student.showProperty("favLanguage");
