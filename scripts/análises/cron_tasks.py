__author__ = 'nolram'

from plan import Plan


cron = Plan("command_crawler", path='/home/nolram/Github/Django/NewsReaderDjango')
cron.command('/home/nolram/Github/Django/NewsReaderDjango/cron_job.sh', every='10.minute')

if __name__ == "__main__":
    cron.run("check")
