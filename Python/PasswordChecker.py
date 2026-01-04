import math
import re

COMMON_PATTERNS = [
    r'123', r'abc', r'qwerty',
    r'password', r'letmein', r'admin'
]

def estimate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)


def password_strength(password):
    score = 0
    issues = []

    length = len(password)
    unique_ratio = len(set(password)) / max(length, 1)

    score += min(length * 0.8, 10)

    entropy = estimate_entropy(password)
    score += min(entropy / 20, 5)

    if unique_ratio < 0.5:
        score -= 3
        issues.append("Too many repeated characters")

    if re.match(r'[A-Z][a-z]+[0-9!@#]*$', password):
        score -= 2
        issues.append("Common capitalization pattern")

    for pattern in COMMON_PATTERNS:
        if re.search(pattern, password.lower()):
            score -= 3
            issues.append("Contains common pattern")
            break

    if length < 8:
        score -= 4
        issues.append("Too short")

    score = max(0, min(round(score), 10))

    return {
        "score": score,
        "issues": issues
    }


if __name__ == "__main__":
    passwd = input("Input a password: ")
    result = password_strength(passwd)

    print("Strength:", result["score"])
    if result["issues"]:
        print("Issues:")
        for issue in result["issues"]:
            print("-", issue)
