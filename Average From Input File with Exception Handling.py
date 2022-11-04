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
   print("I read in "+str(count)+" number(s) Current number is:    "+str(number)+" Total is: "+format(number,'.2f'))
   print("Average: ", format(average,'.2f'))
except IOError:
   print('An error occured trying to read the file.')
except ValueError:
   print('Non-numeric data found in the file.')
except:
   print('An error occured.')
main()
