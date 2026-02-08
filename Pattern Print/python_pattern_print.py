""" 1. 
	*
	* *
	* * *
	* * * *
	* * * * *
"""
n = 6
for row in range(n):
    for col in range(row):
        print("* ", end='')
    print()

          
"=================================================="
"""
* * * * *
  *     *
    *   *
      * *
        *
"""

n = 5
for i in range(5):
    for j in range(5):
        if (i - j == 0) or (i == 0 or j == 4):
            print('*', end =' ')
        else:
            print(' ', end=' ')
    print()

"""" 3. 
    * * * *
      * *
    *   *
  *     *
*     """
for row in range(5):
	for col in range(5):
		if (row + col==4)or (row==0 or col==4):
			print("*" ,end=' ')
		else:
			print(end='  ')
	print()
print()