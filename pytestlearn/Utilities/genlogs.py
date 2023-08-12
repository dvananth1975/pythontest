import logging

logging.basicConfig(filename="..\Logs\\logfile.log",format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

log=logging.getLogger()
log.info("first log)")