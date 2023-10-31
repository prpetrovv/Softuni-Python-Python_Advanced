def matching_par(given_string):
    openings = []
    for index, char in enumerate(given_string):
        if char == "(":
            openings.append(index)
        elif char == ")":
            print(given_string[openings.pop():index + 1])


matching_par(input())
