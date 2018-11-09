import random
import itertools

class Dice(object):

    def __init__(self, dnumber=6):
        self.dnumber = dnumber

    def roll(self, n=1):
        for _ in range(n):
            yield random.randint(1, self.dnumber+1)

    def possibilities(self, n=1):
        return list(itertools.combinations_with_replacement(range(1, self.dnumber+1), n))

def possible_rolls(amount_of_dice=1, min_value= 1, max_value=6):
    return list(itertools.combinations_with_replacement(range(min_value, max_value+1), amount_of_dice))

def outcomes(possible_rolls):
    from collections import defaultdict

    tally = defaultdict(int)
    for roll in possible_rolls:
        tally[sum(roll)] += 1

    return tally

roll_n = lambda n, d_max=6: outcomes(possible_rolls(n, max_value=d_max))

def distribution(outcomes):
    spacing = ' ' * max([len(str(k)) for k in outcomes.keys()])
    height = max(outcomes.values()) // 2
    print('')
    for y in reversed(range(height + 1)):
        chart_row = ''
        for value, frequency in sorted(outcomes.items()):
            difference = frequency - 2 * y
            if difference > 1:
                chart_row += ':'
            elif difference > 0:
                chart_row += '.'
            else:
                chart_row += ' '
            chart_row += spacing
        print(chart_row)
    print(' '.join([(str(k) + (' ' if len(str(k)) != len(spacing) else '')) for k in outcomes.keys()]))

if __name__ == '__main__':
    distribution(roll_n(2, 20))
    distribution(roll_n(3))
    d = Dice(20)
    print(list(d.roll()))