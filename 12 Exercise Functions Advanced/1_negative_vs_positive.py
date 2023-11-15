def positives_and_negatives_sums(*args):
    positives = 0
    negatives = 0
    for i in args:
        if i > 0:
            positives += i
        else:
            negatives += i
    return positives, negatives


numbers = [int(x) for x in input().split()]

print(positives_and_negatives_sums(*numbers)[1])
print(positives_and_negatives_sums(*numbers)[0])
if positives_and_negatives_sums(*numbers)[0] > abs(positives_and_negatives_sums(*numbers)[1]):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
