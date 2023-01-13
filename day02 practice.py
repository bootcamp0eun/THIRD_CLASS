#연습문제 2번


subject = "cherry"
small = True
green = False
if small:
    if green:
        print(f"{subject} is small and green")
    else:
        print(f"{subject} is small but not green")
else:
    if green:
        print(f"{subject} is big and green")
    else:
        print(f"{subject} is big and not green")