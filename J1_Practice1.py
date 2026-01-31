# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#5  (Packages delivered)
#2  (Collisions)
'''
The Scenario: A robot droid is delivering packages while trying to avoid obstacles.

You gain 50 points for every package delivered.

You lose 10 points for every collision with an obstacle.

The Bonus: If the number of packages is greater than the number of collisions, you get a massive 500-point bonus.
'''

delivered=50
collision= 10
number_of_c= 609985
number_of_d= 400345765432
extra=500
total=(number_of_d*delivered) - (number_of_c*collision)
if number_of_d > number_of_c:
    total= total +extra
else: #number_of_d < number_of_c and number_of_d = number_of_c:
    total = total -20
    
print("total=",total)