import re

class EmailSlicer:
    def __init__(self,mailid:str):
        self._mailid = mailid
        
    @property
    def mailid(self):
        return self._mailid 
    @mailid.setter
    def mailid(self,value):
        self._mailid = value
        
    def mail_validator(self) -> bool:
        try:
            valid_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'                    
            return re.match(valid_pattern,self._mailid) is not None
        except Exception as e:
            raise UnboundLocalError(f"Unknown Error : {e}")
            
    def slicer(self)->None:
        try:
            (username,domain) = self._mailid.split('@')            
            twoparts = domain.split(".")    
            domain = twoparts[0]
            extension = ".".join(twoparts[1:])
            
            print(f"Username = {username}")
            print(f"Domain = {domain}")
            print(f"Extension = {extension}")
        except Exception as e:
            raise ValueError(f'Error  : {e}')
                                
                    
if __name__ ==  "__main__":
    print("............Email Summary..............")
    formailvalidator = input(" Provide Email Address : ")
    mail = EmailSlicer(formailvalidator)

    while True:
        print('\n')
        print('1. Email Validator')
        print("2. Email Slicer")
        print("3. Email Slicer and Validator")
        print("4. Exit")
        print('\n')
        
        choice  =  input("apply your choice (1-4): ")
    
        if choice == '1':
            print("Valid Email" if mail.mail_validator() else "Invalid Email")
        elif choice == "2":
            mail.slicer()
        elif choice == '3':
            print("Valid Email" if mail.mail_validator() else "Invalid Email")
            print('\n')
            mail.slicer()
        elif choice == '4':
            print('Exit ..')
            break
        else:
            print("Please enter a valid input!")
        
            
            
    
    
    