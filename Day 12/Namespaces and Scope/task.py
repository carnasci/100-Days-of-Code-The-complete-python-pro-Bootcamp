enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def is_prime(num):
    numbers = []
    for i in range(1, (num + 1)):

        if num % i == 0:
            numbers.append(i)

    if len(numbers) == 2:
        return True
    else:
        return False


print(is_prime(73))

print(is_prime(75))