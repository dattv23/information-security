print("Enter lines of text (Enter 'Done' to finish): ")
lines: list[str] = []
while True:
    line = (
        input()
    )  # The str() conversion is unnecessary because input() returns a string.
    if line.lower() == "done":
        break
    lines.append(line)

print("The entered lines after converting to uppercase: ")
for line in lines:
    print(line.upper())
