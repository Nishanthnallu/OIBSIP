import random
import string

password_length=int(input("Enter your password length : "))
print("CHOICE LIST \n 1.Alphabets \n 2.Symbols \n 3.Numbers \n 4.All the characters")
choice = int(input("Enter your choice :"))

random_password = " "

for i in range(password_length ):

    if choice == 1:
        random_password += random.choice(string.ascii_letters)
        

    elif choice == 2:
        random_password += random.choice(string.punctuation)
        

    elif choice == 3:
        random_password += random.choice(string.digits)
        

    elif choice == 4:
        random_password += random.choice(string.ascii_letters + string.punctuation + string.digits)
        
    
    else:
        print("Enter a valid choice")

print("Random_Password = ",random_password)