import random
import typing

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]

    while True:
        rand_tuple = (random.choice(players), random.choice(actions))
        yield rand_tuple


def main() -> None:
    print("=== Game Data Stream Processor ===")
    
    event = gen_event()
    ten_event_list = [] 
    for i in range(0,1000):
        p_name, p_action = next(event)
        print(f"Event {i}: Player {p_name.lower()} did action {p_action}")
    for i in range(0,10):
        p_name, p_action = next(event)
        ten_event_list.append((p_name.lower(), p_action))
    print(f"Built list of 10 events: {ten_event_list}")
    consumer = consume_event(ten_event_list)
    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_event_list}")

    
def consume_event(event_list: list) -> typing.Generator:
    while event_list:
        index = random.randrange(len(event_list))
        removed_event = event_list.pop(index) 
        yield removed_event

if __name__ == "__main__":
    main()

        