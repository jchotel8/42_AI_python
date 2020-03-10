# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jchotel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 14:19:10 by jchotel           #+#    #+#              #
#    Updated: 2020/03/10 16:54:20 by jchotel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(string) :
	if not string :
		string = input("What is the text to analyse ?")
	spaces = 0
	upper = 0
	lower = 0
	punctu = 0
	for c in string :
		if c == ' ':
			spaces += 1
		if c.isupper():
			upper += 1
		if c.islower():
			lower += 1
		if c in string.punctuation :
			punctu += 1
	print("- ", upper, " upper letters")
	print("- ", lower, " lower letters")
	print("- ", punctu, " punctuation marks")
	print("- ", spaces, " spaces")


