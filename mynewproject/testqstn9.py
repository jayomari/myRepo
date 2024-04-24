import my_modules #imports the entire module into the source file
import platform
my_modules.addNumbers(2,2)

my_modules.subtract(120,3)

my_modules.power(5,5)

from my_modules import addNumbers, power

addNumbers(19,3)
power(4,4)



#in-built modules
#platform module
test1 = platform.system
print(test1())

test2 = platform.release

print(test2())

