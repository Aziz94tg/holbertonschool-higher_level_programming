-- Step 1: Change the database collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 2: Select the database
USE hbtn_0c_0;

-- Step 3: Modify the table to inherit utf8mb4 defaults
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 4: Remove CHARACTER SET from `name` column by redefining only COLLATE
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;

