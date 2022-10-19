#Gillian Bedward
#Average and Grade Assignment
def main():
    score_one = float(input("Score 1: "))
    score_two = float(input("Score 2: "))
    score_three = float(input("Score 3: "))
    score_four = float(input("Score 4: "))
    score_five = float(input("Score 5: "))
    return [score_one, score_two, score_three, score_four, score_five]
def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade
def calc_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("Average Score: {:.1f} {}".format(average, grade))
def show_letters(num, letter_grade):
    print("{:.1f} {}".format(num, letter_grade))
another_calculation = 'yes'
while another_calculation == 'yes':
    lst = main()
    for n in lst:
        show_letters(n, determine_grade(n))
    calc_average(lst)
    another_calculation = input("Enter 'yes' if you would like to do another calculation: ")
