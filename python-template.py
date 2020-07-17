from datetime import datetime

start_time = datetime.now()

def initialize():
    print('Starting')

def main():
    print('Code goes here')

initialize()
main()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))