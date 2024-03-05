
from datetime import datetime


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    address = "test_auto" + time_stamp + "@gmail.com"
    
    return address