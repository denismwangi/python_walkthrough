# checks string to see whether or not it is blank.
# If so, it returns True, if not it return false
def is_field_blank(name):
    if name and name.strip():
        # name is not None AND string is not empty or blank
        return False
        # name is None OR string is empty or blank
    return True


# receives a string and checks to see whether or not it is a number.
# If so, it returns True, if not it return False.
def is_field_a_number(num):
    if num.isdigit():
        return False
    # else returns
    return True
