import pymysql
con=pymysql.connect(user="root",password="root1")
cursor=con.cursor()
cursor.execute("drop database ishan_and_yash_project")
cursor.execute("create database ishan_and_yash_project")
cursor.execute("use ishan_and_yash_project")


cursor.execute("create table student (id int primary key, name varchar(30), class int , date_of_birth varchar(15))")
cursor.execute("insert into student (id, name, class, date_of_birth) values (1, 'Royal', 12,'02/09/2004')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (2, 'Cherye', 1,'04/03/2016')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (3, 'Anna-diana', 1,'20/11/2016')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (4, 'Zaccaria', 5,'14/08/2011')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (5, 'Ileana', 4,'03/06/2012')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (6, 'Kamilah', 12,'25/09/2015')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (7, 'Dianemarie', 2,'27/03/2004')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (8, 'Gavra', 2,'19/10/2017')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (9, 'Rog', 2,'14/10/2017')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (10, 'Cozmo', 3,'18/03/2018')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (11, 'Cathy', 9,'21/08/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (12, 'Fayina', 4,'11/02/2019')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (13, 'Lorrie', 9,'22/11/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (14, 'Daron', 9,'09/06/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (15, 'Iggy', 8,'16/05/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (16, 'Della', 12,'17/11/2004')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (17, 'Davina', 10,'12/04/2006')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (18, 'Dyan', 9,'10/02/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (19, 'Lockwood', 9,'19/02/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (20, 'Cati', 10,'19/04/2006')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (21, 'Nanette', 12,'01/04/2004')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (22, 'Trey', 9,'01/04/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (23, 'Delinda', 11,'13/12/2005')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (24, 'Aurilia', 6,'30/05/2010')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (25, 'Stefano', 2,'19/02/2017')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (26, 'Lea', 10,'13/09/2010')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (27, 'Antin', 5,'02/09/2011')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (28, 'Haywood', 8,'13/05/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (29, 'Kimmie', 8,'10/09/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (30, 'Uta', 8,'01/04/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (31, 'Eduardo', 8,'02/08/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (32, 'Waverly', 8,'24/12/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (33, 'Sherill', 11,'28/03/2005')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (34, 'Julianna', 2,'06/04/2017')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (35, 'Seline', 7,'10/02/2009')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (36, 'Delinda', 4,'06/04/2019')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (37, 'Kaile', 2,'23/05/2017')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (38, 'Sonni', 2,'25/03/2017')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (39, 'Genia', 12,'29/04/2004')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (40, 'Melosa', 9,'08/04/2007')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (41, 'Allix', 5,'04/12/2011')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (42, 'Haydon', 6,'21/01/2010')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (43, 'Selena', 4,'07/09/2019')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (44, 'Humfrey', 4,'30/09/2019')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (45, 'Dilan', 8,'10/08/2008')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (46, 'Wernher', 10,'21/06/2010')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (47, 'Laverne', 5,'07/09/2011')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (48, 'Maribelle', 6,'08/05/2010')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (49, 'Pavlov', 7,'30/06/2009')")
cursor.execute("insert into student (id, name, class, date_of_birth) values (50, 'Randeep', 7,'27/11/2009')")


cursor.execute("create table admin(username varchar(20), password varchar(8))")
cursor.execute("insert into admin values('admin1', '12345')")
cursor.execute("insert into admin values('admin2', '09876')")
cursor.execute("create table marks(id int, examination varchar(20),marks_obtained int,out_of int)")

cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (1, 'midterm', 471, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (2, 'midterm', 376, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (3, 'midterm', 410, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (4, 'midterm', 361, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (5, 'midterm', 445, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (6, 'midterm', 472, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (7, 'midterm', 366, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (8, 'midterm', 497, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (9, 'midterm', 375, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (10, 'midterm', 449, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (11, 'midterm', 492, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (12, 'midterm', 360, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (13, 'midterm', 491, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (14, 'midterm', 478, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (15, 'midterm', 351, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (16, 'midterm', 377, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (17, 'midterm', 436, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (18, 'midterm', 433, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (19, 'midterm', 486, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (20, 'midterm', 398, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (21, 'midterm', 491, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (22, 'midterm', 380, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (23, 'midterm', 428, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (24, 'midterm', 405, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (25, 'midterm', 370, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (26, 'midterm', 375, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (27, 'midterm', 365, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (28, 'midterm', 458, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (29, 'midterm', 457, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (30, 'midterm', 446, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (31, 'midterm', 419, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (32, 'midterm', 416, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (33, 'midterm', 493, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (34, 'midterm', 447, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (35, 'midterm', 451, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (36, 'midterm', 407, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (37, 'midterm', 498, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (38, 'midterm', 370, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (39, 'midterm', 353, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (40, 'midterm', 367, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (41, 'midterm', 465, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (42, 'midterm', 422, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (43, 'midterm', 477, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (44, 'midterm', 426, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (45, 'midterm', 434, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (46, 'midterm', 438, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (47, 'midterm', 448, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (48, 'midterm', 375, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (49, 'midterm', 462, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (50, 'midterm', 498, 500)")



cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (1, 'finalexam', 465, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (2, 'finalexam', 402, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (3, 'finalexam', 441, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (4, 'finalexam', 493, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (5, 'finalexam', 492, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (6, 'finalexam', 442, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (7, 'finalexam', 359, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (8, 'finalexam', 372, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (9, 'finalexam', 375, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (10, 'finalexam', 416, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (11, 'finalexam', 488, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (12, 'finalexam', 481, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (13, 'finalexam', 496, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (14, 'finalexam', 388, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (15, 'finalexam', 390, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (16, 'finalexam', 366, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (17, 'finalexam', 495, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (18, 'finalexam', 440, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (19, 'finalexam', 352, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (20, 'finalexam', 402, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (21, 'finalexam', 389, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (22, 'finalexam', 388, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (23, 'finalexam', 422, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (24, 'finalexam', 436, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (25, 'finalexam', 498, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (26, 'finalexam', 496, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (27, 'finalexam', 365, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (28, 'finalexam', 406, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (29, 'finalexam', 382, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (30, 'finalexam', 475, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (31, 'finalexam', 492, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (32, 'finalexam', 476, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (33, 'finalexam', 417, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (34, 'finalexam', 460, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (35, 'finalexam', 486, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (36, 'finalexam', 440, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (37, 'finalexam', 367, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (38, 'finalexam', 382, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (39, 'finalexam', 448, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (40, 'finalexam', 422, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (41, 'finalexam', 438, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (42, 'finalexam', 404, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (43, 'finalexam', 472, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (44, 'finalexam', 380, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (45, 'finalexam', 421, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (46, 'finalexam', 359, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (47, 'finalexam', 424, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (48, 'finalexam', 425, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (49, 'finalexam', 500, 500)")
cursor.execute("insert into marks (id, examination, marks_obtained, out_of) values (50, 'finalexam', 427, 500)")

cursor.execute("create table fees(class int,fees_per_month int)")
cursor.execute("insert into fees (class, fees_per_month) values (1, 1000)")
cursor.execute("insert into fees (class, fees_per_month) values (2, 1200)")
cursor.execute("insert into fees (class, fees_per_month) values (3, 1400)")
cursor.execute("insert into fees (class, fees_per_month) values (4, 1500)")
cursor.execute("insert into fees (class, fees_per_month) values (5, 1800)")
cursor.execute("insert into fees(class, fees_per_month) values (6, 2000)")
cursor.execute("insert into fees (class, fees_per_month) values (7, 2500)")
cursor.execute("insert into fees (class, fees_per_month) values (8, 2500)")
cursor.execute("insert into fees(class, fees_per_month) values (9, 2500)")
cursor.execute("insert into fees (class, fees_per_month) values (10, 3000)")
cursor.execute("insert into fees (class, fees_per_month) values (11, 3000)")
cursor.execute("insert into fees(class, fees_per_month) values (12, 3000)")

cursor.execute("create table std_fees_record (id int,months_pending int)")
cursor.execute("insert into std_fees_record (id, months_pending) values (1, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (2, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (3, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (4, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (5, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (6, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (7, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (8, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (9, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (10, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (11, 2)")
cursor.execute("insert into std_fees_record (id, months_pending) values (12, 2)")
cursor.execute("insert into std_fees_record (id, months_pending) values (13, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (14, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (15, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (16, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (17, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (18, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (19, 2)")
cursor.execute("insert into std_fees_record (id, months_pending) values (20, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (21, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (22, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (23, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (24, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (25, 2)")
cursor.execute("insert into std_fees_record (id, months_pending) values (26, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (27, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (28, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (29, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (30, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (31, 2)")
cursor.execute("insert into std_fees_record (id, months_pending) values (32, 2)")
cursor.execute("insert into std_fees_record (id, months_pending) values (33, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (34, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (35, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (36, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (37, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (38, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (39, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (40, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (41, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (42, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (43, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (44, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (45, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (46, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (47, 0)")
cursor.execute("insert into std_fees_record (id, months_pending) values (48, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (49, 1)")
cursor.execute("insert into std_fees_record (id, months_pending) values (50, 1)")



cursor.execute("create table new_student(name varchar(30),contact varchar(15),date_of_birth varchar(15),class_to_admit int)")
con.commit()
cursor.close()
con.close()
