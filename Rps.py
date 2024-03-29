import random
import string

# length= int (input("Enter lenght :"))
# chars = string.ascii_letters
# chars  += string.digits
# chars += string.punctuation

# password = ''.join([random.choice(chars) for i in range(length)])
# print("Your Random Password is :" , password)


# code with harry
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase
    
    
    s3 = string.digits


    s4 = string.punctuation

    pl= int(input("Enter the Password length :\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("Your  random gentered Password")
    print("".join(random.sample(s , pl)))
