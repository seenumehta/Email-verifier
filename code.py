email = input("Enter your Email ID: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():  # Check if the email starts with an alphabet
        # Check "@" in email only once
        if ("@" in email) and (email.count("@") == 1):
            # "." appears only at the third or fourth position from the end
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Invalid email ID 5")
                else:
                    print("Valid email ID")
            else:
                print("Invalid email ID 4")
        else:
            print("Invalid email ID 3")
    else:
        print("Invalid email ID 2")
else:
    print("Invalid email ID 1")


