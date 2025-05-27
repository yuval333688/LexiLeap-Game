-- ========= Seeding Test Data =========

-- 1. Insert a new user for testing
-- We assume this user's user_id will be 1, as it's the first one being added.
INSERT INTO users (email, password_hash) 
VALUES ('test.user@example.com', 'dummy_bcrypt_hash_for_testing');


-- 2. Insert progress records for the user
-- The user with user_id = 1 has passed 10 levels (0-9) with a valid score.
-- The dates are staggered to simulate progress over several days.

INSERT INTO user_progress (user_id, level_id, score, completed_at) VALUES
(1, 0, 750, NOW() - INTERVAL '10 days'), -- Passed level 0 with a score of 750, 10 days ago
(1, 1, 810, NOW() - INTERVAL '9 days'),  -- Passed level 1 with a score of 810, 9 days ago
(1, 2, 645, NOW() - INTERVAL '9 days'),  -- Passed level 2 with a score of 645, 9 days ago
(1, 3, 920, NOW() - INTERVAL '8 days'),  -- Passed level 3 with a score of 920, 8 days ago
(1, 4, 705, NOW() - INTERVAL '7 days'),  -- Passed level 4 with a score of 705, 7 days ago
(1, 5, 880, NOW() - INTERVAL '6 days'),  -- Passed level 5 with a score of 880, 6 days ago
(1, 6, 615, NOW() - INTERVAL '5 days'),  -- Passed level 6 with a score of 615, 5 days ago
(1, 7, 995, NOW() - INTERVAL '4 days'),  -- Passed level 7 with a score of 995, 4 days ago
(1, 8, 760, NOW() - INTERVAL '2 days'),  -- Passed level 8 with a score of 760, 2 days ago
(1, 9, 855, NOW() - INTERVAL '1 day');   -- Passed level 9 with a score of 855, yesterday


-- ======== Verification Query (Optional) =========
-- Run this query to see the new user's progress in an ordered fashion
SELECT 
    u.user_id,
    u.email,
    up.level_id,
    up.score,
    up.completed_at
FROM 
    users u
JOIN 
    user_progress up ON u.user_id = up.user_id
WHERE 
    u.email = 'test.user@example.com'
ORDER BY 
    up.level_id;