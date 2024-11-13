#SRY for bad grammer// lending book processes 
from datetime import datetime, timedelta
import mongo as mg
import testmail as tstm

na = input("Name: ")
usn = input("USN: ")
bkid = input("Book id: ")
eid=input("Email id:")
s = datetime.now().date()  
sd=datetime.combine(s,datetime.min.time())
ld = sd + timedelta(days=14)

print("Date: ", sd)
print("Date2:", ld)

dat = {
    "name": na,
    "USN": usn,
    "Book Id": bkid,
    "email id": eid,
    "Submission Date": sd,  
    "Return Date": ld      
}
try:
    mg.insert(dat)
except Exception as e:
    print("coudn't insert data the data to database")
else:
    print("Data added to database Scussfully")
msg=f"""You Have borrowed a book with id {bkid} from Library.

Last Date to return The Book is {ld}
Enjoy Reading,
Thank You
""" 
subject="Borrowed Book"
try:
    tstm.email(eid,msg,subject,na)
except Exception as e:
    print("Error in sending mail",e)
else:
    print("Mail sent scussfully...!")
