import random
import string
import uuid


class EventDataGenerator:
    @staticmethod
    def generate_event_data():
        event_record = {
            "event": {
                "property": {
                    "call_id": str(uuid.uuid4()),
                    "call_duration": str(random.randint(10, 300)),
                    "call_status": random.choice(["completed", "ongoing"]),
                },
                "super_property": {
                    "source": "mandir",
                    "type": "purchase",
                    "producer": "user",
                    "name": "astrology_session_purchase",
                    "timestamp": str(random.randint(1000000000000, 9999999999999)),
                },
            },
            "user": {
                "user_id": str(random.randint(100, 999)),
                "state": {
                    "coins": str(random.randint(50, 200)),
                    "is_logged_in": random.choice(["true", "false"]),
                    "language": random.choice(["en", "es", "fr"]),
                    "language_mode": random.choice(["en", "es", "fr"]),
                    "country_code": random.choice(["US", "UK", "CA"]),
                    "tz": random.choice(["America/New_York", "Europe/London", "Asia/Tokyo"]),
                },
                "device_segment": str(random.randint(1, 100)),
            },
            "platform": {
                "version": {
                    "integer": str(random.randint(100, 999)),
                    "string": ".".join([str(random.randint(0, 9)) for _ in range(3)]),
                },
                "code": "com.mandir",
                "type": "iOS",
            },
            "geo_location": None,
            "device": {
                "a_id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=36)),
                "state": {
                    "is_background": random.choice(["true", "false"]),
                    "is_online": random.choice(["true", "false"]),
                    "is_playing_music": random.choice(["true", "false"]),
                },
                "hardware": {
                    "model_name": "iPhone 12",
                    "brand_name": "Apple",
                    "type": "Mobile",
                },
                "software": {
                    "mobile": {
                        "version": "14",
                        "name": "iOS",
                    },
                    "web": None,
                },
                "ip": {
                    "ipv4": f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}",
                    "ipv6": f"2401:db00:2110:3004:0:0:0:{random.randint(0, 65535)}",
                },
                "system_language": "Spanish",
                "system_id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
            },
            "session": {
                "number": str(random.randint(1, 10)),
                "id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=32)),
            },
            "referral": {
                "user_id": str(random.randint(100, 999)),
                "user_code": ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)),
            },
        }
        return event_record
