import sys
 
print "Welcome to the FizzBuzz project!"
print "*For reference, the file name is: {}".format(sys.argv[0])
print "Background information alert: You supplied {} arguments at run time.  Intriguing, right?! ".format(len(sys.argv))
 
for arg in sys.argv[1:]:
    print arg    
 
my_input = raw_input("Directions: Enter the largest FizzBuzz number to query, then click 'Enter.' The outcome will be a FizzBuzz commentary of each number; thus, don't go nuts and type 9999 etc as each number is analyzed i.e. prints on a separate line, and will take a long duration to run.  Ok, ready? Type that number: ")
print my_input
 
count = 0
while count < int((my_input) or (arg)):
	if count % 5 == 0 and count % 3 == 0:
		print "fizzBuzz"
	elif count % 3 == 0:
		print "Fizz"
	elif count % 5 == 0:
		print "Buzz"
	else:
		print "Fizz Buzz counting up to {}".format(str(count))
		
	count = count + 1
