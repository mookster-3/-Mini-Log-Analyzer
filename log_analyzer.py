# Open the log file
file = open("login_logs.txt", "r")

# Store failed login times per user
failed_times = {}

# Read file line by line
for line in file:
    if "FAILED" in line:
        parts = line.split()

        date = parts[0]
        time = parts[1]
        timestamp = date + " " + time

        for part in parts:
            if part.startswith("user="):
                user = part.replace("user=", "")

                if user not in failed_times:
                    failed_times[user] = []

                failed_times[user].append(timestamp)

file.close()

# Print failed attempts per user
print("Failed login timestamps per user:")
print("---------------------------------")

for user in failed_times:
    print(user + ":", failed_times[user])

# Rapid brute-force detection
print("\n⚠️ Rapid brute-force detection:")

attack_found = False

for user in failed_times:
    times = failed_times[user]

    if len(times) >= 3:
        first_time = times[0]
        last_time = times[2]

        first_minutes = int(first_time[11:13]) * 60 + int(first_time[14:16])
        last_minutes = int(last_time[11:13]) * 60 + int(last_time[14:16])

        if last_minutes - first_minutes <= 5:
            print("User:", user, "- 3 failed attempts within 5 minutes")
            attack_found = True

if not attack_found:
    print("No rapid brute-force attacks detected.")
