import os
import sys

# make two processes which run the same
# program after this instruction
pid = os.fork()

if pid < 0:
    print("fork failed", file=sys.stderr)
    sys.exit(1)

print(f"Hello world!, process_id(pid) = {os.getpid()}")
sys.exit(0)