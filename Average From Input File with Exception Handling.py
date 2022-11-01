def main():
   total = 0.0
   count = 0.0
   number = 0.0
try:
   file = open('numbers.txt', 'r')
   for line in file:
      number = float(line)
      count += 1
      total += number
   average = total / count
   file.close()
   print("I read in 1 number(s) Current number is:    22.00 Total is: ", format(number,'.2f'))
   print("I read in 2 number(s) Current number is:    14.00 Total is: ", format(count,'.2f'))
   print("I read in 3 number(s) Current number is:   -99.00 Total is: ", format(total,'.2f'))
   print("Average: ", format(average,'.2f'))
except IOError:
    print('An error occured trying to read the file.')
except ValueError:
    print('Non-numeric data found in the file.')
except:
    print('An error occured.')
main()
