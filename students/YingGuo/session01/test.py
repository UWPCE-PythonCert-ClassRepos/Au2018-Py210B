print("This is puzzle solving under visual studio code")
def sleep_in(weekday, vacation):
  if weekday == True and vacation == True:
      print("sleep more!")
  if weekday == True and vaction == False:
      print("get up and work!")
  if weekday == False:
      print("enjoy weekend and sleep in")

"""Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;"""
def front_times(str, n):
    if len(str) >= 3:
        return str[:3]*n
        #isn't python zero index? why not [0:2]
    return str*n

