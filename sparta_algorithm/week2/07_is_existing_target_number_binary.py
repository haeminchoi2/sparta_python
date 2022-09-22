finding_target = 8
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    if target in numbers:
        return 1
    else:
        return 0


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)