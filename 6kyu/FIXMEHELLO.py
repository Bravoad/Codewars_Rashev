class Dinglemouse:
    def __init__(self):
        self._values = {'name': None, 'age': None, 'sex': None}
        self._order = []
        self._formatters = {
            'name': lambda v: f"My name is {v}.",
            'age': lambda v: f"I am {v}.",
            'sex': lambda v: f"I am {'male' if v == 'M' else 'female'}.",
        }

    def _track(self, key: str):
        """Записываем ключ, если присваиваем впервые."""
        if key not in self._order:
            self._order.append(key)

    def setName(self, name: str):
        self._track('name')
        self._values['name'] = name
        return self

    def setAge(self, age: int):
        self._track('age')
        self._values['age'] = age
        return self

    def setSex(self, sex: str):
        self._track('sex')
        self._values['sex'] = sex
        return self

    def hello(self) -> str:
        if not self._order:
            return "Hello."

        parts = []
        for key in self._order:
            val = self._values[key]
            if val is None:
                continue
            parts.append(self._formatters[key](val))

        return "Hello. " + " ".join(parts)
