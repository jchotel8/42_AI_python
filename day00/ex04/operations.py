	# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jchotel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 16:55:34 by jchotel           #+#    #+#              #
#    Updated: 2020/03/10 17:54:02 by jchotel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	is_int(x):
	try :
		r = int(x)
		return (1)
	except ValueError :
		return (0)

if len(sys.argv) < 3 :
	print("InputError : too few arguments")
elif len(sys.argv) > 3 :
	print("InputError: too many arguments")
elif not is_int(sys.argv[1]) or not is_int(sys.argv[2]):
	#print(sys.argv[2])
	print("InputError: only numbers")
if len(sys.argv) != 3 or not is_int(sys.argv[1]) or not is_int(sys.argv[2]):
	print("Usage: python operations.py <number1> <number2>")
	print("Example")
	print("\tpython operations.py 10 3")
else :
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	print ("Sum:\t\t", x + y)
	print ("Difference:\t", x - y)
	print ("Product:\t", x * y)
	if y != 0 :
		print ("Quotient:\t", x / y)
		print ("Remainder:\t", x % y)
	else :
		print ("Quotient:\tERROR (div by zero)")
		print ("Quotient:\tERROR (modulo by zero)")
