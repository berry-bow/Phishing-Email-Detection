print("=== Phishing Email Detection ===")

print("Paste the email content (type END on a new line when finished):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

email = "\n".join(lines)

keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click",
    "login",
    "account",
    "winner",
    "prize",
    "free",
    "suspended"
]

score = 0

for word in keywords:
    if word.lower() in email.lower():
        score += 1

print("\n=== Result ===")

if score >= 3:
    print("⚠️ Phishing Email Detected")
else:
    print("✅ Email Appears Safe")

print(f"Matched suspicious keywords: {score}")