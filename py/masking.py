
phone = "7396610166" 
masked = "******" + phone[-4:]
print(masked)


email = "ravi@example.com" 
username, domain = email.split("@") 
masked = username[0] + "***@" + domain 
print(masked)