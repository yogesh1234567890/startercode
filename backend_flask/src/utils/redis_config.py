import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def lock_tickets(event_id, quantity, user_id, lock_duration=300):
    key = f"event:{event_id}:tickets"
    tickets = redis_client.get(key)

    if tickets is None:
        return False

    tickets = json.loads(tickets)
    available_tickets = tickets.get("available", 0)

    if available_tickets < quantity:
        return False

    # Lock the tickets
    tickets["available"] -= quantity
    tickets["locked_by"][user_id] = quantity
    redis_client.set(key, json.dumps(tickets), ex=lock_duration)
    return True

def unlock_tickets(event_id, user_id):
    key = f"event:{event_id}:tickets"
    tickets = redis_client.get(key)

    if tickets is None:
        return

    tickets = json.loads(tickets)
    if user_id in tickets["locked_by"]:
        tickets["available"] += tickets["locked_by"].pop(user_id)
        redis_client.set(key, json.dumps(tickets))
