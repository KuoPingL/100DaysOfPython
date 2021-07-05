import enum


class PixeUnitType(enum.Enum):
    INT = "int"
    FLOAT = "float"


class PixeColor(enum.Enum):
    GREEN = "shibafu"
    RED = "momiji"
    BLUE = "sora"
    YELLOW = "ichou"
    PURPLE = "ajisai"
    BLACK = "kuro"

# class Pixe:
#     def __init__(self):
#         self.token = None
#         self.username = None
#         self.agree_terms_of_service = None
#         self.not_minor = None
#         self.thanks_code = None
#
#
# def create_user_api(cls) -> Pixe:
