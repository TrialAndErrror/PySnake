import random

PIXEL_SIZE = 50
DEFAULT_START_LOCATION = (10, 4)

class Pixel:
    x: int
    y: int
    
    fillStyle: str
    strokeStyle: str

    def get_location(self):
        return self.x * PIXEL_SIZE, self.y * PIXEL_SIZE

class SnakeSegment(Pixel):  
    fillStyle = 'lightblue'
    strokeStyle = 'darkblue'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Snake:
    segments: list

    def __init__(self, x, y):
        self.segments = [
            SnakeSegment(x, y),
            SnakeSegment(x-1, y),
            SnakeSegment(x-2, y),
            SnakeSegment(x-3, y),
            SnakeSegment(x-4, y),
        ]

    def move(self, head_change):
        head: SnakeSegment = SnakeSegment(self.segments[0].x + head_change['x'], self.segments[0].y + head_change['y'])
        self.segments.insert(0, head)


    def check_if_hit_head(self) -> bool:
        head = self.segments[0]
        for element in self.segments[1:]:
            if element.x == head.x and element.y == head.y:
                return True

        return False

    def check_if_hit_wall(self, width: int, height: int) -> bool:
        head = self.segments[0]
        hit_left_wall = head.x < 0
        hit_right_wall = head.x > width / PIXEL_SIZE
        hit_top_wall = head.y < 0
        hit_bot_wall = head.y > height / PIXEL_SIZE
        return any([hit_left_wall, hit_right_wall, hit_top_wall, hit_bot_wall])

    def __str__(self):
        return str([segment.get_location() for segment in self.segments])

class Food(Pixel):
    fillStyle = 'lightgreen'
    strokeStyle = 'darkgreen'

    @classmethod
    def make_random(cls, max_width: int, max_height: int):
        def random_food(min, max):
            value = round((random.random() * (max-min) + min) / PIXEL_SIZE)
            print(f'Food value: {value}')
            return value

        obj = cls()
        obj.x = random_food(0, max_width - PIXEL_SIZE)
        obj.y  = random_food(0, max_height - PIXEL_SIZE)

        return obj



class GameBoard:
    snake: Snake
    food: Food or None
    is_running = False

    current_direction: dict
    next_direction: dict

    def __init__(self, snakeboard, snakeboard_ctx):
        self.board = snakeboard
        self.ctx = snakeboard_ctx

    def start_game(self):
        self.is_running = True
        self.snake = Snake(*DEFAULT_START_LOCATION)

        self.current_direction = {'x': 1, 'y': 0}
        self.next_direction = {'x': 1, 'y': 0}

        self._gen_food()

    def _draw_pixel(self, pixel: Pixel):
        self.ctx.fillStyle = pixel.fillStyle
        self.ctx.strokestyle = pixel.strokeStyle
        self.ctx.fillRect(*pixel.get_location(), PIXEL_SIZE, PIXEL_SIZE)
        self.ctx.strokeRect(*pixel.get_location(), PIXEL_SIZE, PIXEL_SIZE)

    def draw_food(self):
        self._draw_pixel(self.food)

    def draw_snake(self):
        self.ctx.clearRect(0, 0, self.board.width, self.board.height)
        for segment in self.snake.segments:
            self._draw_pixel(segment)

    def move_snake(self):
        self.snake.move(self.next_direction)

        has_eaten_food: bool = self.snake.segments[0].x == self.food.x and self.snake.segments[0].y == self.food.y
        if has_eaten_food:
            self._clear_square(*self.food.get_location())

            # Generate new food location
            self._gen_food()
            self.draw_food()

        else:
            # Remove the last part of snake body
            prev = self.snake.segments.pop()
            self._clear_square(*prev.get_location())

        self.current_direction = self.next_direction

    def has_ended(self):
        return any([self.snake.check_if_hit_head(), self.snake.check_if_hit_wall(self.board.width, self.board.height)])

    def get_score(self):
        return len(self.snake.segments) - 5


    def _gen_food(self):
        self.food = Food.make_random(self.board.width, self.board.height)
    
    def _clear_square(self, x, y):
        self.ctx.clearRect(x, y, x + PIXEL_SIZE, y + PIXEL_SIZE)

