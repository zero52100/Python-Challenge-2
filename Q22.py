def divide_num(dividend,divisor):
    try:
        result = dividend  / divisor
        print(result)
    
    except ZeroDivisionError:
        print("divisor Number Should Not Be Zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

try:
    dividend  = int(input("Enter dividend  Value: "))
    divisor = int(input("Enter divisor Value: "))
    divide_num(dividend, divisor)

except ValueError :
    print(f"ValueError:Invalid Input. Please Input Integer Only")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
