import json


class BaseClass:
    def to_dict(self) -> dict:
        """
        Convert nested object to dict
        :return: dict
        """
        x = json.dumps(self, default=lambda o: o.__dict__)
        y = json.loads(x)
        return y