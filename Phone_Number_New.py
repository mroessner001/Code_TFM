
import re
def phone_number_check(segment1, segment2):
    def find(segment):
        phone_nos = re.findall('[\+][\d]{2}[ ]?[\d]{3}[\d]{3}[\d]{4}', segment)
        print(phone_nos)
        return phone_nos
    phone_nos1 = find(segment1)
    phone_nos2 = find(segment2)
    if len(phone_nos1) > 0:
        if len(phone_nos1) == len(phone_nos2):
            for i in range(0, len(phone_nos1)):
                if phone_nos1[i] != phone_nos2[i]:
                    print("Phone Number found, But didn't match in segments")
            print("Phone number found and are matching")
        else:
            print("Phone Number found, But didn't match in segments")
    else:
        print("No Phone Number Found")

phone_number_check("hello+910123456789", "+910123456789 Hello")