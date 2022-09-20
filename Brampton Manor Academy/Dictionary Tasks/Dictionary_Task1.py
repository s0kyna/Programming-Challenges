def splitDate():
  months = {"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}
  date = input("Enter date (DD-MMM-YY): ")
  date = date.split("-")
  date[1] = months[date[1]]
  return tuple(date)
if __name__ == '__main__':
  print(splitDate())
