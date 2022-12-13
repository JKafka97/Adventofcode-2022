file1 = open('.\\10_day\\text.txt', 'r')
lines = file1.read().strip().split("\n")

X = 1
op = 0

ans = 0
interesting = [20, 60, 100, 140, 180, 220]

for line in lines:
    parts = line.split(" ")

    if parts[0] == "noop":
        op += 1

        if op in interesting:
            ans += op * X

    elif parts[0] == "addx":
        V = int(parts[1])
        X += V

        op += 1

        if op in interesting:
            ans += op * (X - V)

        op += 1

        if op in interesting:
            ans += op * (X - V)


print(ans)