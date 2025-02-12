# 🧪 Password Analyzer - Testing

Follow these test cases to verify the functionality of **Password Analyzer**.

---

## ✅ 1. Generate SHA-256 Hash
Run:

python password_analyzer.py --hash "mypassword123"

📌 Expected Output:
A SHA-256 hash of "mypassword123" should be displayed.

🖼 Screenshot:

![test1](https://github.com/user-attachments/assets/eb8f5e0a-3ae6-465f-975d-0df185f60253)




## ✅ 2. Analyze a Single Password
Run:

python password_analyzer.py --password "StrongPass!@#"

📌 Expected Output:
Displays password length.
Shows entropy level.
Checks if the password is in leaked databases.

🖼 Screenshot:

![test2](https://github.com/user-attachments/assets/8fb1bbb6-025c-4c80-8d14-edf6f2067e9a)




## ✅ 3. Analyze Multiple Passwords from a File
Create a test file:

echo -e "password123\nStrongPass!@#\nqwerty123" > test_passwords.txt

Run:

python password_analyzer.py --file test_passwords.txt

📌 Expected Output:
Each password in test_passwords.txt should be analyzed separately.

🖼 Screenshot:

![test3](https://github.com/user-attachments/assets/5c44f82d-293c-485d-9ee1-d66157bd3224)




## ✅ 4. Save Report to a File
Run:

python password_analyzer.py --password "mypassword123" --save

📌 Expected Output:
A password_report.txt file is created with detailed password analysis.

🖼 Screenshot:

![test 4](https://github.com/user-attachments/assets/021287d2-7009-452f-b87d-ce7fc3a3361d)



