def duplicate_count(text):
    # Your code goes here
    register = []
    count = 0
    for i in text:
        if i not in register:
            register.append(i)
        else:
            count += 1
    return count

print(duplicate_count("Lambidii"))