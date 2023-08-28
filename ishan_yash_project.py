import pymysql
import os


# PLEASE CHECK USERNAME AND PASSWORD
con = pymysql.connect(user="root", password="root1", db="ishan_and_yash_project")
cursor = con.cursor()




def admin_console():
    print("Welcome....")

    admin_id = input("Enter admin id:-")
    password = input("Enter numeric password:-")
    n = cursor.execute("select * from admin where username='%s'" % (admin_id))
    if n == 0:
        print("No such admin")
        home_page()

    rec = cursor.fetchall()

    cred = (admin_id, password)
    for row in rec:
        adm_id = row[0]
        pswd = row[1]
    c = (adm_id, pswd)
    if c == cred:
        print("Welcome admin")
        while True:
            print("1. View all student")
            print("2. Issue T.C.")
            print("3. Search Student")
            print("4. Add new Student")
            print("5. Update Student_record")
            print("6. Fees update")
            print("7. Add Marks")
            print("8. View New Admission Applications")
            print("9. Exit")

            ch = input("Enter your choice:-")

            if ch == "1":
                cursor.execute("select * from student order by class")
                rec = cursor.fetchall()
                print("ID  NAME CLASS DATE OF BIRTH")
                for row in rec:
                    student_id = row[0]
                    name = row[1]
                    student_class = row[2]
                    date_of_birth = row[3]

                    print(row[0], row[1], row[2], row[3])

            elif ch == "2":
                std_id = int(input("Enter Student id:-"))
                cursor.execute("Select * from student where id='%d'" % (std_id))
                rec = cursor.fetchall()
                n = cursor.execute("delete from student where id='%d'" % (std_id))

                if n == 0:
                    print("No such Student exist")
                else:
                    print("Deleted successfuly")

                con.commit()
                stmnt = "Transfer Certificate"
                stmnt2 = "ABC International School"
                f = open("TC.txt", "w")
                for row in rec:
                    f.write(stmnt2 + "\n")
                    f.write(stmnt + "\n")
                    f.write("Admission Number" + str(row[0]) + "\n")
                    f.write("Name:-" + str(row[1]) + "\n")
                    f.write("Class:-" + str(row[2]) + "\n")
                    f.write("Date Of Birth:-" + str(row[3]) + "\n")
                    f.close()
                    path = os.path.abspath("TC.txt")
                    print("TC generated at " + path)

            elif ch == "3":
                std_id = int(input("Enter Student id to be search:-"))
                n = cursor.execute("select * from student where id='%s'" % (std_id))
                if n == 0:
                    print("No such student")

                else:
                    print("ID  NAME CLASS DATE OF BIRTH")
                rec = cursor.fetchall()

                for row in rec:
                    print(row[0], row[1], row[2], row[3])

            elif ch == "4":
                print("student id should be unique")
                std_id = int(input("Enter student id:-"))
                name = input("Enter name of student:-")
                std_class = int(input("Enter class:-"))
                date_of_birth = input("Enter student's date of birth:-")
                cursor.execute(
                    "insert into student values('%d','%s','%d','%s')"
                    % (std_id, name, std_class, date_of_birth)
                )
                print("New student added")
                con.commit()

            elif ch == "5":
                std_id = int(input("Enter student id:-"))
                name = input("Enter correct/updated name of student:-")
                std_class = int(input("Enter correct class:-"))
                date_of_birth = input("Enter correct student's date of birth:-")
                cursor.execute(
                    "update student set name='%s',class='%d',date_of_birth='%s' where id='%d'"
                    % (name, std_class, date_of_birth, std_id)
                )
                con.commit()
                if n == 0:
                    print("No such student")
                else:
                    print("update succesfull")
            elif ch == "6":
                fees_class = int(input("Enter class whose fees to be updated:-"))
                new_fees = int(input("Enter new fees:-"))
                n = cursor.execute(
                    "update fees set fees_per_month='%d' where class='%d'"
                    % (new_fees, fees_class)
                )
                if n == 0:
                    print("No such class")
                else:
                    print("Update succesful")
                con.commit()

            elif ch == "7":
                std_id = int(input("Enter sudent Id:-"))
                examination = input("Enter name of Examination:-")
                marks_obtained = int(input("Enter Marks obtained:-"))
                out_of = 500
                n = cursor.execute(
                    "insert into marks values ('%d', '%s','%d' , 500)"
                    % (std_id, examination, marks_obtained)
                )
                con.commit()
                if n == 0:
                    print("Error")
                else:
                    print("Insert succesful")

            elif ch == "8":
                cursor.execute("Select * from new_student")
                row = cursor.fetchall()
                for rows in row:
                    print("ID  CONTACT DATE OF BIRTH  CLASS")
                    print(rows[0], rows[1], rows[2], rows[3])

            elif ch == "9":
                print("Bye")
                break

            else:
                print("Wrong Input")
    else:
        print("Wrong credentials")

def Student_console():
    print("Welcome....")

    student_id = int(input("Enter your id:- "))
    password = input("Enter your Password(Date_of_birth):- ")
    n = cursor.execute("select * from student where id='%d'" % (student_id))
    if n == 0:
        print("No such student exist")
        home_page()
    rows = cursor.fetchall()
    tup = (student_id, password)
    for row in rows:
        std_id = row[0]
        pswd = row[3]
    c = (std_id, pswd)
    if c == tup:
        while True:
            print("1. Generate report card")
            print("2. Chek Fees")
            print("3. Exit ")
            print("For any change in details please contact admin.")

            ch = input("Enter your choice:-")
            if ch == "1":

                f = open("Result.txt", "w")
                cursor.execute(
                    "select s.id, s.name,m.marks_obtained, m.out_of, m.examination, s.class from student s inner join marks m on s.id = m.id where s.id='%d'"
                    % (student_id)
                )
                row = cursor.fetchall()

                f.write("Name" + " " + str(row[0][1]) + "\n")
                f.write("student id" + " " + str(row[0][0]) + "\n")
                f.write("\n")
                total = int(row[0][2]) + int(row[1][2])
                for rows in row:
                    marks = rows[2]
                    out_of = rows[3]
                    exam = rows[4]
                    std_class = rows[5]
                    f.write("Class" + " " + str(std_class) + "\n")
                    f.write("\n")
                    f.write("\n")
                    f.write("exam" + " " + exam + "\n")
                    f.write("marks" + " " + str(rows[2]) + "\n")
                    f.write("out of" + " " + str(out_of) + "\n")

                    f.write("\n")
                    f.write("\n")

                f.write("Total marks obtained" + " " + str(total) + "\n")
                f.write("Percentage" + " " + str((total / 10)))
                f.close()
                path = os.path.abspath("Result.txt")
                print("Report Card generated at " + path)

            elif ch == "2":
                cursor.execute(
                    "select s.id,s.name,s.class,a.months_pending, f.fees_per_month, (a.months_pending * f.fees_per_month) as pending_fees from student s  inner join std_fees_record a on s.id=a.id inner join fees f on f.class=s.class where s.id='%d'"
                    % std_id
                )
                row = cursor.fetchall()
                f = open("Fees_Record.txt", "w")
                for rows in row:
                    name = rows[0]
                    std_id = rows[1]
                    std_class = rows[2]
                    mnt_pending = rows[3]
                    fees_per_mnt = rows[4]
                    pending_fees = rows[5]

                f.write("Name" + " " + str(name) + "\n")
                f.write("ID" + " " + str(std_id) + "\n")
                f.write("Class" + " " + str(std_class) + "\n")
                f.write("Fees per Month" + " " + str(fees_per_mnt) + "\n")
                f.write("Months pending" + " " + str(mnt_pending) + "\n")
                f.write("Total Fees Pending" + " " + str(pending_fees) + "\n")
                f.close()
                path = os.path.abspath("Fees_Record.txt")
                print("Fees record generated at " + path)

            elif ch == "3":
                print("Exit")
                break
            else:
                print("Wrong Input")
    else:
        print("Wrong Credentials")

def New_Student_page():
    print("Welcome")
    name = input("Enter your name:-")
    cont = int(input("Enter your mobile number:-"))
    date_of_birth = input("Enter Your Date of Birth:-")
    ns_class = int(input("Enter Class in which you want to take admission:-"))

    cursor.execute(
        "insert into new_student(name,contact,date_of_birth,class_to_admit) value('%s',%d,'%s','%d')"
        % (name, cont, date_of_birth, ns_class)
    )
    cursor.execute("Select count(name) from new_student")

    row = cursor.fetchall()
    ackw_number = str(row[0][0])

    con.commit()

    f = open("Acknowledgement.txt", "w")
    stmt1 = "We have recieved your Application for admission in our School.Currently we are reviewing your application will update you shortly."
    f.write("ABC International School" + "\n")
    f.write("Acknowledge ment number:-" + "00" + ackw_number + "\n")
    f.write("Name" + "  " + name + "\n")
    f.write(stmt1)
    path = os.path.abspath("Acknowledgement.txt")
    print("Acknowledgement generated at " + path)

def home_page():
    while True:
        print("Welcome to ABC International School")
        print("1. Admin console")
        print("2. Student console")
        print("3. New Student Registartion")
        print("4. Exit")
        ch = input("Enter your choice:-")
        if ch == "1":
            admin_console()
        elif ch == "2":
            Student_console()
        elif ch == "3":
            New_Student_page()
        elif ch == "4":
            print("Bye")
            break
        else:
            print("Wrong Input")

home_page()


cursor.close()
con.close()

