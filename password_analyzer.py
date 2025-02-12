import hashlib
import math
import requests
import re

def calculate_entropy(password):
    """Calculate the entropy of a given password."""
    char_sets = [
        (r'[a-z]', 26),  # Lowercase letters
        (r'[A-Z]', 26),  # Uppercase letters
        (r'[0-9]', 10),  # Numbers
        (r'[\W]', 32)    # Special characters
    ]
    
    pool_size = sum(size for pattern, size in char_sets if re.search(pattern, password))
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    
    return round(entropy, 2)

def check_pwned(password):
    """Check if a password is found in HaveIBeenPwned database."""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if suffix in response.text:
        return True  # Password has been leaked
    return False

def analyze_password(password):
    """Analyze password strength and provide recommendations."""
    length = len(password)
    entropy = calculate_entropy(password)
    pwned = check_pwned(password)

    print("\n🔍 Password Analysis Report 🔍")
    print(f"🔹 Password Length: {length}")
    print(f"🔹 Entropy: {entropy} bits (Higher is better)")
    
    if length < 8:
        print("⚠️ Weak: Password should be at least 8 characters long!")
    elif length < 12:
        print("🟡 Moderate: Consider using 12+ characters.")
    else:
        print("✅ Strong: Good length!")

    if entropy < 40:
        print("⚠️ Low Entropy: Password is predictable.")
    elif entropy < 60:
        print("🟡 Medium Entropy: Could be improved.")
    else:
        print("✅ High Entropy: Strong password.")

    if pwned:
        print("🚨 WARNING: This password has been found in leaked databases! Change it immediately.")
    else:
        print("✅ Safe: This password has not been found in leaks.")

if __name__ == "__main__":
    user_password = input("Enter a password to analyze: ")
    analyze_password(user_password)
def save_report(password, length, entropy, pwned):
    with open("password_report.txt", "w") as f:
        f.write("🔍 Password Security Report 🔍\n")
        f.write(f"🔹 Password Length: {length}\n")
        f.write(f"🔹 Entropy: {entropy} bits\n")

        if length < 8:
            f.write("⚠️ Weak: Password should be at least 8 characters long!\n")
        elif length < 12:
            f.write("🟡 Moderate: Consider using 12+ characters.\n")
        else:
            f.write("✅ Strong: Good length!\n")

        if entropy < 40:
            f.write("⚠️ Low Entropy: Password is predictable.\n")
        elif entropy < 60:
            f.write("🟡 Medium Entropy: Could be improved.\n")
        else:
            f.write("✅ High Entropy: Strong password.\n")

        if pwned:
            f.write("🚨 WARNING: This password has been leaked! Change it immediately.\n")
        else:
            f.write("✅ Safe: This password has not been found in leaks.\n")
    
    print("\n📜 Report saved as password_report.txt")

# Call save_report in analyze_password function
save_report(password, length, entropy, pwned)
