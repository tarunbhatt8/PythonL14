'''
Q.1- Create a database. Create the following tables:
1. Book
2. Titles
3. Publishers
4. Zipcodes
5. AuthorsTitles
6. Authors



Q.2- Insert values in the tables.


Q.3- Update any values in any of the tables. Print the original and updated values.

'''
import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()

query1 = "create table zipcodes(zipcodeid int(6) primary key, city varchar(20), state varchar(20), zipcode int(6));"
records1 = [(248001, 'Dehradun', 'Uttarakhand',248001),(249193, 'Uttarkashi', 'Uttarakhand',249193)]
cursor.executemany(query1, records1)


query2 = "create table publishers(publisherid int(6) primary key, name varchar(20), streetaddress varchar(50), streetno int(6), zipcodeid int(6), FOREIGN KEY (zipcodeid) REFERENCES zipcodes(zipcodesid));"
records2 = [(1, 'Tarun', 'Sarvoday Ashram Ujeli',1,249193),(2, 'Ashu', 'Baker's Street Premnagar',1,248001)]
cursor.executemany(query2, records2)


query3 = "create table authors(authorid int(6) primary key, firstname varchar(20), middlename varchar(20),lastname varchar(20) );"
records3 = [(1,'Samyak','Kumar','Sinha'),(2,'Rahul','Pratap','Singh')]
cursor.executemany(query3, records3)



query4 = "create table authorstitles(authortitleid int(6) primary key, authorid int(6),titleid int(6), FOREIGN KEY (authortitleid) REFERENCES authors(authorid));"
records4 = [(1,1,1),(2,2,2)]
cursor.executemany(query4, records4)


query5 = "create table titles(titleid int(6) primary key, title varchar(20),ISBN varchar(20),publisherid int(6), publicationyear varchar(4) FOREIGN KEY (titleid) REFERENCES authorstitles(authortitleid),FOREIGN KEY (publicherid) REFERENCES publishers(publisherid));"
records5 = [(1,'ABC','1A2B',1,'2010'),(2,'DEF','3C4D',2,'2011')]
cursor.executemany(query5, records5)





    
query6 = "create table book(bookid int(5) primary key, titleid varchar(10), location varchar(20), genre varchar(20),FOREIGN KEY (bookid) REFERENCES titles(titleidid));"
records6 = [(1, 'Book1', 'Dehradun','Comedy'),(2,'Book2','Uttarkshi','Thriller')]
cursor.executemany(query6, records6)


query7="select * from books"
cursor.execute(query7)
    
query8 = "update books set titleid='MyBook' where titleid = 'Book1'"
    
cursor.execute(query8)  
cursor.execute(query7)

 
con.commit()


    
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
