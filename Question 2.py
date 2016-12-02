def calc_trail_zeros(fact_n):
    """this function returns the trailling 0s of any factorial number"""
    power_root = 0
    numb_trail_zeros = 0
    s = fact_n / (5 ** power_root)
    while ((fact_n / (5 ** power_root)) >=1):
        # continously going to keep doing it, until a number less than one
        power_root = power_root + 1
        numb_trail_zeros = numb_trail_zeros + int((fact_n / (5 ** power_root)))

    return numb_trail_zeros
#total of all numbers in divions, will give number of trailing 0s
print(calc_trail_zeros(5555))
