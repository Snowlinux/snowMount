# Meant to parse fstab
# Seperate content into different columns
# For now it's the whole file.

# DOES NOT WORK, IN NEED OF PEOPLE TO EDIT
file = open(r'/etc/fstab', 'r').readlines()
for line in logfile:
	print line

