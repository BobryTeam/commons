from enum import Enum

from trend_data import *
from scale_data import *
from metrics import *

class EventType(Enum):
    # Event of invalid message
    Invalid = 'erro'
    # General usage event with a string message
    # mesg <message>
    Message = 'mesg'

    # Trend Analyser -> Observer Manager, Observer Manager -> Decision Module, Decision Module Manager -> Decision Module AI
    # trda <str(TrendData)>
    TrendData = 'trda'
    # Observer Manager -> Metrics Collector
    # getm
    GetMetrics = 'getm'
    # Observer Manager -> Trend Analyser
    # antr
    AnalyseTrend = 'antr'
    # Observer Manager -> Metrics Collector
    # updm <metrics_file_path>
    UpdateMetrics = 'updm'
    # Decision Module AI -> Decision Module Manager
    # trar <str(ScaleData)>
    TrendAnalyseResult = 'trar'


_event_type_members = EventType._member_map_.values()
class EventTypeConstants:
    event_type_to_prefix = {}
    prefix_to_event_type = {}

    for enum in _event_type_members:
        event_type_to_prefix[enum] = enum.value
        prefix_to_event_type[enum.value] = enum


class Event:
    def __init__(self, type: EventType, data):
        self.type = type
        self.data = data

    def __str__(self) -> str:
        return f'{EventTypeConstants.event_type_to_prefix[self.type]} {self.data}'


class EventFromMessage(Event):
    def __init__(self, kafka_message: str):
        prefix = kafka_message[:4]
        data = kafka_message[5:]

        try:
            event_type = EventTypeConstants.prefix_to_event_type[prefix]
        except:
            event_type = EventType.Invalid

        match event_type:
            case EventType.Message:
                data = data
            case EventType.TrendData:
                data = TrendDataFromStr(data)
            case EventType.GetMetrics: pass
            case EventType.UpdateMetrics:
                data = data
            case EventType.TrendAnalyseResult:
                data = ScaleDataFromStr(data)
            case EventType.AnalyseTrend: pass
            case _:
                data = f'Error: got invalid message: {kafka_message}'

        return super().__init__(event_type, data)

