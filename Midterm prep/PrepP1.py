

def payRollStatement(name, numHrsWorked, payRate, fHoldingRate, sHoldingRate):
    print("Employee Name: " + name)
    print("Hours Worked: " + str(numHrsWorked))
    print("Pay Rate: " + str(payRate))
    print("Gross Pay: " + eval(int(numHrsWorked * payRate)))
    print("Deductions: ")
    fedHoldAmount = fHoldingRate * payRate
    stateHoldAmount = sHoldingRate * payRate
    print("Federal Withholdings ({fHoldingRate}) : " + fedHoldAmount)
    print("Federal Withholdings ({sHoldingRate}) : " + stateHoldAmount)
    print("Total Deductions: " + eval(fedHoldAmount + stateHoldAmount))
    print("Net Pay: " + eval((numHrsWorked * payRate) -
          (fedHoldAmount + stateHoldAmount)))


name, numHrsWorked, payRate, fHoldingRate, sHoldingRate = input(
    "Enter in your values:").split()

payRollStatement(name, numHrsWorked, payRate, fHoldingRate, sHoldingRate)
