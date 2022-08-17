-- SQLite
SELECT COUNT(*) FROM healthcare;
SELECT MAX(age),MIN(age) FROM healthcare;
SELECT MAX(height),MAX(weight),Min(height),MIN(weight) FROM healthcare;
SELECT count(*)FROM healthcare where 160<=height and height<=170;
SELECT waist FROM healthcare WHERE is_drinking=1 order by waist asc limit 5;
SELECT COUNT(*) FROM healthcare WHERE is_drinking=1 and va_left>=1.5 and va_right >=1.5;
SELECT COUNT(*)FROM healthcare WHERE blood_pressure<120;
SELECT avg(waist) from healthcare 
where blood_pressure>=140;
SELECT avg(height),avg(weight) FROM healthcare WHERE gender=1;
SELECT id, height, weight FROM healthcare order by height, weight desc limit 1 offset 1;
SELECT COUNT(*) FROM healthcare WHERE 30<=(weight/(height*height*0.0001));
SELECT id,(weight/(height*height*0.0001))FROM healthcare WHERE smoking=3 order by (weight/(height*height*0.0001)) asc limit 5; 
SELECT age FROM healthcare WHERE va_left+va_right>=3 order by age desc;
SELECT Max(age),va_right+va_left FROM healthcare;
SELECT height,gender FROM healthcare order by height desc, gender desc;