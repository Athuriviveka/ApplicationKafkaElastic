import json
import time

from faker import Faker
from confluent_kafka import Producer
from faker.generator import random

from kafka_logger import logger

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():
    p = Producer({'bootstrap.servers': 'localhost:29092'})
    print('Kafka Producer has been initiated...')
    fake = Faker()
    for i in range(10):
        data={
           'user_id': fake.random_int(min=20000, max=100000),
           'user_name':fake.name(),
           'user_address':fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
           'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
           'signup_at': str(fake.date_time_this_month())
           }
        m=json.dumps(data)
        p.poll(1)
        p.produce('user-tracker', m.encode('utf-8'), callback= receipt)
        p.flush()
        time.sleep(3)

if __name__ == "__main__":
    main()