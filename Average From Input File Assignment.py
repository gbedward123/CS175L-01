def main():
   total = 0.0
   count = 0.0
   number = 0.0
   file = open('numbers.txt', 'r')
   for line in file:
      number = float(line)
      count += 1
      total += number
      print("I read in "+str(count)+" number(s) Current number is:    "+str(number)+" Total is: "+format(number,'.2f'))
   average = total / count
   file.close()
   print("Average: ", format(average,'.2f'))
main()
