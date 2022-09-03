# Python Postgresql Connection Monitoring
# We would like to monitor postgres server status and write a syslog to track when accident happens 

## Future: Make it as a cron job to run this script.
# The cronjob also writes systemlog every 5 min but this can be modifeid depending on your system requirements.

## Additional Development for future: Delete line after certain days like every 7 days to refresh the log file and send the log into the desired log directory 
## Logging output: 
#Create a new log file!
#PSQL connection is valid at 11:03:46
#PSQL connection is valid at 11:03:55

import time
import socket
from pathlib import Path
#cron = cronTab(user='root')
# Setting cron job interval for every 5 min
#cron.setall('* /5 * *  *')
 
port=5432
FILE='/Users/rickyyang/log/psql_metrics.txt'                                                                                                                                                          
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('localhost',port))
    print("Port " + str(port) + " connection is valid!")
    #subprocess.check_output('SELECT current_database();', shell=True)
    #connect =os.system('/Applications/Postgres.app/Contents/Versions/13/bin/psql -p5432 "postgres"')
    my_file = Path("/Users/rickyyang/log/psql_metrics.txt")
    if my_file.is_file():
        print("Writing to the log file...")
    else:
        with open(FILE, 'w') as f:
            f.write('Create a new log file!\n')

    file = open(FILE,'a+')
    file.write('PSQL connection is valid at '+ time.strftime("%H:%M:%S")+'\n')
    file.close()
    s.close()
except socket.error as ex:
    print("Connection failed with errno {0}: {1}".format(ex.errno, ex.strerror))            


