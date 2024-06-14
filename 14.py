
lines = []
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if not line:
        break
    lines.append(line)
print("\n".join(lines))
