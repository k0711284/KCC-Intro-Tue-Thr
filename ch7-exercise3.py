from helpers import getNum

def getRainfallData():
    result = []
    months = ["April", "May", "June", "July"]
    for month in months:
        question = "Enter " + month + "'s rainfall total:"
        result.append(getNum(question, 0.0, 100.0))
    return result

def getSum(rainfall):
    sum = 0
    for num in rainfall:
       sum += num
    return sum

def getAverage(sum, count):
    return sum / count

def main():
   rainfall = getRainfallData()
   total = getSum(rainfall)
   average = getAverage(total, len(rainfall))
   print('The total rainfall is', format(total, ",.2f"), 'inches.')
   print('The average monthly rainfall is', format(average, ",.2f"), 'inches.')
   print('The most rainfall recorded in a month was', max(rainfall), 'inches.')
   print('The lowest rainfall recorded in a month was', min(rainfall), 'inches.')

main()