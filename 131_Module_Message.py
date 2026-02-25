credit = 10

def sendsms(mobile_no, message):
    global credit
    credit -= 2

def sendWhatmsg(mobile_no, message):
    global credit
    credit -= 1.5

def sendEmail(email, message):
    global credit
    credit -= 1

def increaseCredit(points):
    global credit
    if points > 0:
        credit += points