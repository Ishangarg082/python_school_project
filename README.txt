The python project requires the scrip pre requistive to be run first.
please run that file only once
please check and add your mysql credentials


onwer credentials= owner_username   , owner_pass@123

admin creds= admin1 , 12345 
             admin2 , 9876


cursor.execute("create table northindian(numb varchar(20), name varchar(60), price varchar(15), type varchar(30));")
cursor.execute("create table southindian(numb varchar(20), name varchar(60), price varchar(15), categary varchar(30));")
cursor.execute("create table snack(numb varchar(20), name varchar(60), price varchar(15), type varchar(30));")

cursor.execute("insert into snack values (1, 'TEA', '20', 'veg');")
cursor.execute("insert into snack values (2, 'COFFEE', '20', 'veg');")
cursor.execute("insert into snack values (3, 'SAMOSA', '20', 'veg');")
cursor.execute("insert into snack values (4, 'Pattie', '25', 'veg');")
cursor.execute("insert into snack values (5, 'BREAD PAKODA', '20', 'veg');")
cursor.execute("insert into snack values (6, 'LEMONADE', '20', 'veg');")
cursor.execute("insert into snack values (7, 'SODA DRINKS', '40', 'veg');")
cursor.execute("insert into snack values (8, 'CHESSY SANDWICH GRILLED', '40', 'veg');")
cursor.execute("insert into snack values (9, 'TIKKI CHAT', '40', 'veg');")
cursor.execute("insert into snack values (10, 'RAJ KACHORI', '40', 'veg');")
cursor.execute("insert into snack values (11, 'BURGER', '50', 'veg');")
cursor.execute("insert into snack values (12, 'FRENCH FRIES', '50', 'veg');")
cursor.execute("insert into snack values (13, 'ROLLS', '50', 'veg');")
cursor.execute("insert into snack values (14, 'PASTA', '60', 'veg');")
cursor.execute("insert into snack values (15, 'ICECREAM', '60', 'veg');")
cursor.execute("insert into snack values (16, 'PIZZA', '150', 'veg');")



cursor.execute("insert into northindian values (1, 'DAL MAKHANI', '150', 'veg');")
cursor.execute("insert into northindian values (2, 'PANEER MASALA', '150', 'veg');")
cursor.execute("insert into northindian values (3, 'SAHI PANEER','180', 'veg');")
cursor.execute("insert into northindian values (4, 'PANEER KHOFTA', '200', 'veg');")
cursor.execute("insert into northindian values (5, 'ALLO GOBHI', '70', 'veg');")
cursor.execute("insert into northindian values (6, 'BHINDI', '60', 'veg');")
cursor.execute("insert into northindian values (7, 'CHOLLE BHATURE','50', 'veg');")
cursor.execute("insert into northindian values (8, 'CHOLLE KULCHE', '50', 'veg');")
cursor.execute("insert into northindian values (9, 'RAJMA CHAWAL', '100', 'veg');")
cursor.execute("insert into northindian values (10, 'FRIED RICE', '90', 'veg');")
cursor.execute("insert into northindian values (11, 'ALLO PRANTHA', '25', 'veg');")
cursor.execute("insert into northindian values (12, 'GOBHI PRANTHA', '25', 'veg');")
cursor.execute("insert into northindian values (13, 'MIX VEG', '90', 'veg');")
cursor.execute("insert into northindian values (14, 'BUTTER NAAN', '40', 'veg');")
cursor.execute("insert into northindian values (15, 'PLAIN NAAN', '30', 'veg');")
cursor.execute("insert into northindian values (16, 'TAWA ROTI', '10', 'veg');")
cursor.execute("insert into northindian values (17, 'TANDOOR ROTI', '10', 'veg');")
cursor.execute("insert into northindian values (18, 'CURD', '50', 'veg');")
cursor.execute("insert into northindian values (19, 'GULAB JAMUN', '50', 'veg');")
cursor.execute("insert into northindian values (20, 'GAJAR HALWA', '50', 'veg');")



cursor.execute("insert into southindian values (1, 'PLAIN DOSA', '50', 'veg');")
cursor.execute("insert into southindian values (2, 'BUTTER DOSA', '80', 'veg');")
cursor.execute("insert into southindian values (3, 'IDLI', '30', 'veg');")
cursor.execute("insert into southindian values (4, 'VADA', '40', 'veg');")
cursor.execute("insert into southindian values (5, 'UTTAPAM', '50', 'veg');")




