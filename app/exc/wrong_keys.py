class WrongKeyReceived(Exception):

    correct_keys = ["name", "email", "phone"]

    def __init__(self, data: dict) -> None:
        self.message = {
            "available_keys": self.correct_keys,
            "wrong_keys": self.wrong_key(data)
        }
        self.miss_keys = {
            "available_keys": self.correct_keys,
            "missing_keys": self.missing_key(data)
        }
        self.only_email_message = {
            "available_key" : "email",
            "your_requisition_keys": self.only_email(data)
        }

    @classmethod
    def wrong_key(cls, data: dict) -> list:
        return [key for key in data.keys() if key not in cls.correct_keys]
    
    @classmethod
    def missing_key(cls, data: dict) -> list:
        return [key for key in cls.correct_keys if key not in data.keys()]
    
    def only_email(cls, data: dict) -> list:
        return [key for key in data.keys()]