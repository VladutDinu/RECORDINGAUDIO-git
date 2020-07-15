from ProducerThread import ProducerThread
from ConsumerThread import ConsumerThread
p = ProducerThread()
c = ConsumerThread()
p.start()
c.start()

