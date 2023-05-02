from checkers.point import Point
from checkers.enums import CheckerType, SideType

# Сторона за яку грає гравець
PLAYER_SIDE = SideType.WHITE

# Розмір поля
X_SIZE = Y_SIZE = 8
# Розмір комірки (у пікселях)
CELL_SIZE = 75

# Швидкість анімації (більше = швидше)
ANIMATION_SPEED = 4

# Кількість ходів для передбачення
MAX_PREDICTION_DEPTH = 3

# Ширина рамки (Бажано повинна бути парною)
BORDER_WIDTH = 2 * 2

# Кольори ігрової дошки
FIELD_COLORS = ['#E7CFA9', '#927456']
# Колір рамки при наведенні на клітинку мишкою
HOVER_BORDER_COLOR = '#54b346'
# Колір рамки при виділенні комірки
SELECT_BORDER_COLOR = '#944444'
# Колір кружків можливих ходів
POSIBLE_MOVE_CIRCLE_COLOR = '#944444'

# Можливі зміщення ходів шашок
MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]

# Масиви типів білих і чорних шашок [Звичайна пішак, дамка]
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN]