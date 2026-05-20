class DuplicateUserError(Exception):
    pass

class WeakPasswordError(Exception):
    pass

class User:
    user_name=set()
    def  __init__(self,un,mob,pwd):
        self.un=un
        self.mob=mob
        self.pwd=pwd
        self.add_user()
        self.validate()
        
    def add_user(self):
        if self.un in User.user_name:
            raise DuplicateUserError('Username already exists')
        else:
            User.user_name.add(self.un)
            
    def validate(self):
        uc=lc=num=sp=0
        for i in self.pwd:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isdigit():
                num += 1
            else:
                sp += 1
                
        if len(self.pwd)<5 or uc==0 or \
        lc==0 or num==0 or sp==0:
            raise WeakPasswordError('Password not strong enough')
    
def main():
    un=input('Enter Username:')
    mob=int(input('Enter  Mobile :'))
    pwd=input('Enter the  Password:')
    try:
        u1=User(un,mob,pwd)
        u2=User(un,mob,pwd)
    except DuplicateUserError as e:
        print(e)
    except WeakPasswordError as e:
        print(e)
    except:
        print('Hey some issue occurred')
    else:
        print('Account created successfully')

main()