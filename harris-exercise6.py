from helpers import getNum
from random import randint

def findAllGreaterThanNumbers( listOfNumbers, userNumber ):
      greaterThanNumbersList = []

      for currentNumberIndex in range( len( listOfNumbers ) ):
            if listOfNumbers[ currentNumberIndex ] > userNumber:
                  greaterThanNumbersList.append( listOfNumbers[ currentNumberIndex ] )

      return greaterThanNumbersList

def getUserNumber():
      userNumber = int( input( "Enter a number: " ) )
      return userNumber

def displayValuesInList( anyList ):
      for currentValueIndex in range( len( anyList ) ):
            if currentValueIndex == len( anyList ) - 1:
              print( anyList[ currentValueIndex ], end = "." )
            else:
              print( anyList[ currentValueIndex ], end = ", " )            

def main():
      listOfNumbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
      
      userNumber = getUserNumber()
      
      greaterThanNumbersList = findAllGreaterThanNumbers( listOfNumbers, userNumber )

      if len( greaterThanNumbersList ) < 1:
            print( "There are no numbers greater than", userNumber, "in this list" )
      else:
            displayValuesInList( greaterThanNumbersList )
      
main()