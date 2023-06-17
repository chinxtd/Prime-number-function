# return list of prime number from range of input
def range_of_prime_number(start_num, end_num):
    prime_result = []
    for i in range(start_num, end_num+1):
        divisor = 0
        for j in range(1, i+1):
            if i % j == 0 :
                divisor += 1
        # if that number has only 2 divisor so it's prime number                
        if divisor == 2 : 
            prime_result.append(i)
    return prime_result

# write the result to specified files
def write_to_text(to_write, target_path):
    for i in to_write:
        with open(target_path, "a") as write:
            write.write(f"{str(i)}\n")

"""
Display all the prime numbers between 1 to 250.
Store the results in a results.txt file.
"""
write_to_text(range_of_prime_number(1,250), "result.txt")
