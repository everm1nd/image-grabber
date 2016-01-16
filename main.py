from redis import Redis
from rq import Queue
from workers.grabber import grab
import sys

q = Queue(connection=Redis())

start = 0
stop  = 10

if len(sys.argv) > 2:
    start = sys.argv[1]
    stop  = sys.argv[2]

for n in range(start,stop):
    result = q.enqueue(grab, 'http://www.pornhub.com/video?page=' + str(n+1))
    print("Pushed queue: " + str(result))
