-- Convert the database to utf8mb4 with utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Select the database
USE hbtn_0c_0;

-- Convert the table to utf8mb4 with utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Fix the column 'name' to use only COLLATE (not CHARACTER SET)
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;

