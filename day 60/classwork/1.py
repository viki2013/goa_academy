def main():
    try:

        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

        result = num1 / num2
        print(result)

    except ValueError:
        print("შეცდომა: გთხოვთ, შეიყვანეთ სწორი რიცხვები.")

    except ZeroDivisionError:
        print("შეცდომა: ნულზე გაყოფა დაუშვებელია.")

    except:
        print("მოულოდნელი შეცდომა:")

