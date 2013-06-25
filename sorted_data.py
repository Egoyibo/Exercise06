from sys import argv

script, file_name = argv

text = open(file_name)

text_lines = text.read()
final = text_lines.replace('\n', ' ')
print final

# for line in text:
	

# rest_list = text.readline()

# data = {"Arinell's" :4,
# "Pancho Villa":3,
# "Andalu":3,
# "Urbun Burger":1,
# "El Toro":5,
# "Casa Thai":2,
# "Taqueria Cancun":2,
# "Little Baobab":1,
# "Charanga":3,
# "Irma's Pampanga":5,
# "Bay Blend Coffee and Tea":3,
# "Giordano Bros":2
# }

# restaurant = sorted(data.items(), key = lambda x: x[0])

# for name, rating in restaurant:
# 	print "Restaurant %s is rated at %d" % (name, rating)