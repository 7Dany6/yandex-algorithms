from collections import defaultdict
with open('input.txt', 'r') as file_input:
    points = 0
    parties = []
    numbers = []
    final_result = []
    total = 0
    final = defaultdict(int)
    for line in file_input:
        *party, votes = line.split()
        points += int(votes)
        parties.append(party)
        numbers.append(int(votes))
    first_number = points / 450
    for num in numbers:
        final_result.append([num // first_number, num % first_number])
        total += num // first_number
    results = zip(parties, final_result)
    sort_list = sorted(results, key=lambda x: x[1][1], reverse=True)
    if total < 450:
        remaining_seats = 450 - total
        for par in range(0, int(remaining_seats)):
            sort_list[par][1][0] += 1
    for party in parties:
        for el in sort_list:
            if ' '.join(el[0]) == ' '.join(party):
                final[' '.join(party)] = int(el[1][0])
with open('output.txt', 'w') as output_file:
    for key, value in final.items():
        output_file.write("%s %s\n" % (key, value))