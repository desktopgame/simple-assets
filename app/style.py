class Style:
    def __init__(self, color, filename: str):
        self.__color = color
        self.__filename = filename

    @property
    def color(self):
        return self.__color

    @property
    def filename(self) -> str:
        return self.__filename
