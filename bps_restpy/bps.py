import sys,os
#sys.path.insert(0,os.path.abspath(__file__+"/../.."))
if sys.version_info[0] >= 3:
    from .restPyWrapper3 import BPS, pp
else:
	from .restPyWrapper import BPS, pp