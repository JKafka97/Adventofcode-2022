from collections import defaultdict

file1 = open('.\\7_day\\text.txt', 'r')
Lines = ("\n" + file1.read().strip()).split("\n$ ")[1:]

path = []

dir_sizes = {}
children = defaultdict(list)

for block in Lines:
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])
        continue
    abspath = "/".join(path)
    assert op == "ls"

    sizes = []
    for line in outputs:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dir_name}")

    dir_sizes[abspath] = sum(sizes)

def dfs(abspath):
    size = dir_sizes[abspath]
    for child in children[abspath]:
        size += dfs(child)
    return size

ans = 0
for abspath in dir_sizes:
    if dfs(abspath) <= 100000:
        ans += dfs(abspath)

print(ans)