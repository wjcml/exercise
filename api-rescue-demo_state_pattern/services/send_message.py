from db_model import RescueEvent
from flask import request

from lib.common import hlog, db_session
from lib.state_machine import RescueEventMachine


def send_message():
    event_id = request.args.get('eventId')
    hlog.var('event_id', event_id)

    rescue_event_obj = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
    event_state = str(rescue_event_obj.state)
    db_session.close()

    rescue_event = RescueEventMachine(event_state)
    rescue_event.send_message(event_id=event_id)

    result = {
        "code": 0,
        "EventId": event_id
    }

    hlog.var('result', result)
    return result
