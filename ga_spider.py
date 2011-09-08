import threading, Queue, urllib, datetime, os, sys

def download(jobs):
    while True:
        url, name=jobs.get()
        
        #with report:
        print "Downloading ... %s\n" % name,
        if not os.path.isfile(name) or os.path.getsize(name) < 1024:
            urllib.urlretrieve(url, name)
                              
        jobs.task_done()

def main():
    jobs = Queue.Queue()
    for i in range(10):
        t = threading.Thread(target=download, args=(jobs))
        t.daemon = True
        t.start()

    d = datetime.date(1978, 6, 19)
    while d < datetime.date.today():
        jobs.put(("http://images.ucomics.com/comics/ga/%s/ga%s.gif"\
                  %(d.strftime("%Y"), d.strftime("%y%m%d")), \
                  "ga%s.gif" % d.strftime("%y%m%d")))
        d = d + datetime.timedelta(days = 1)
    jobs.join()

if __name__ == "__main__":
    main()
