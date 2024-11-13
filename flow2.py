import testmail as tst
import mongo as mg
from datetime import *
import logging as lg
d=date(2024,11,23)
rd=datetime.combine(d,datetime.min.time())
dt={"Return Date":rd}
ev=mg.extract(dt)
for i in range(len(ev)):
    tad=ev[i]["email id"]
    nam=ev[i]["name"]
    id=ev[i]["Book Id"]
    t=datetime.now().date()
    sd=datetime.combine(t,datetime.min.time())
    sub="Book Returning Due"
    mesg=f"Book with id {id}, submission is due on {t}"
    try:
        tst.email(tad,mesg,sub,nam)
    except Exception as ex:
        lg.error(f"Failed to send mail...!\n err:{ex}")
