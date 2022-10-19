#Gillian Bedward
#Average and Grade Assignment
def main():
    score1 = float(input("Score 1: "))
    score2 = float(input("Score 2: "))
    score3 = float(input("Score 3: "))
    score4 = float(input("Score 4: "))
    score5 = float(input("Score 5: "))
    return [score1, score2, score3, score4, score5]
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
