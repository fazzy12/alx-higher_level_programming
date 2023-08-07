#!/usr/bin/python3
import builtins
print(getattr(builtins, '__{0}__'.format(chr(97)), None).__doc__)

