# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jchotel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 14:03:44 by jchotel           #+#    #+#              #
#    Updated: 2020/03/10 14:18:29 by jchotel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2 :
	print("ERROR : too many args")
else :
	try: 
		truc = int(sys.argv[1])
		if truc == 0 :
			print("I'm Zero")
		elif truc % 2 :
			print("I'm Odd")
		else :
			print("I'm Even")
	except ValueError :
		print("ERROR : not int")

