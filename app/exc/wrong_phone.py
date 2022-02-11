class WrongPhone(Exception):

    correct_format = "(xx)xxxxx-xxxx"
    def __init__(self, data: dict) -> None:
        self.message = {
            "correct_format": self.correct_format,
            "your_requisition": self.your_requisition(data)
        }

    @classmethod
    def your_requisition(cls, data: dict) -> str:
        return data["phone"]