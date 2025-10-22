numbers = {
    "numb1":23,
    "numb2":45,
    "numb3":51
}
def sub(a, b):
    result_substraction = numbers[a]-numbers[b]
    return result_substraction
answer = sub("numb3", "numb1")
print(answer)
assert answer == 28, "The substraction's answer is wrong!"
