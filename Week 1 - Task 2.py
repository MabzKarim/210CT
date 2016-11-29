def calculating_trailing_zeros(factorial_n):
    """this function returns the trailling 0s of any factorial number"""
    power_root = 0
    number_trailing_zeros = 0
    s = factorial_n / (5 ** power_root)
    while ((factorial_n / (5 ** power_root)) >=1):
        power_root = power_root + 1
        number_trailing_zeros = number_trailing_zeros + int((factorial_n / (5 ** power_root)))

    return number_trailing_zeros

print(calculating_trailing_zeros(5555))
