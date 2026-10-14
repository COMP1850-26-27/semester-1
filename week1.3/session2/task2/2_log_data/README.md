# Log Data Filtering

Log files are provided by websites to track different http requests and where they come from. 
This is useful for blocking disruptive IP addresses, tracking failed login attempts, and handling DDOS attacks.

`site.log` is an example of a log file. Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code.

1. We want to find all failed login attempts in a log file based on Request and Status code (i.e., `POST /login` with the response `401`) and print these out in a human-readable format.  

2. Edit `log_data.py` to add lines to:

    - Open and read the content of `site.log`
    - Fine all failed login attempts
    - Print the failed login attemps in the format 
    
        `IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20`


Hints:
- Remember to handle file errors
- The first row is headers - you'll need to skip it
- Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
- You need to find rows where Request = `POST /login` AND Status_Code = `401`
- You can use list comprehension or loops to filter the data