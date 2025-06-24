-- Script to create table `unique_id` with a unique default id value

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

