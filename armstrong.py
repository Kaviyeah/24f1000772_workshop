num = int(input("Enter a number: "))

digits = len(str(num))
total = 0

for d in str(num):
    total += int(d) ** digits

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
