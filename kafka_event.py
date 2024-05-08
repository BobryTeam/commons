from queue import Queue

from kafka import KafkaConsumer, KafkaProducer

from event import *


class KafkaEventReader:
    '''
    Класс, который считывает сообщения с кафки и сохраняет их в виде ивентов
    '''

    def __init__(self, kafka_consumer: KafkaConsumer, event_queue: Queue):
        '''
        Подписка к кафке с помощью конфига
        '''
        self.consumer = kafka_consumer
        self.running = True
        self.events = event_queue

    async def read_events(self):
        '''
        Считывание сообщений от кафки, превращение их в ивенты, сохранение в очередь ивентов
        Запущен на отдельном потоке для постоянного считывания новых сообщений
        '''
        while self.running:
            message = self.consumer.consume()
            if message is not None:
                self.events.put(EventFromMessage(message))

    def release(self):
        '''
        Отключение от кафки
        '''
        self.running = False
        self.consumer.close()
        pass

class KafkaEventWriter:
    '''
    Класс, который превращает ивенты в сообщения и отправляет их в кафку
    '''

    def __init__(self, kafka_producer: KafkaProducer):
        '''
        Инициализация класса - подключение к кафке с помощью конфига
        '''
        self.producer = kafka_producer

    def send_event(self, event: Event):
        '''
        Отправка ивента превращенного в сообщение
        '''
        message = str(event)
        self.producer.send(message)
        
    def release(self):
        '''
        Отключение от кафки
        '''
        pass
