#Gillian Bedward
#Average and Grade Assignment
def main():
    score1,score2,score3,score4,score5=input_scores()
    calc_average(score1,score2,score3,score4,score5)
def input_scores():
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))
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
def calc_average(score1,score2,score3,score4,score5):
    average = (score1+score2+score3+score4+score5) / 5
    grade = determine_grade(average)
    print("Average Score: {:.1f} {}".format(average, grade))
    print("Score            Numeric Grade          Letter Grade")
    print("score 1: ","           ", score1, "                 ",determine_grade(score1))
    print("score 2: ","           ", score2, "                 ",determine_grade(score2))
    print("score 3: ","           ", score3, "                 ",determine_grade(score3))
    print("score 4: ","           ", score4, "                 ",determine_grade(score4))
    print("score 5: ","           ", score5, "                 ",determine_grade(score5))
    print("Average score: ","     ", average, "                 ",determine_grade(average))
def show_letters(num, letter_grade):
    print("{:.1f} {}".format(num, letter_grade))
another_calculation = 'yes'
while another_calculation == 'yes':
    last = main()
    for n in last:
        show_letters(n, determine_grade(n))
        calc_average(last)
        another_calculation = input("Enter 'yes' if you would like to do another calculation: ")
