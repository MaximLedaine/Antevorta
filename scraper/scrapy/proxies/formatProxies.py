import csv


# results = []
# with open('inputfile.txt') as inputfile:
#     for line in inputfile:
#         results.append(line.strip().split(','))

results = []
with open('proxies.txt', newline='') as inputfile:
    for line in inputfile:
        results.append(line.strip())

open("proxies.txt", "w").close()

for row in results:
    with open("proxies.txt", "a") as text_file:
        print(f"http://{row}", file=text_file)