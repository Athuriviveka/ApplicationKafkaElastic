from confluent_kafka import Consumer
from IngestDataElastic import ingest

c = Consumer({'bootstrap.servers':'localhost:29092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['user-tracker'])

def main():
    i = 0
    while True:
        msg = c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')
        print(data)
        ingest(data, i)
        i = i+1
    c.close()

if __name__ == "__main__":
    main()