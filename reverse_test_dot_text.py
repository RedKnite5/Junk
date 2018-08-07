from sys import argv

script, a_weird_name = argv

def wind(t):
	letter_number = 30
	print "wind letter_number"
	print type(letter_number)
	t.seek(letter_number)
	return letter_number
	
def rewind(t, c_number):
	t.seek(c_number)
	
def read_current_line(t):
	print t.readline()

def back_line(t, line_number_times_ten):
	print "backline line_number_times_ten"
	print type(line_number_times_ten)
	line_number_times_ten = int(line_number_times_ten) - 10
	return line_number_times_ten

current_file = open(a_weird_name)

charactor_number = wind(current_file)

charactor_number = back_line(current_file, charactor_number)

print charactor_number
read_current_line(current_file)

charactor_number = back_line(current_file, charactor_number)

print charactor_number
read_current_line(current_file)