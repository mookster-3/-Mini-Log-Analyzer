Mini Log Analyzer (Python)



Description:

This project is a beginner Python program that analyzes a login log file.

It reads login attempt records and counts how many login attempts failed.



Purpose:

This project demonstrates basic programming concepts such as:

\- File input/output

\- Loops

\- Conditionals

\- String searching

\- Debugging and testing



Tools Used:

This project was developed with the assistance of AI-based programming guidance, similar to using online documentation or tutoring resources.



Files:

\- log\_analyzer.py: The Python program that analyzes the logs

\- login\_logs.txt: A sample log file used for testing

\- README.md: Project documentation



How It Works:

1\. The program opens a log file.

2\. It reads the file line by line.

3\. If a line contains the word "FAILED", it increases a counter.

4\. The final count is printed to the terminal.



Testing:

The program was tested using multiple log file scenarios including:

\- Mixed successful and failed logins

\- All successful logins

\- All failed logins



Upgrade 1:

The program was extended to count both failed and successful login attempts.



Upgrade 2:

The program was enhanced to track failed login attempts per user using a dictionary.

This simulates basic authentication log analysis used in cybersecurity and digital forensics.



Brute-Force Detection:

The program detects possible brute-force attacks by identifying users with three or more failed login attempts.

This simulates basic intrusion detection techniques used in cybersecurity.



Rapid Brute-Force Detection:

The program analyzes timestamps of failed login attempts to detect rapid brute-force attacks.

If a user fails to log in three times within a five-minute window, the activity is flagged as suspicious.



Learning Process:

This project was developed with guided assistance. I focused on understanding the overall logic,

testing the program with different inputs, and extending it with additional security features

such as brute-force detection.



Future Improvements:

\- Count successful login attempts

\- Identify users with repeated failed logins

\- Detect possible brute-force attacks

\- Output results to a report file



Author:

Mooki

