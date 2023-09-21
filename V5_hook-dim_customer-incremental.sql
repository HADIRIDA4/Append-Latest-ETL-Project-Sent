-- Ensure the table exists and create it if it doesn't
CREATE TABLE IF NOT EXISTS target_schema.dim_customer (
    ID SERIAL PRIMARY KEY NOT NULL,
    customer_name TEXT,
    customer_lastname TEXT,
    customer_age INT,
    date_of_birth TIMESTAMP,
    updated_date TIMESTAMP,
    source_name TEXT
);

-- Create an index if it doesn't exist
CREATE INDEX IF NOT EXISTS idx_customer_id ON target_schema.dim_customer(ID);
-- UPSERT(UPDATE THEN INSERT IF NEW)
--PART 1 UPDATE BASED ON ID 
UPDATE target_schema.dim_customer AS dim
SET
    customer_name = src.customer_name,
    customer_lastname = src.customer_lastname,
    customer_age = src.customer_age,
    date_of_birth = src.date_of_birth,
    updated_date = src.updated_date,
    source_name = src.source_name
FROM (
    SELECT 
        id,
        name AS customer_name,
        lastname AS customer_lastname,
        age AS customer_age,
        dob AS date_of_birth,
        updated_date,
        'DVD_RENTAL' AS source_name
    FROM target_schema.stg_dvd_rental_customer
    UNION ALL
    SELECT 
        id,
        customer_name,
        customer_lastname,
        customer_age,
        date_of_birth,
        updated_date,
        'ANOTHER_SOURCE' AS source_name
    FROM target_schema.stg_college_students
) AS src
WHERE dim.ID = src.id;

-- PART 2 Insert new records that don't exist in the target table
INSERT INTO target_schema.dim_customer (ID, customer_name, customer_lastname, customer_age, date_of_birth, updated_date, source_name)
SELECT 
    src.id,
    src.customer_name,
    src.customer_lastname,
    src.customer_age,
    src.date_of_birth,
    src.updated_date,
    src.source_name
FROM (
    SELECT 
        id,
        name AS customer_name,
        lastname AS customer_lastname,
        age AS customer_age,
        dob AS date_of_birth,
        updated_date,
        'DVD_RENTAL' AS source_name
    FROM target_schema.stg_dvd_rental_customer
    UNION ALL
    SELECT 
        id,
        customer_name,
        customer_lastname,
        customer_age,
        date_of_birth,
        updated_date,
        'ANOTHER_SOURCE' AS source_name
    FROM target_schema.stg_college_students
) AS src
WHERE src.id NOT IN (SELECT ID FROM target_schema.dim_customer);
