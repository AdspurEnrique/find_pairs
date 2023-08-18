def find_pairs(listOfNumbers, target):
    seen = set()
    pairs = []
    for n in listOfNumbers:
        complement = target - n
        if complement in seen:
            pairs.append((n, complement))
        seen.add(n)
    return pairs

