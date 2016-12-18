F = open('input.txt', 'w')
F.write('Hello\nWorld')
F.close()
lines = []
for line in open('input.txt'):
    lines.append(line.rstrip())
print(lines)
