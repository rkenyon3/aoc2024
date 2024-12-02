
FILE_PATH = "/home/richardkenyon/projects/aoc2024/1/input.txt"

def get_lists():
    with open(FILE_PATH) as f:
        l1 = []
        l2 = []
        lines = f.readlines()
        for line in lines:
            if line.strip():
                a, b = line.strip().split()
                l1.append(int(a))
                l2.append(int(b))

        l1.sort()
        l2.sort()
        return l1, l2

def main():
    l1, l2 = get_lists()
    total = 0
    while(l1):
        min1 = l1.pop(0)
        min2 = l2.pop(0)
        total += abs(min1 - min2)

    print(f"The total is: {total}")

main()
