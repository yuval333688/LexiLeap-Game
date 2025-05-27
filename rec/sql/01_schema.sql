-- ========= Database Creation (First Step) =========
-- Note: This command should be run separately, or the database should be created via the pgAdmin GUI.
-- CREATE DATABASE learning_progress_db;


-- ========= Table Creation (inside the newly created database) =========

-- 1. Create the 'users' table
-- This table will hold user information.
CREATE TABLE users (
    user_id BIGSERIAL PRIMARY KEY,  -- Primary Key, auto-incrementing big integer
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email, cannot be null
    password_hash VARCHAR(255) NOT NULL, -- Hashed password, cannot be null
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP -- Automatic timestamp of creation time
);

-- 2. Create the 'levels' table
-- This table defines all valid levels in the system.
CREATE TABLE levels (
    level_id INT PRIMARY KEY, -- Primary Key, the number of the level
    CONSTRAINT level_id_non_negative CHECK (level_id >= 0) -- Constraint to ensure the level number is non-negative
);

-- 3. Create the 'user_progress' table
-- This is the junction table, documenting the results of each user for each level.
CREATE TABLE user_progress (
    user_id BIGINT NOT NULL, -- Foreign key pointing to the user
    level_id INT NOT NULL,  -- Foreign key pointing to the level
    score INT NOT NULL, -- The score achieved
    completed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, -- Automatic timestamp

    -- Define a composite primary key: a unique combination of user and level
    PRIMARY KEY (user_id, level_id),

    -- Define foreign keys to link the tables
    CONSTRAINT fk_user
        FOREIGN KEY(user_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE, -- If a user is deleted, all their progress records will also be deleted

    CONSTRAINT fk_level
        FOREIGN KEY(level_id) 
        REFERENCES levels(level_id)
        ON DELETE RESTRICT, -- A level cannot be deleted if there are users who have completed it

    -- Constraint for valid score values
    CONSTRAINT score_range CHECK (score BETWEEN 0 AND 1000)
);


-- ========= Seed Initial Data into the 'levels' Table =========
-- This command inserts all levels from 0 to 20 into the 'levels' table.
INSERT INTO levels (level_id)
SELECT generate_series(0, 20);