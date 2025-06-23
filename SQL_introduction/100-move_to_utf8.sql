-- Select the correct DB
USE hbtn_0c_0;

-- Change default charset and collation at the DB level
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Apply conversion at table level
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Override column-level charset to remove CHARACTER SET declaration
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
-- Step 1: Change the database collation

