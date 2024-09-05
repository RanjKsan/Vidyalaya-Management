# ***************SRDF VIDYALAYA CHROMEPET **********************"
# ******************VIDYALAYA MANAGER *****************************"
# *******Designed and Maintained By:"
# *******RANJINI- CLASS XII D - ROLL NO - 2 [ 2019-2020 ]"
# *******GM- CLASS XII A - ROLL NO - 7 [ 2019-2020 ]"
# *******GM - CLASS XII A - ROLL NO - 8 [ 2019-2020 ]"

import mysql.connector

# GLOBAL VARIABLES DECLARATION
myConnection = ""
cursor = ""
userName = ""
password = ""

# MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck():
    global myConnection
    global userName
    global password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME: ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD: ")
    myConnection = mysql.connector.connect(
        host="localhost",
        user=userName,
        passwd=password,
        auth_plugin='mysql_native_password'
    )
    if myConnection:
        print("\n CONGRATULATIONS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS SMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION. CHECK USERNAME AND PASSWORD!")


# MODULE TO ESTABLISH MYSQL CONNECTION
def MYSQLconnection():
    global userName
    global password
    global myConnection
    myConnection = mysql.connector.connect(
        host="localhost",
        user=userName,
        passwd=password,
        database="SMS",
        auth_plugin='mysql_native_password'
    )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")
        myConnection.close()


# MODULE FOR NEW ADMISSION
def newStudent():
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """
        CREATE TABLE IF NOT EXISTS STUDENT(
            SNAME VARCHAR(30),
            FNAME VARCHAR(30),
            MNAME VARCHAR(30),
            PHONE VARCHAR(12),
            ADDRESS VARCHAR(100),
            SCLASS VARCHAR(5),
            SSECTION VARCHAR(5),
            SROLL_NO VARCHAR(5),
            SADMISSION_NO VARCHAR(10) PRIMARY KEY
        )
        """
        cursor.execute(createTable)
        sname = input("\n ENTER STUDENT'S NAME: ")
        fname = input(" ENTER FATHER'S NAME: ")
        mname = input(" ENTER MOTHER'S NAME: ")
        phone = input(" ENTER CONTACT NO.: ")
        address = input(" ENTER ADDRESS: ")
        sclass = input(" ENTER CLASS: ")
        ssection = input(" ENTER SECTION: ")
        sroll_no = input(" ENTER ROLL_NO: ")
        sadmission_no = input(" ENTER ADMISSION_NO: ")

        sql = """
        INSERT INTO student(
            SNAME, FNAME, MNAME, PHONE, ADDRESS, SCLASS, SSECTION, SROLL_NO, SADMISSION_NO
        ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (sname, fname, mname, phone, address, sclass, ssection, sroll_no, sadmission_no)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nNew Student Enrolled Successfully!")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    cursor = myConnection.cursor()
    if myConnection:
        cursor.execute("SELECT * FROM STUDENT")
        data = cursor.fetchall()
        print(data)
        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")


# MODULE TO UPDATE STUDENT'S RECORD
def updateStudent():
    cursor = myConnection.cursor()
    if myConnection:
        admission_no = input("ENTER ADMISSION NO: ")
        sql = "SELECT * FROM STUDENT WHERE SADMISSION_NO = %s"
        cursor.execute(sql, (admission_no,))
        data = cursor.fetchall()
        if data:
            print("PRESS 1 FOR NAME")
            print("PRESS 2 FOR CLASS")
            print("PRESS 3 FOR ROLL NO")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                name = input("ENTER NAME OF THE STUDENT: ")
                sql = "UPDATE STUDENT SET SNAME = %s WHERE SADMISSION_NO = %s"
                cursor.execute(sql, (name, admission_no))
                cursor.execute("COMMIT")
                print("NAME UPDATED")
            elif choice == 2:
                std = input("ENTER CLASS OF THE STUDENT: ")
                sql = "UPDATE STUDENT SET SCLASS = %s WHERE SADMISSION_NO = %s"
                cursor.execute(sql, (std, admission_no))
                cursor.execute("COMMIT")
                print("CLASS UPDATED")
            elif choice == 3:
                roll_no = int(input("ENTER ROLL NO OF THE STUDENT: "))
                sql = "UPDATE STUDENT SET SROLL_NO = %s WHERE SADMISSION_NO = %s"
                cursor.execute(sql, (roll_no, admission_no))
                cursor.execute("COMMIT")
                print("ROLL NO UPDATED")
            else:
                print("Record Not Found. Try Again!")
            cursor.close()
        else:
            print("\nSomething Went Wrong, Please Try Again!")


# MODULE TO ENTER MARKS OF THE STUDENT
def marksStudent():
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """
        CREATE TABLE IF NOT EXISTS MARKS(
            SADMISSION_NO VARCHAR(10) PRIMARY KEY,
            HINDI INT, ENGLISH INT, MATH INT, SCIENCE INT,
            SOCIAL INT, COMPUTER INT, TOTAL INT, AVERAGE DECIMAL
        )
        """
        cursor.execute(createTable)
        admission_no = input("ENTER ADMISSION NO OF THE STUDENT: ")
        hindi = int(input("\n ENTER MARKS OF HINDI: "))
        english = int(input("\n ENTER MARKS OF ENGLISH: "))
        math = int(input("\n ENTER MARKS OF MATH: "))
        science = int(input("\n ENTER MARKS OF SCIENCE: "))
        social = int(input("\n ENTER MARKS OF SOCIAL: "))
        computer = int(input("\n ENTER MARKS OF COMPUTER: "))
        total = hindi + english + math + science + social + computer
        average = total / 6
        sql = """
        INSERT INTO MARKS(
            SADMISSION_NO, HINDI, ENGLISH, MATH, SCIENCE, SOCIAL, COMPUTER, TOTAL, AVERAGE
        ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (admission_no, hindi, english, math, science, social, computer, total, average)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nMarks of the Student Entered Successfully!")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE TO GENERATE REPORT CARD OF ALL STUDENTS
def reportCardAllStudent():
    cursor = myConnection.cursor()
    if myConnection:
        cursor.execute("SELECT * FROM MARKS")
        data = cursor.fetchall()
        print(data)
        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")


# MODULE TO GENERATE REPORT CARD OF ONE STUDENT
def reportCardOneStudent():
    cursor = myConnection.cursor()
    if myConnection:
        admission_no = input("ENTER ADMISSION NO OF THE STUDENT: ")
        cursor = myConnection.cursor()
        sql = "SELECT * FROM MARKS WHERE SADMISSION_NO = %s"
        cursor.execute(sql, (admission_no,))
        data = cursor.fetchall()
        if data:
            print(data)
        else:
            print("Record Not Found, Please Try Again!")
        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")


# MODULE TO ENTER FEES OF THE STUDENTS
def feeStudent():
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """
        CREATE TABLE IF NOT EXISTS FEES(
            SADMISSION_NO VARCHAR(10) PRIMARY KEY,
            MONTH INT, TUTION_FEES INT, VVN INT, COMPUTER_FEES INT,
            MUSIC_FEES INT, TOTAL INT
        )
        """
        cursor.execute(createTable)
        admission_no = input("ENTER ADMISSION NO OF THE STUDENT: ")
        month = int(input("\n ENTER MONTH IN NUMERIC FORM (1-12): "))
        tutionfee = int(input("\n ENTER TUTION FEES: "))
        vvn = int(input("\n ENTER VVN: "))
        computerfee = int(input("\n ENTER COMPUTER FEES: "))
        musicfee = int(input("\n ENTER MUSIC FEES: "))
        total = tutionfee + vvn + computerfee + musicfee
        sql = """
        INSERT INTO FEES(
            SADMISSION_NO, MONTH, TUTION_FEES, VVN, COMPUTER_FEES, MUSIC_FEES, TOTAL
        ) VALUES(%s, %s, %s, %s, %s, %s, %s)
        """
        values = (admission_no, month, tutionfee, vvn, computerfee, musicfee, total)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nFees Paid Successfully!")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE TO GENERATE FEES REPORT OF ALL STUDENTS
def feesReportAllStudents():
    cursor = myConnection.cursor()
    if myConnection:
        cursor.execute("SELECT * FROM FEES")
        data = cursor.fetchall()
        print(data)
        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")


# MODULE TO GENERATE FEES REPORT OF ONE STUDENT
def feesReportOneStudent():
    cursor = myConnection.cursor()
    if myConnection:
        admission_no = input("ENTER ADMISSION NO OF THE STUDENT: ")
        cursor = myConnection.cursor()
        sql = "SELECT * FROM FEES WHERE SADMISSION_NO = %s"
        cursor.execute(sql, (admission_no,))
        data = cursor.fetchall()
        if data:
            print(data)
        else:
            print("Record Not Found, Please Try Again!")
        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again!")


# MAIN PROGRAM STARTS HERE
print("\n******************WELCOME TO VIDYALAYA MANAGER SYSTEM******************")
print("\n******************CHECKING MYSQL CONNECTIVITY**********************")
MYSQLconnectionCheck()

while True:
    print("\n*********************WELCOME TO VIDYALAYA MANAGER******************************")
    print("\nPRESS 1: FOR NEW ADMISSION")
    print("PRESS 2: TO DISPLAY ALL STUDENT'S RECORDS")
    print("PRESS 3: TO UPDATE STUDENT'S RECORD")
    print("PRESS 4: TO ENTER STUDENT'S MARKS")
    print("PRESS 5: TO GENERATE REPORT CARD OF ALL STUDENTS")
    print("PRESS 6: TO GENERATE REPORT CARD OF A STUDENT")
    print("PRESS 7: TO ENTER FEES OF STUDENTS")
    print("PRESS 8: TO GENERATE FEES REPORT OF ALL STUDENTS")
    print("PRESS 9: TO GENERATE FEES REPORT OF A STUDENT")
    print("PRESS 10: TO EXIT")
    print("\n*******************************************************************************")

    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        MYSQLconnection()
        newStudent()
    elif choice == 2:
        MYSQLconnection()
        displayStudent()
    elif choice == 3:
        MYSQLconnection()
        updateStudent()
    elif choice == 4:
        MYSQLconnection()
        marksStudent()
    elif choice == 5:
        MYSQLconnection()
        reportCardAllStudent()
    elif choice == 6:
        MYSQLconnection()
        reportCardOneStudent()
    elif choice == 7:
        MYSQLconnection()
        feeStudent()
    elif choice == 8:
        MYSQLconnection()
        feesReportAllStudents()
    elif choice == 9:
        MYSQLconnection()
        feesReportOneStudent()
    elif choice == 10:
        break
    else:
        print("\nWrong Choice, Please Try Again!")
