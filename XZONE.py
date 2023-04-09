import os, sys

try:

    __import__("zone").main()

except Exception as e:

    exit(str(e))
