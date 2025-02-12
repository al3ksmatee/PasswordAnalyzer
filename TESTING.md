# 🧪 Password Analyzer - Testing

Follow these test cases to verify the functionality of **Password Analyzer**.

---

## ✅ 1. Generate SHA-256 Hash
Run:

python password_analyzer.py --hash "mypassword123"

📌 Expected Output:
A SHA-256 hash of "mypassword123" should be displayed.

🖼 Screenshot:

## ✅ 2. Analyze a Single Password
Run:

python password_analyzer.py --password "StrongPass!@#"

📌 Expected Output:
Displays password length.
Shows entropy level.
Checks if the password is in leaked databases.

🖼 Screenshot:

## ✅ 3. Analyze Multiple Passwords from a File
Create a test file:

echo -e "password123\nStrongPass!@#\nqwerty123" > test_passwords.txt

Run:

python password_analyzer.py --file test_passwords.txt

📌 Expected Output:
Each password in test_passwords.txt should be analyzed separately.

🖼 Screenshot:

## ✅ 4. Save Report to a File
Run:

python password_analyzer.py --password "mypassword123" --save

📌 Expected Output:
A password_report.txt file is created with detailed password analysis.

🖼 Screenshot:
