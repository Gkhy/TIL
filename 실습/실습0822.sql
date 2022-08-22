-- SQLite

sqlite3 0822.sqlite3
 CREATE TABLE users(
   ...> id primary key,
   ...> name text,
   ...> role_id int);
   .mode column;
   INSERT INTO users VALUES
   ...> (1,'관리자',1),
   ...> (2,'김철수',2),
   ...> (3,'이영희',2);
    CREATE TABLE role(
   ...> id primary key,
   ...> tilte TEXT);
    INSERT INTO role VALUES(
   ...> (1,admmin),
   ...> (2,staff),
   ...> (3,student);
   alter TABLE role
   ...> RENAME COLUMN tilte TO TITLE;
   UPDATE role set TITLE='studendt',TITLE='student'
    UPDATE role set TITLE='admin'where id=1
    UPDATE role set TITLE='staff' WHERE id=2
    CREATE TAble articles(        
   ...> id primary key,
   ...> title text,
   ...> content text,
   ...> user_id int);
    SELECT * FROM users INNER JOIN role ON
       ...> users.role_id= role.id;
       INSERT INTO articles VALUES(
   ...> 1,'1번글',111,1),
   ...> (2,'2번글',222,2),
   ...> (3,'3번글',333,1),
   ...> (4,'4번글',444,NULL)
   SELECT users.name, role.TITLE
   ...> FROM users INNER JOIN role
   ...> on users.role_id=role.id;
   SELECT users.name,role.id
   ...> FROM users INNER JOIN role
   ...> on users.role_id=role.id
   ...> where role_id=2;
    SELECT name,TITLE
   ...> FROM users INNER JOIN role
   ...> on users.role_id=role.id
   ...> ;
 SELECT * FROM articles LEFT OUTER JOIN users
   ...> on users.id= articles.user_id;
    SELECT * FROM articles LEFT OUTER JOIN users
   ...> on users.id=articles.user_id
   ...> WHERE user_id is not NULL;
   SELECT * FROM articles FULL OUTER JOIN users
   ...> ON users.id=articles.user_id;
    SELECT * FROM users CROSS
   ...> JOIN role;
SELECT * FROM articles
JOIN users
on articles.user_id=users.id
JOIN role
ON users.role_id=role.id;