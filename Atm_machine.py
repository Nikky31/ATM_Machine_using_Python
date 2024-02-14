import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='1234',database='  ATM_MACHINE')
c1=conn.cursor()
print("================================================================================")

print("                       WELCOME TO OUR ATM ")

print("================================================================================")

print("1.To create account")
print("2.To login")
print("3.Exit")
print("================================================================================")

op=int(input("Enter your choice :"))
print("================================================================================")








f op==1:
      c="y"
      while c=="y":
            m=int(input("Enter a 4 digit number as accont number:"))
            cb="select * from records where ACCONT_NO={}".format(m)
            c1.execute(cb)
            d=c1.fetchall()
            data=c1.rowcount
            if data==1:
                  print("================================================================================")

                  print("This account number already exists:")
                  c=input("Do you want to continue y/n -")
                  print("================================================================================")

                  if c=="y":
                        continue
                  else:
                        print("                    Thank you.")
                        print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        print("Visit again")
                        print("================================================================================")
                   

          






else:
                  name=input("Enter your name:")
                  passw=int(input("Enter your pass word:"))
                  ab="insert into records(ACCONT_NO,PASSWORD,NAME) values({},{},'{}')".format(m,passw,name)
                  print("================================================================================")

                  c1.execute(ab)
                  conn.commit()
                  print("Account sucessfully created")
                  print("The minimum balance is 1000 ")
                  print("================================================================================") 

                  s=int(input("Enter the money to be deposited :"))
                  print("================================================================================")

                  sr="update records set  CR_AMT={} where ACCONT_NO={}".format(s,m)
                  c1.execute(sr)
                  conn.commit()
                  ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(m)
                  c1.execute(ef)
                  conn.commit()
                  print("sucessfully deposited")

                  print("                    Thank you")
                  print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                  print("Visit again")
                  Break
if op==2:
      y="y"
      while y=="y":
            
            acct=int(input("Enter your account number:"))
            cb="select * from records where ACCONT_NO={}".format(acct)
            c1.execute(cb)
            c1.fetchall()
            data=c1.rowcount
            if data==1:
                  pas=int(input("Enter your password  :"))
                  print("================================================================================")

                  e="select password from records where ACCONT_NO={}".format(acct)
                  c1.execute(e)
                  a=c1.fetchone()
                  d=list(a)
                  if pas==d[0]:
                        print("correct")
                        print("1.Depositng money")
                        print("2.withdrawing money")
                        print("3.Transfering money")
                        print("4.Checking balance")
                        print("5.Changing Account number ")
                        print("================================================================================")

                        r=int(input("Enter your choice:"))
                        print("================================================================================")


if r==1:
          amt=int(input("Enter the money to be deposited:"))            print("=============================================================================”)
sr="update records set CR_AMT=CR_AMT + {} where ACCONT_NO={}".format(amt,acct)
           c1.execute(sr)
           conn.commit()
           ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(acct)
           c1.execute(ef)
           conn.commit()
           print("sucessfully deposited")                    
           t=input("Do you want to continue y/n -")                  print("================================================================================")

           if t=="y":
                  continue
           else:
                  print("                    Thank you")
                  print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                       

 if r==2:
           amt=int(input("Enter the money to withdraw:”)                     print("================================================================================")   
ah="select  BALANCE from records where accont_no={}".format(acct)
           c1.execute(ah)
           m=c1.fetchone()
           if amt >m[0]:
                         print("Your are having less than",amt)
                         print("Please try again")                 
print("================================================================================")
  else:
                
               sr="update records set balance=balance - {}  where ACCONT_NO={}".format(amt,acct)
                  ed="update records set  WITHDRAWL ={}  where ACCONT_NO={}".format(amt,acct)
                  c1.execute(ed)
                  c1.execute(sr)
                  conn.commit()
                  print("Sucessfully updatad")
       y=input("do you want to continue y/n -")
                              if y=="y":
                                    continue
                              else:
                                    print("                    Thank you")
                                    print("           PLEASE CLOSE THIS FILE BEFORE EXITING")

if r==3:
           act=int(input("Enter the accont number to be transferrsd :"))
print("================================================================ 
==============")
                      cb="select * from records where ACCONT_NO={}".format(act)
                       c1.execute(cb)
                       c1.fetchall()
                       data=c1.rowcount
                        if data==1:
                                    print(act ,"number exists")
                                    m=int(input("Enter the money to be transferred :"))
print("======================================================
==========================")
                                    ah="select  BALANCE from records where accont_no={}".format(acct)
                                    c1.execute(ah)
                                    c=c1.fetchone()
                                    if m > c[0]:
                                          print("Your are having less than",m)
                                          print("Please try again")
print("====================================================
============================")


                          else:
                                  av="update records set balance=balance-{} where
ACCONT_NO={}".format(m,acct)  
                                  cv="update records set balance=balance+{} where
ACCONT_NO={}".format(m,act)
                                  w="update records set withdrawl=withdrawl+{} where accont_no={}".format(m,acct)
                                   t="update records set  CR_AMT=CR_AMT+{} where accont_no={}".format(m,act)
                                   c1.execute(av)
                                   c1.execute(cv)
                                   c1.execute(w)
                                   c1.execute(t)
                                   conn.commit()
                                   print("Sucessfully transfered")
                            y=input("do you want to continue y/n -")
                            if y=="y":
                                          continue
                             else:
                                          print("                    Thank you")
                                          print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
if r==4:
                              ma="select balance from records where accont_no={}".format(acct)
                              c1.execute(ma)
                              k=c1.fetchone()
                              print("Balance in your account=",k)
print("=========================================================
=======================")
                              y=input("do you want to continue y/n -")
                              if y=="y":
                                    continue
                              else:
                                    print("                    Thank you")
                                    print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                        if r==5:
                              i=int(input("Enter your new account number:"))
                              cb="select * from records where ACCONT_NO={}".format(i)
                              c1.execute(cb)
                              c1.fetchall()
                              data=c1.rowcount
                              if data==1:
                                    print("This number already exists")
                                    print("Try again")

                                    y=input("do you want to continue y/n -")
                                    if y=="y":
                                          continue
                                    else:
                                          print("                    Thank you")
                                          print("           PLEASE CLOSE THIS FILE BEFORE EXITING")
                              else:
                                    name=input("Enter your name")
                                    ar="Update records set accont_no={} where name='{}' and password={}".format(i,name,pas)
                                    c1.execute(ar)
                                    conn.commit()
                                    print("Your new account number is ",i)
                        
            
                  
                  else:
                        print("Wrong password")                        print("================================================================================")

                        y=input("do you want to continue y/n -")
            
         else:
                  print("your Account does not exists")





if op==3:
      print("Exiting")
      print("Please close this file before exiting.")
      c1.close()
