# 2) დაბეჭდე შენი სახელი
print("ვიქტორია სიხარულიძე")# ან ვიკი სიხარულიძე
#print  ბრძანებით ვბეჭდავთ ვიქტორია სიხარულიძეს 

# 3) დაბეჭდე საყვარელი ციტატა ბრჭყალებით
print('"მადლი ქენი გზაზე დადე გაიარე წინ დაგხვდება"') #ქართულში ვისწავლე საყვარელი არაა მარა საინტერესოა
# ახსნა : გააკეთე სიკეთე და ის უკან დაგიბრუნდება

# 4) დაბეჭდე რამდენიმე ხაზი
print("პირველი და განუმერებელი (buhehe)")# პირველი ხაზი რომელიც არ ვიცი რატო დავწერე პირველი და განუმეორებელი
print("მეორე როგორც ჩანს დაგვჭირდა") # პირველი განუმეორებელი არ ყოფილა ამიტომ მეორეც ავიღე
print("ბოლო და უკანასკნელი ჯერჯერობი")# ჯერჯერობით მესამე და ბოლო

# 5) დაბეჭდე მარტივი მათემატიკური მოქმედება
print(437725-823882+765234236738*453)# ძაან მარტივია 
#765234236738 უნდა * 453 შემდეგ დავუმატოთ 823882 და ბოლოს მიღებულს გამოვაკლოთ 437725

# 6) დაბეჭდე ფიგურა სიმბოლოებით #
print("###") # სამი ცალი დიეზი
print("###") # სამი ცალი დიეზი
print("###") # სამი ცალი დიეზი
print("###") # სამი ცალი დიეზი

# 7) სტრინგის კონვერტაცია მთელ რიცხვად
num = "42" # რადგან 42 არის ე.წ პრწყალებში ის არის სტრინგი და მას ჩვენ int ბრძანებუს საშუალებით ვაქცევთ ინტეჯერად
num= int(num) # ინტეჯერად გადაქცევა
print(num) # დავპრინტოთ 42 ე.წ პრჭყალებუს გარეშე

# 8) ორი ათწილადი რიცხვის დამატება
num1 = 13.5 # პირველი ათწილადი
num2= 2.5 # მეორე ათწილადი
print(num1 + num2) # 13.5 და 2.5 ის დამატება შემდეგ კი მათი ჯამის დაპრინტვა

# 9) ორი სტრინგის შეერთება
str1 = "Hello" # პირველი სტრინგი
str2 = "World" #მეორე სტრინგი
print(str1 + " " + str2 + " . ") #hello უნდა დავუმატოთ space შემდეგ world ბოლოს კი . ამ ყველაფრის შემდეგ ვბეჭდავთ მას

# 10) მონაცემთა ტიპების დაბეჭდვა
nim1 = 10        # ეს არის ინტეჯერი
nim2 = "Python"  # ეს არის სტრინგი
nim3 = 3.14      # fეს კი არის ათწილადი

print(type(nim1)) # ვადგენთ რა ტიპია nim1
print(type(nim2)) # ვადგენთ რა ტიპია nim2
print(type(nim3)) # ვადგენთ რა ტიპია nim3

# 11) მომხმარებლის შეყვანა და ტიპის შეცვლა
vikis_input = input("შეიყვანე რიცხვი: ")  #ამით მომხმარებელს ვეუბნებით რომ შემოიტანოს რიცხვი
boss = int(vikis_input) # ამით vikis_input - ს ვაქცევთ ინტეჯერად
print(boss) #ვპრინტავთ boss ცვლადს 
print(type(boss)) #ბოლოს ვადგენთ მის ტიპს

# 12) კითხე სახელი და მიესალმე
question_from_viki = input("რა გქვია? ") #ვეკითხებით მის სახელს input ბრძანების საშუალებით
print("გამარჯობა," + " "  + question_from_viki + "!")
 #ამით კი ვბეწდავთ გამარჯობას , space  შემდეგ კი როგორ ხარ და ძახილის ნიშანს

# 13) კითხე ასაკი და გამოიანგარიშე შემდეგი წლის ასაკი
question2_from_viki = int(input("რამდენი წლის ხარ? "))#ამით მომხმარებელს ვეკითხებით თუ რამდენი წლისაა
print("შემდეგ წელს იქნები", question2_from_viki  + 1, "წელი.") #შემდეგ კი ვიანგარიშებთ თუ რამდენი წლის იქნება 1 წელში.

# 14) მარტივი კალკულატორი (დამატება)
um1 = int(input("შეიყვანე პირველი რიცხვი: ")) #სტრინგს ვაქცევთ ინტეჯერად შემდეგ კი მომხმარებელს ვთხოვთ შემოიტანოს პირველი რიცხვი
um2 = int(input("შეიყვანე მეორე რიცხვი: ")) # სტრინგს ვაქცევთ ინტეჯერად მერე მომხმარებელს ვთხოვთ შემოიტანოს მეორე რიცხვი
print( um1 + um2) #ბოლოს კი მის მიერ შემოტანილ რიცხვებს ვუმატებთ ერთმანეთ მაგ: um1 = 2  ხოლო ,  um2 = 8   , 8 + 2 =  10

# 15) საყვარელი ფერი
vikis_fav_color = input("რა არის შენი საყვარელი ფერი? ") #მომხმარებელს ვეკითხებით რა არის მისი საყვარელი ფერი
print("შენი საყვარელი ფერია " + vikis_fav_color + "!")# შეკითხვის შემდეგ ვადგენთ წინადადებას მაგ: შენი საყვარელი ფერია წითელი!

# 16) შეამოწმე სიმაღლე
height = int(input("შეიყვანე სიმაღლე (სმ): "))#ის მომხმარებელს ეუბნება რო შემოიტანოს მისი სიმაღლე სანტიმეტრებით 
if height > 150: # თუ სიმაღლე მეტია 150 სმ - ზე
    print("შენ ხარ მაღალი!") # ის არის მაღალი
else:#სხვა შემთხვევაში 
    print("შენ ხარ 150 სმ-ზე დაბალი ან ზუსტად ამდენი.")#მისი სიმაღლე არის 150 ზე პატარა ან ზუსტად 150 

# 17) ბეჭდავს რიცხვებს 1-დან 5-ის ჩათვლით
for i in range(1, 6): #ვადგენ დიაპაზონს 1 დან 6 ამდე
    print(i) #ვბეჭდავთ დიაპაზონს

# 18) ბეჭდავს სიტყვა "Python"-ის თითოეულ ასოს ცალ-ცალკე ხაზზე
text = "Python" # სტრინგი
for letter in text: #ვწერთ კოდს იმისთვის რომ "Python" დავყოთ ცალ - ცალკე ასოებად
    print(letter)#ბოლოს კი ვბეჭდავთ მას

# 19) ითვლის რიცხვების 1-დან 10-ის ჩათვლით ჯამს
total = 0 # ინტეჯერი
for i in range(1, 11): #ვადგენთ დიაპაზონს 1 იდან 10 ის ჩათვლით 
    total += i #თუ ინტეჯერი მეტია ან ტოლია i 
print( total) #ვბეჭდავთ ინტეჯერი

# 20) ბეჭდავს 2-ის გამრავლების ტაბულას 1-დან 5-მდე
for i in range(1, 5): # ვადგენთ დიაპაზონს 1 იდან 5 ამდე
    print("2 x = 2 * i ")# ვბეჭდავთ  2 * i  საინტერაციო ცვლადზე

# 21) ბეჭდავს ყველა ლუწ რიცხვს 2-დან 20-ის ჩათვლით
for i in range(2, 21, 2): #ვადგენთ ყველა ლუწ რიცხვს 2-დან 20-ის ჩათვლით
    print(i) # შემდეგ კი ვბეჭდავთ მას 

# 22) ბეჭდავს რიცხვებს 1-დან 5-მდე while ციკლის გამოყენებით
i = 1  # ინტეჯერი
while i <= 5:  # while ციკლი მიმდინარეობს, სანამ i 5-ს არ გაუტოლდება ან მეტიარ  გახდება
    print(i)  # თითოეულ გაშვებაზე ბეჭდავს i-ს მნიშვნელობას
    i += 1  # i-ს მნიშვნელობა იზრდება 1-ით 


# 23) ითვლის რიცხვების 1-დან 5-მდე ჯამს while ციკლით
i = 1  #ინტეჯერი
total = 0  # ინტეჯერი
while i <= 5:  # while ციკლი მიდის, სანამ i-ს მნიშვნელობა 5-ს არ გაუტოლდება
    total += i  # total-ს ემატება i
    i += 1  # i-ს მნიშვნელობა იზრდება 1-ით
print(total)  # ბეჭდავს ჯამს


# 24) ბეჭდავს რიცხვებს 10-დან 1-მდე უკუღმა
i = 10  # ინტეჯერი
while i >= 1:  # while ციკლი გაგრძელდება, სანამ i 1-ზე ნაკლები არ გახდება
    print(i)  # ბეჭდავს i-ს მნიშვნელობას
    i -= 1  # i-ს მნიშვნელობა მცირდება 1-ით

# 25) ბეჭდავს ყველა კენტ რიცხვს 1-დან 10-მდე
i = 1  # ინტეჯერი
while i <= 10:  # while ციკლი მიდის, სანამ i 10-ს არ გაუტოლდება
    if i % 2 != 0:  # თუ i-ს დანარჩენი გამყოფი 2-თან არ არის კენტი
        print(i)  # ბეჭდავს კენტ რიცხვს
    i += 1  # i-ს მნიშვნელობა იზრდება 1-ით

# 26) სთხოვს მომხმარებელს შეიყვანოს ტექსტი სანამ არ დაწერს "exit"
user_input = ""  # ცვლადი user_input იწყება ცარიელი სტრიქონით
while user_input.lower() != "exit":  # while ციკლი მუშაობს, სანამ მომხმარებელი "exit"-ს არ ჩაწერს
    user_input = input("შეიყვანე ტექსტი: ")  # სთხოვს მომხმარებელს ტექსტის შეყვანას
print("პროგრამა დასრულდა.")  # თუ "exit" აირჩია, გამოაქვს ეს შეტყობინებავო

# 27) ბეჭდავს ყველა ელემენტს სიიდან
my_list = ["apple", "banana", "cherry"]  # lista შედგება 3 ელემენტისგან
for item in my_list:  # ციკლი გადაუვლის  სიაში თითოეული ელემენტს
    print(item)  # ბეჭდავს თითოეულ ელემენტს

# 28) სიაში ელემენტების სიდიდის გამოტანა
my_list = ["apple", "banana", "cherry"]
print(len(my_list))  # len() ფუნქცია აბრუნებს სიაში ელემენტების რაოდენობას

# 29) კონკრეტული ელემენტის წვდომა სიიდან
my_list = [10, 20, 30, 40, 50]  # სიაში 5 რიცხვია
print( my_list[1])  # სიაში მეორე ელემენტს იქნება 20


# 30) ახალი ელემენტის დამატება სიაში
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")  # append() ფუნქცია გვამატებს ახალ ელემენტს სიას ბოლოს
print(my_list)  # ბეჭდავს სიას ახალ ელემენტთან ერთად

# 31) ელემენტის წაშლა სიიდან
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")  # remove() წაშლის პირველი "banana"-ს სიიდან
print(my_list)  # ბეჭდავს სიას წაშლილი ელემენტით

# 37) ფუნქცია, რომელიც აჩვენებს მისალმებას მომხმარებლისთვის
def greet_user(name):
    # ბეჭდავს მისალმებას მომხმარებლის სახელით
    print(name)

# 38) ფუნქცია ორი რიცხვის დასამატებლად
def add_numbers(a, b):
    # აბრუნებს ორი რიცხვის ჯამს
    return a + b

# 39) ფუნქცია ამოწმებს, ლუწია თუ კენტი რიცხვი
def check_even_odd(number):
    # თუ რიცხვი ლუწია
    if number % 2 == 0:
        return "Even"  # ლუწი
    else:
        return "Odd"  # კენტი

# 40) ფუნქცია მართკუთხედის ფართობის გამოსათვლელად
def area(length, width):
    # აბრუნებს ფართობს: სიგრძე * სიგანე
    return length * width

# 41) ფუნქცია სტრიქონის შებრუნებისთვის
def reverse_string(text):
    # აბრუნებს ტექსტის შებრუნებულ ვერსიას
    return text[::-1]

# 42) ტუპლის შექმნა და დაბეჭდვა
my_tuple = (10, "hello", 3.14)  # ტუპლი შეიცავს მთელ რიცხვს, სტრიქონს და ათწილადს
print(my_tuple)  # ბეჭდავს მთელ ტუპლს

# 43) ტუპლიდან კონკრეტული ელემენტის მიღება
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # ინდექსი 1 არის "banana"

# 44) ტუპლის სიგრძის პოვნა
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # len() აბრუნებს ელემენტების რაოდენობას

# 45) ორი ტუპლის გაერთიანება
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
vk = tuple1 + tuple2  # + ოპერატორით ტუპლები ერთდება
print(vk)

# 46) ტუპლში კონკრეტული ელემენტის შემოწმება
my_tuple = ("apple", "banana", "cherry")
if "banana" in my_tuple:  # თუ "banana" არის ტუპლში
    print("Found")#დაიბეჭდოს პოვნა
else:#სხვა შემთხვევაში
    print("Not found")#დაიბეჭდოს არ პოვნა

# 47) სეტის (set) შექმნა და დაბეჭდვა
my_set = {1, "hello", 3.14}  # სეტი შეიცავს მთელ რიცხვს, სტრიქონს და ათწილადს
print(my_set)  # ბეჭდავს სეტს — ელემენტები შესაძლოა არ იყოს რიგში

# 48) ელემენტის არსებობის შემოწმება სეტში
my_set = {"apple", "banana", "cherry"}
if "banana" in my_set:  # თუ "banana" არის სეტში
    print("Yes")  # მოიძებნა
else:#სხვა შემთხვევაში
    print("No")  # არ მოიძებნა

# 49) ელემენტის დამატება სეტში
my_set = {1, 2, 3}
my_set.add(4)  # add() მეთოდი ამატებს ახალ ელემენტს სეტში
print( my_set)#პრინტავს განახლებულ სეტს

# 50) ელემენტის წაშლა სეტიდან
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")  # remove() წაშლის მითითებულ ელემენტს
print( my_set)#პრინტავს განახლებულ სეტს

# 51) ორი სეტის გაერთიანება (union)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set = set1 | set2  # | ოპერატორი გამოიყენება ორი სეტის გაერთიანებისთვის
print(set)

# 52) ლექსიკონის (dictionary) შექმნა და დაბეჭდვა
person = {
    "name": "vikvi", # name არის key, "vikvi" არის value
    "age": 11 # age არის key, 11 არის value
}
print(person)  # ბეჭდავს მთლიან ლექსიკონს

# 53) მნიშვნელობის წვდომა key-ით
person = {
    "name": "viktoria",
    "age": 12
}
print(person["name"])  # წვდომა "name" key-ის მნიშვნელობაზე


# 54) ახალი key-value წყვილის დამატება ლექსიკონში
person = {
    "name": "vikitoria",
    "age": 10
}
person["city"] = "Tbilisi"  # ახალ key-ს "city" ვამატებთ შესაბამისი მნიშვნელობით
print( person)# ბეჭდავს მთლიან განახლებულ ლექსიკონს





