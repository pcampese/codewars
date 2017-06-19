# https://www.codewars.com/kata/regular-ball-super-ball/train/python

class Ball(object):
    """A class that defines the ball type"""
    
    # Initialize the class
    def __init__(self, ball_type=None):    # 'ball_type' attribute is not required, so set it to 'None'
        if (ball_type):                    # If the ball type is defined
            self.ball_type = ball_type     # Set it to whatever is provided during instantiation
        else:                              # if the ball type is NOT defined
            self.ball_type = "regular"     # Set it to the default value
			
# # Codewars Tests
# Test.assert_equals(Ball().ball_type, "regular")
# Test.assert_equals(Ball("super").ball_type, "super")