#convert Minutes into hours
minutes = int(input("Enter Minutes :"))
# 2 hours 30 minutes
hours = minutes // 60
minute = minutes % 60
print(f"{hours} Hours {minute} Minutes")
