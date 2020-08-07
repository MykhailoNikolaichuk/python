a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

b = "Hello, World!"
# print(b[7:12])
# print(b[-2:5])


a = "Hello, World!"
# print(len(a))



# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
# print(a.replace("H", "J"))


a = "Hello, World!"
# print(type(a.split(","))) 


txt = "The rain in Spain stays mainly in the plain"
x = "ain"
# print(x in txt)


number = 3
cost = 160
waitTime = 90

text = ' misha ordered the {} pizzas which cost {} hryvnya\'s and he need to wait {} minutes'
# print(text.format(number, cost, waitTime));
print(text.strip().capitalize())