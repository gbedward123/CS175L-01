def main():
    import matplotlib.pyplot as plot
    try:
        expenses = ["1000", "250", "350", "200", "375", "800"]
        categories = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]
        function = open("expenses.txt", "r+")
        function.writelines(categories)
        function.writelines(expenses)
        function.readlines()
        function.readlines()
        plot.pie (expenses, labels = categories, startangle = 90, autopct = '%.1f%%')
        plot.title ('Monthly Expenses')
        plot.show()
        function.close()
    except OSError as error:
        print("OSError:", error)
    except ValueError as error:
        print("ValueError:", error)
    except Exception as error:
        print(f"Unexpected {error=}, {type(error)=}")
main()
