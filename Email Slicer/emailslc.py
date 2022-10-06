#collect email from the user
#split the mail using the @, the first part as username,the second part as the saved domain name
#split domain using ..

def main():
    print("Welcome to email Slicer")
    print("")
    
    email_input=input("Enter your Mail id:")
    
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")
    
    print("Username:",username)
    print("Domain:",domain)
    print("Extension:",extension)
    
main()