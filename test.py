import datetime, time, os
from api.browserstack import API, Browser, Worker

bs_api = API(username = os.environ['BROWSERSTACK_USER'], access_key = os.environ['BROWSERSTACK_ACCESS_KEY'])

print bs_api.status()

print "\nOSs"
print bs_api.browsers().keys()

print "\nWorkers"
print bs_api.workers()

print "\nCreating new worker ..."

browser = Browser('Windows', '7', 'chrome', 14.0)

worker = bs_api.spawn(browser, "http://github.com/404", "BS Test: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print worker

print "\nCreated new worker ..."
print "\nWorker Status:" 
print status = worker.status()

# while status['status'] != 'queue':
# 	time.sleep(15)
# 	status = worker.status()

# print "\nWorker running ..."
# print "\nSaving worker screenshot ..."



print "\nDeleting new worker ..."
print worker.terminate()

print "\nDeleted new worker ..."
print "\nWorker Status:" 
print worker.status()


print bs_api.status()
