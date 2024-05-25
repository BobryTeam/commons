# Ивенты
Ивент - это класс, хранящий в себе тип ивента и передаваемую информацию ивента

Ивенты передаются через сообщения кафки, для удобства определения типа передаваемого ивента, первые четыре символа сообщения отводятся на тип ивента, тогда сообщения ивентов имееют вид `<event_type_prefix> <event_data>`

Тип ивента представляется enum'ом, каждому типу соответсвует его представление в виде префикса сообщения:

```py
class EventType(Enum):
    Invalid = 'erro'
    TrendData = 'trda'
    GetMetrics = 'getm'
    ...
```

Для каждого класса, который передается ивентом должны быть реализованы способы сериализации и десериализации.

Способ сериализации мы задаем при помощи имплементации функции `__str__` для класса передаваемых данных.

Способ десериализации мы задаем при помощи имплементации конструктора класса `<DataClass>FromStr`. Этот класс наследуется от `<DataClass>`.

# Кафка

Для работой с сообщениями кафки написано два класса: `KafkaEventWriter` и `KafkaEventReader`.

## Запись

Запись происходит разово при каждом вызове метода `send()`.

## Считывание

Считывание происходит в очередь событий (`event_queue`, переданный в конструкторе) в отдельном потоке.

То есть `read_events()` запущен постоянно, он сохраняет ивенты в очередь. Чтобы получить первый ивент в очереди, вызываем `event_queue.get()`.
