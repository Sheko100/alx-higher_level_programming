-- creates "user_0d_1" user and give it all privileges
CREATE USER user_0d_1 IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL
ON *.*
TO user_0d_1@localhost;
