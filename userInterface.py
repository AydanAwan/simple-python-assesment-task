"""the user interface which where users can interact with our code and do calculations."""


from interface import interface

endCalcs = True
while endCalcs:
    usertake = input("please enter the data list you wish to work on by entering a list of numbers seperated by a comma or enter \" default \" if you wish to use the default data lsit")
    if usertake == "default":
        inter_current = interface(usertake)
    elif not usertake:
        raise IndexError("there are no values in your data list")
    else:
        try:
            workingDataList = list(map(float, usertake.split(',')))
            inter_current = interface(workingDataList)
        except ValueError:
            raise ValueError("a value has been added that is not a real number")
        except Exception as e:
            print(e)
    endWorkingDataList = True
    while endWorkingDataList:
        chooseCalc = input("input what analysis you wish to see. the list is: length, sort, count, sum, average, median, min, max, range, variance, meanDeviation, standardDeviation, or data to input a new data set, or end to end the pogramme")
        match(chooseCalc):
            case "length":
                print(inter_current.find_length())
            case "sort":
                print(inter_current.find_sort())
            case "count":
                countVariable = input("enter the value you wish to get the count of")
                try:
                    countNumber = float(countVariable)
                    print(inter_current.find_count(countNumber))
                except ValueError:
                    print("the value you entered isnt a real number")
            case "sum":
                print(inter_current.find_sum())
            case "average":
                print(inter_current.find_average())
            case "median":
                print(inter_current.find_median())
            case "min":
                print(inter_current.find_min())
            case "max":
                print(inter_current.find_max())
            case "range":
                print(inter_current.find_range())
            case "variance":
                print(inter_current.find_variance())
            case "meanDeviation":
                print(inter_current.find_meanDeviation())
            case "standardDeviation":
                print(inter_current.find_standardDeviation())
            case "data":
                break
            case "end":
                endCalcs = False
                break
            case _:
                print("invalid operation please pick from the list provided")
