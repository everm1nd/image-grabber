from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

from workers.grabber import grab

result = q.enqueue(
             grab, 'http://www.pornhub.com/')
