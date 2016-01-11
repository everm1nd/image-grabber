from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

from workers.grabber import grab

result = q.enqueue(
             grab, 'https://pixabay.com/en/photos/?q=bunny&image_type=&cat=&min_width=&min_height=')
