def check_multiple (number):
    if number % 3 == 0 and number % 5 ==0:
         return True
    else:
         return False

def check_password(password):
     secret_word = "Python123"
     if password==secret_word:
          return "access granted"
     else:
          return "access denied"


def calculate_federal_tax(salary):
    if salary <=11000:
         return salary*0.10
    elif salary <=44725:
         return salary*0.12
    elif salary<=95375:
         return salary*0.22
    else:
         return salary*0.24