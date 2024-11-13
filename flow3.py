import mongo as mg
import testmail as tst
import logging as lg
#import testmail as tst
from datetime import * 
ussn = input("Enter USN:")
dt = {"USN": ussn}  # Create a dictionary for the USN
ev = mg.extract(dt)  # Pass the dictionary to extract
tad=ev[0]["email id"]
nam=ev[0]["name"]
id=ev[0]["Book Id"]
t=datetime.now()
sub="Book returned to Libarary"
mesg=f"You have submite the book of id {id} on{t} "
try:
    tst.email(tad,mesg,sub,nam)
except Exception as ex:
    lg.error(f"Failed to send mail...!\n err:{ex}")




