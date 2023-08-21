"""
File: class_reviews.py
Name: Ian
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
# This constant controls when to stop
EXIT = -1

def main():
    """
    Step1: define the numbers of score and initial constants number of each class
    Step2: build a loop enable entering the class and score
    Step3: calculate the maximum, minimum, and average of each class' scores
    Step4: print the result
    """
    # Step1
    i = 0
    j = 0
    max_001 = -1
    min_001 = 11
    sum_001 = 0
    max_101 = -1
    min_101 = 11
    sum_101 = 0
    # Step2
    while True:
        classes = input('Which class? ')
        if classes == str(EXIT):
            break
        elif classes.upper() == "SC001":
            score_001 = int(input('Score: '))
            i += 1
            # Step3
            if max_001 <= score_001:
                max_001 = score_001
            if min_001 >= score_001:
                min_001 = score_001
            sum_001 += score_001
            avg_001 = sum_001 / i
        elif classes.upper() == "SC101":
            score_101 = int(input('Score: '))
            j += 1
            # Step3
            if max_101 <= score_101:
                max_101 = score_101
            if min_101 >= score_101:
                min_101 = score_101
            sum_101 += score_101
            avg_101 = sum_101 / j
    # Step4
    print('='*13 + 'SC001' + '='*13)
    if i == 0:
        print('No score for SC001')
    else:
        print('Max (001): ' + str(max_001))
        print('Min (001): ' + str(min_001))
        print('Avg (001): ' + str(avg_001))
    print('=' * 13 + 'SC101' + '=' * 13)
    if j == 0:
        print('No score for SC101')
    else:
        print('Max (101): ' + str(max_101))
        print('Min (101): ' + str(min_101))
        print('Avg (101): ' + str(avg_101))




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
