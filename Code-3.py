import os
import sys

def forkexample():
    p = os.fork()
    
    if p < 0:
        print("fork fail", file=sys.stderr)
        sys.exit(1)
    
    # child process because return value zero
    elif p == 0:
        print("Hello from Child!")
    
    # parent process because return value non-zero.
    else:
        print("Hello from Parent!")

if __name__ == "__main__":
    forkexample()
