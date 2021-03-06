"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Hao Jiang.
"""
###############################################################################
# TODO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
bryan = rg.SimpleTurtle('turtle')
bryan.pen = rg.Pen('midnight blue', 3)
bryan.speed = 20
size1 = 100
liw4 = rg.SimpleTurtle('turtle')
liw4.pen = rg.Pen('green', 3)
liw4.speed = 20
size2 = 100
for k in range(25):
    bryan.draw_square(size1)
    bryan.pen_up()
    bryan.right(45)
    bryan.forward(10)
    bryan.right(45+k)
    bryan.pen_down()
    liw4.draw_circle(size2)
    liw4.right(14.4)
    size1 = size1 - 2
window.close_on_mouse_click()