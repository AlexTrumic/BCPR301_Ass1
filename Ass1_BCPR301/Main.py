from Controller import *
import sys

b = Model_Handler(sys.argv[1])
Controller(b).Go()