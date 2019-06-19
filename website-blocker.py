import time
from datetime import datetime as dt


hosts_path ="C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now():
        print("Working Hours")

    else:
        print("Working Hours")
    time.sleep(5)