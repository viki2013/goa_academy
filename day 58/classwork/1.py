#საკლასო დავალება: შექმენით names სია სადაც შეინახავთ 10 სახელს.

#შექმენით renewed სია, სადაც დაემატება names სიიდან სახელი თუ მისი სიგრძე ნაკლებია 6-ზე ან იწყება "A" სიმბოლოთი. renewed სია შექმენით list comprehension-ის გამოყენებით

name = ["viki" , "luka" , "nino" , "lizi" , "daviti" , "lika" , "deme" , "arvici" , "arvici"]
renewed = [name for name in name if len(name) < 6 or name.startswith("A")]

print(renewed)

