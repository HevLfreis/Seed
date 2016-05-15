activate_this = '/home/hevlfreis/projects/Seed/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from home import app as application

import sys
sys.path.insert(0, '/home/hevlfreis/projects/Seed')