print("\n\n\t\t\tWorld Of Secrets.....\n\n")
z=1
def Encrypt():    # This function is used to encrypt. 
    word2=raw_input("Enter The String you want to Encrypt \n") #The string to be encrypted.
    word=word2.lower()
    key=int(raw_input("Enter the key \n"))   # key value taken from the user.
    result=''
    for letter in word:                                         # For loop is taken so that each character in the string is checked.
        The_digit=(ord(letter)+key)%122                         # Value + key is used to encrypt.
        if(The_digit==0):                                       # The ascii Value of z is 122 hence % 122 is used.
            The_digit=122
        if(The_digit<96):
            The_digit=The_digit+96
                
        result += chr(The_digit)
    print(result)
    z=1
def Decrypt(): # The Function is used to Decrypt.
    word3=raw_input("Enter The String you want to Decrypt \n")  #The string to be decrypted.
    word1=word3.lower()
    key1=int(raw_input("Enter the key \n"))   # key value taken from the user.
    result1=''
    for letter1 in word1:                       # For loop is taken so that each character in the string is checked.
        The_digit1=(ord(letter1)-key1)%122      # Value + key is used to decrypt.
        if(The_digit1==0):                      # The ascii Value of z is 122 hence % 122 is used.
            The_digit1=122
        if(The_digit1<96):
            The_digit1=The_digit1+26
        else:
            The_digit1=The_digit1
                
        result1 += chr(The_digit1)
    print(result1)
    z=1
while(z):
    ch=raw_input("Enter:\n 1 for encryption.\n 2 for decryption.\n 3 to leave. \n")
    if(ch=='1'):
        Encrypt();
    if(ch=='2'):
        Decrypt();
        
    if(ch=='3'):
        z=0
    continue1= raw_input("Do you want to continue.Y for Yes and N for No: \n")
    if(continue1.lower()=='y'):                             #.lower() function is used so that if user press small y then also the code executes.
        z=1
    if(continue1.lower()=='n'):
        z=0
    
