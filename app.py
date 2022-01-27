class Mother:
    def __init__(self, eye_color):
        self.eye_color = eye_color


class Father:
    def __init__(self, hair_color):
        self.hair_color = hair_color


class Child(Mother, Father):
    def __init__(self, eye_color, hair_color):
        super(Mother, self).__init__(eye_color)
        super(Father, self).__init__(hair_color)
