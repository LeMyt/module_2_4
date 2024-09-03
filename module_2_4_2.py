numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes =[]

for i in range(1, len(numbers)):
    is_prime = False
    index = 2
    while index < numbers[i] + 1:
        if numbers[i] % index == 0 and numbers[i] != index:
            is_prime = True
            index = 2
            break
        else:
            index += 1
            continue

    if is_prime:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])


print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')