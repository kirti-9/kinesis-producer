import random
import string


class EventDataGenerator:
    @staticmethod
    def generate_event_data():
        dummy_name = ''.join(random.choices(string.ascii_letters, k=10))  # Generate a random name
        random_user_id = random.randint(1, 1000)  # Generate a random user ID
        return {"name": dummy_name, "userID": random_user_id}
