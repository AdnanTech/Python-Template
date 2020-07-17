

from datetime import datetime
start_time = datetime.now()

def initialize():
    print('Starting')

initialize()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))