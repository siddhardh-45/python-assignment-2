Studentid= input("Enter the Student Id:")
Emailid= input("Enter the Email id:")
Password= input("Enter the password:")
Referralcode= input("Enter the referral code:")
stu=0
email=0
password=0
referral=0
if Studentid[0:3]=="CSE" and Studentid[3]=='-' and Studentid[4:7].isdigit():
    stu=1
if '@'in Emailid and '.'in Emailid and Emailid[0]!='@' and Emailid[len(Emailid)-1]!='@' and Emailid[-4:]=='.edu':
    email=1
if len(Password)>=8 and 'A'<=Password[0]<='Z' and ( Password.count("0") + Password.count("1") + Password.count("2") + Password.count("3") + Password.count("4") + Password.count("5") + Password.count("6") + Password.count("7") + Password.count("8") + Password.count("9")>=1):
    password=1
if Referralcode[0:3]=="REF" and '0'<=Referralcode[3:5]<='9' and Referralcode[5]=='@':
    referral=1
if stu==1 and password==1 and referral==1 and email==1:
    print("APPROVED")
else :
    print("REJECTED")
