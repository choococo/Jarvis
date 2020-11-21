
import sys
import time

t = time.time()
time.sleep(5)

try:
    sys.exit(-1)

except SystemExit as e:
    print(1)
    print(e)
    print(time.time() - t)

