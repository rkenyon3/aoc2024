FILE_PATH = "/home/richardkenyon/projects/aoc2024/1/input.txt"

numbers = []
appearance_counts = {}

with open (FILE_PATH) as f:
    lines = f.readlines()

# make a list of numbers and a dict of how many times each appears in the right-hand list
for line in lines:
    if line.strip():
        a, b = line.strip().split()
        numbers.append(int(a))
        if int(b) in appearance_counts.keys():
            appearance_counts[int(b)] = appearance_counts[int(b)] + 1
        else:
            appearance_counts[int(b)] = 1

similarity_score = 0

for n in numbers:
    if n in appearance_counts:
        similarity_score += n * appearance_counts[n]

print(f"Similarity score: {similarity_score}")
