# Write your solution here
import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    now = datetime.datetime.now()

    try:
        year = int(pic[4:6])
        if year == 0:
            year = 2000
        valid_datetime = datetime.datetime(year, int(pic[2:4]), int(pic[0:2]))
    except ValueError:
        return False
    
    century_marker = pic[6]

    if century_marker == "+":
        if not (valid_datetime.year <= 99):
            return False
    elif century_marker == "-":
        if not (valid_datetime.year <= 99):
            return False
    elif century_marker == "A":
        if not (valid_datetime.year <= now.year):
            return False
    
    selection_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    personal_identifier = pic[7:10]
    control_char = pic[0:6]+personal_identifier
    control_char = int(control_char) % 31
    if selection_chars[control_char] != pic[10]:
        return False
    
    return True


if __name__ == "__main__":
    is_it_valid("100400A644E")
    # is_it_valid("120488+246L")
    # is_it_valid("310823A9877")