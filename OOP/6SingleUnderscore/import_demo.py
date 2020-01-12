'''
import underscore_demo  # This style will import everything normally
print(underscore_demo._secret)  # Accessing protected member
print(underscore_demo.not_a_secret)  # Can be access normally
'''


'''
from underscore_demo import *  # This style won't import _NAME member
# print(_secret)  # Can't be access
print(not_a_secret)
# print(_rectangle(5,6))  # Can't be access
print(circle(5))
Alpha.foo()
# _Beta.foo()  # Can't be access
'''

# When import manually, you can still gain the access back
from underscore_demo import Alpha, _Beta, _rectangle, circle, _secret, not_a_secret
print(_secret)  # Now can be access
print(not_a_secret)
print(_rectangle(5, 6))  # Now can be access
print(circle(5))
Alpha.foo()
_Beta.foo()  # Now can be access

