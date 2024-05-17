from kafka import KafkaProducer

def producer_fun():

    servers = [
        "bootstrapserver-1",
        "bootstrapserver-1",
        "bootstrapserver-1",
    ]

    topics = ["topic-name"]
    ssl_cafile = f'cert/ca.crt'
    ssl_certfile = f'cert/cert.pem'
    ssl_keyfile = f'cert/key.pem'

    producer = KafkaProducer(
        api_version=(0, 11, 5),
        bootstrap_servers=servers,
        security_protocol='SSL',
        ssl_check_hostname=True,
        ssl_cafile=ssl_cafile,
        ssl_certfile=ssl_certfile,
        ssl_keyfile=ssl_keyfile,
        ssl_password='prmcert'
    )

    data = [
    # data to be pushed
            ]
    
    for topic in topics:
        for datum in data:
            x = producer.send(topic=topic, value=bytes(datum, encoding='utf-8'))
            producer.flush()
            print(x)


if __name__ == "__main__":
    producer_fun()
