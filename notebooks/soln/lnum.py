%%file lnum.py
#!/usr/bin/env python
import sys
for i, line in enumerate(sys.stdin.readlines()):
    print i+1, ':', line,
    
print '\n---- END ---'