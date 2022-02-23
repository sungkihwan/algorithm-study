from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

tmp1 = Counter(participant)
tmp2 = Counter(completion)

print(tmp1-tmp2)

print(tmp2-tmp1)

string = "tars"

print("".join(sorted(string)))

print(tmp2.values())
