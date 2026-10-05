import pygame
import random
import math
import sys

pygame.init()

# =========================================================
# SETUP
# =========================================================

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYTHON STRIKE - Learn Python By Shooting")

clock = pygame.time.Clock()

# =========================================================
# COLORS
# =========================================================

BLACK = (7, 10, 18)
WHITE = (245, 248, 255)
CYAN = (0, 220, 255)
GREEN = (40, 240, 130)
RED = (255, 70, 80)
YELLOW = (255, 220, 50)
PURPLE = (190, 80, 255)
BLUE = (50, 100, 220)
DARK = (20, 28, 45)
GRAY = (130, 140, 155)
ORANGE = (255, 150, 40)

# =========================================================
# FONTS
# =========================================================

FONT_SMALL = pygame.font.SysFont("consolas", 18, bold=True)
FONT = pygame.font.SysFont("consolas", 24, bold=True)
FONT_BIG = pygame.font.SysFont("consolas", 38, bold=True)
FONT_HUGE = pygame.font.SysFont("consolas", 58, bold=True)

# =========================================================
# QUESTIONS
# =========================================================

NORMAL_QUESTIONS = [

    ("What is the output?\nprint(2 + 3)",
     ["5", "23", "6", "Error"], 0,
     "2 + 3 = 5"),

    ("Which keyword creates a function?",
     ["func", "def", "function", "create"], 1,
     "Python uses def."),

    ("Which symbol starts a comment?",
     ["//", "#", "/*", "--"], 1,
     "# starts a Python comment."),

    ("What is the type of 10?",
     ["str", "float", "int", "bool"], 2,
     "10 is an integer."),

    ("Which is a list?",
     ["(1,2)", "[1,2]", "{1,2}", "<1,2>"], 1,
     "Square brackets create a list."),

    ("What does len('Python') return?",
     ["5", "6", "7", "Error"], 1,
     "Python has 6 letters."),

    ("Which keyword is used for condition?",
     ["if", "when", "check", "case"], 0,
     "if is used for conditions."),

    ("Output?\nprint(10 > 5)",
     ["True", "False", "10", "Error"], 0,
     "10 is greater than 5."),

    ("Which loop is commonly used for sequences?",
     ["repeat", "for", "loop", "each"], 1,
     "for loops iterate over sequences."),

    ("What does input() return?",
     ["int", "float", "string", "bool"], 2,
     "input() returns a string by default."),

    ("Which collection uses key-value pairs?",
     ["list", "tuple", "dictionary", "string"], 2,
     "Dictionaries use key-value pairs."),

    ("What is 10 % 3?",
     ["1", "3", "0", "10"], 0,
     "The remainder is 1."),

    ("Which keyword exits a loop?",
     ["stop", "exit", "break", "end"], 2,
     "break exits a loop."),

    ("Which keyword skips current iteration?",
     ["skip", "continue", "pass", "next"], 1,
     "continue moves to the next iteration."),

    ("What is a tuple?",
     ["Mutable sequence", "Immutable sequence",
      "Loop", "Function"], 1,
     "Tuples are immutable."),

    ("Output?\nx = [1,2,3]\nprint(x[0])",
     ["1", "2", "3", "0"], 0,
     "Index 0 contains 1."),

    ("Which method adds item to list?",
     ["add()", "push()", "append()", "insertEnd()"], 2,
     "append() adds an item."),

    ("Which operator means power?",
     ["^", "**", "//", "%%"], 1,
     "** means exponentiation."),

    ("What is 7 // 2?",
     ["3", "3.5", "4", "2"], 0,
     "Floor division gives 3."),

    ("Which value means no value?",
     ["null", "none", "None", "empty"], 2,
     "Python uses None."),

    ("Output?\nprint(bool(0))",
     ["True", "False", "0", "None"], 1,
     "0 is False."),

    ("Which is immutable?",
     ["list", "dict", "set", "tuple"], 3,
     "Tuple is immutable."),

    ("What does range(5) produce?",
     ["0 to 4", "1 to 5", "0 to 5", "5 only"], 0,
     "range(5) gives 0,1,2,3,4."),

    ("Which handles exceptions?",
     ["catch", "except", "error", "handle"], 1,
     "except handles exceptions."),

    ("What does str(10) do?",
     ["10 to string", "string to int",
      "10 to float", "error"], 0,
     "str converts a value to string."),

    ("What does int('5') return?",
     ["'5'", "5", "5.0", "Error"], 1,
     "int converts to integer."),

    ("Which operator checks equality?",
     ["=", "==", "!=", "==="], 1,
     "== checks equality."),

    ("Which keyword imports modules?",
     ["include", "using", "import", "module"], 2,
     "Python uses import."),

    ("What is a set?",
     ["Ordered duplicate collection",
      "Unique collection", "Function", "String"], 1,
     "Sets contain unique values."),

    ("Output?\nprint(3 * 2)",
     ["5", "6", "32", "9"], 1,
     "3 multiplied by 2 is 6.")
]


ADVANCED_QUESTIONS = [

    ("What is the output?\nprint([x*x for x in range(4)])",
     ["[1,4,9,16]", "[0,1,4,9]",
      "[0,1,2,3]", "Error"], 1,
     "range(4) starts from 0."),

    ("What does LEGB stand for?",
     ["Local Enclosed Global Built-in",
      "List Element Global Base",
      "Local External Global Basic",
      "Loop Expression Global Built-in"], 0,
     "LEGB describes Python name lookup."),

    ("Output?\nx = 10\ndef f():\n x = 20\n print(x)\nf()",
     ["10", "20", "30", "Error"], 1,
     "The local variable x is 20."),

    ("Which creates an anonymous function?",
     ["def", "lambda", "anon", "func"], 1,
     "lambda creates anonymous functions."),

    ("What does map() return in Python 3?",
     ["list", "iterator", "tuple", "set"], 1,
     "map returns an iterator."),

    ("What does filter() do?",
     ["Sorts values", "Filters iterable",
      "Deletes list", "Maps values"], 1,
     "filter selects values."),

    ("What does *args collect?",
     ["Keyword arguments", "Positional arguments",
      "Variables", "Classes"], 1,
     "*args collects positional arguments."),

    ("What does **kwargs collect?",
     ["Positional arguments", "Keyword arguments",
      "Lists", "Tuples"], 1,
     "**kwargs collects keyword arguments."),

    ("What is a closure?",
     ["Nested class",
      "Function remembering enclosing scope",
      "Loop", "Module"], 1,
     "A closure remembers its enclosing scope."),

    ("What is recursion?",
     ["Function calling itself",
      "Looping list", "Creating class", "Importing module"], 0,
     "Recursion means a function calls itself."),

    ("Which keyword creates generator behavior?",
     ["yield", "return", "generate", "next"], 0,
     "yield is used with generators."),

    ("What does next(iterator) do?",
     ["Restarts iterator", "Gets next item",
      "Deletes item", "Sorts iterator"], 1,
     "next() gets the next value."),

    ("What is a decorator used for?",
     ["Modify function behavior",
      "Delete function", "Create variable", "Loop"], 0,
     "Decorators wrap functions."),

    ("Which method initializes an object?",
     ["init()", "__init__()", "start()", "new()"], 1,
     "__init__ initializes an object."),

    ("What does inheritance allow?",
     ["Class reuse/extension", "Only variables",
      "Only loops", "File deletion"], 0,
     "Inheritance allows reuse and extension."),

    ("What is polymorphism?",
     ["Same interface, different implementations",
      "Only one class", "Data hiding", "Recursion"], 0,
     "Different objects can implement the same interface."),

    ("What is a dataclass useful for?",
     ["Data-focused classes", "Loops",
      "Networking", "Rendering"], 0,
     "dataclasses reduce boilerplate."),

    ("What is __name__ == '__main__' used for?",
     ["Run code only when file is executed directly",
      "Create class", "Import package", "Delete module"], 0,
     "It detects direct execution."),

    ("Which handles cleanup even if exception occurs?",
     ["catch", "finally", "cleanup", "end"], 1,
     "finally runs during cleanup."),

    ("What is an iterator required to implement?",
     ["__iter__ and __next__",
      "__start__ and __stop__",
      "__loop__", "__run__"], 0,
     "Python iterator protocol uses __iter__ and __next__.")
]


BOSS_QUESTIONS = [

    ("What is the output?\nprint([i for i in range(5) if i % 2 == 0])",
     ["[0,2,4]", "[1,3,5]", "[2,4]", "Error"], 0),

    ("What is printed?\nx=5\ndef f():\n global x\n x=10\nf()\nprint(x)",
     ["5", "10", "Error", "None"], 1),

    ("What does a generator provide?",
     ["All values immediately",
      "Values lazily", "Only strings", "Only lists"], 1),

    ("Which principle hides implementation details?",
     ["Inheritance", "Encapsulation",
      "Iteration", "Recursion"], 1),

    ("Output?\na=[1,2]\nb=a\nb.append(3)\nprint(a)",
     ["[1,2]", "[1,2,3]", "[3]", "Error"], 1)
]

# =========================================================
# GAME VARIABLES
# =========================================================

state = "MENU"
mode = "NORMAL"

normal_level = 1
advanced_level = 1
boss_level = 1

score = 0
xp = 0

hp = 100
max_hp = 100

bullets = 8
max_bullets = 8

time_limit = 15
level_start_time = 0

current_question = ""
current_options = []
current_answer = 0
current_explanation = ""

targets = []
projectiles = []
particles = []

message = ""
message_timer = 0

show_hint = False
show_controls = False
show_exit = False

exit_selection = 0

boss_hp = 100
boss_max_hp = 100

stage_start_level = 1

recoil = 0
muzzle_flash = 0

# =========================================================
# TEXT
# =========================================================

def draw_text(value, font, color, x, y, center=False):

    surf = font.render(str(value), True, color)

    if center:
        rect = surf.get_rect(center=(x, y))
    else:
        rect = surf.get_rect(topleft=(x, y))

    screen.blit(surf, rect)


# =========================================================
# BUTTON
# =========================================================

def draw_button(rect, label, color):

    pygame.draw.rect(
        screen,
        (18, 28, 48),
        rect,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        color,
        rect,
        3,
        border_radius=12
    )

    draw_text(
        label,
        FONT,
        WHITE,
        rect.centerx,
        rect.centery,
        True
    )


# =========================================================
# LOAD QUESTION
# =========================================================

def load_level():

    global current_question
    global current_options
    global current_answer
    global current_explanation
    global targets
    global bullets
    global level_start_time
    global show_hint
    global projectiles
    global particles

    projectiles.clear()
    particles.clear()

    bullets = max_bullets
    show_hint = False

    if mode == "NORMAL":

        q_index = (normal_level - 1) % len(NORMAL_QUESTIONS)

        question, answers, correct, explanation = NORMAL_QUESTIONS[q_index]

    else:

        q_index = (advanced_level - 1) % len(ADVANCED_QUESTIONS)

        question, answers, correct, explanation = ADVANCED_QUESTIONS[q_index]

    # -----------------------------------------------------
    # IMPORTANT:
    # RANDOMIZE ANSWERS
    # -----------------------------------------------------

    answer_data = []

    for i, answer in enumerate(answers):
        answer_data.append((answer, i))

    random.shuffle(answer_data)

    current_question = question
    current_options = [item[0] for item in answer_data]

    correct_original_index = correct

    for new_index, item in enumerate(answer_data):

        if item[1] == correct_original_index:
            current_answer = new_index
            break

    current_explanation = explanation

    # -----------------------------------------------------
    # TARGET POSITIONS
    # -----------------------------------------------------

    positions = [
        (250, 390),
        (500, 390),
        (780, 390),
        (1030, 390)
    ]

    targets = []

    for i in range(4):

        x, y = positions[i]

        targets.append({
            "rect": pygame.Rect(
                x - 105,
                y - 55,
                210,
                110
            ),
            "index": i,
            "alive": True,
            "result": None,
            "result_timer": 0
        })

    level_start_time = pygame.time.get_ticks()


# =========================================================
# START
# =========================================================

def start_game(selected_mode):

    global mode
    global state
    global normal_level
    global advanced_level
    global score
    global xp
    global hp
    global stage_start_level

    mode = selected_mode

    normal_level = 1
    advanced_level = 1

    score = 0
    xp = 0
    hp = max_hp

    stage_start_level = 1

    load_level()

    state = "PLAYING"


# =========================================================
# MENU
# =========================================================

def draw_menu():

    screen.fill(BLACK)

    # Grid
    for x in range(0, WIDTH, 40):
        pygame.draw.line(
            screen,
            (13, 23, 38),
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, 40):
        pygame.draw.line(
            screen,
            (13, 23, 38),
            (0, y),
            (WIDTH, y)
        )

    draw_text(
        "PYTHON STRIKE",
        FONT_HUGE,
        CYAN,
        WIDTH // 2,
        90,
        True
    )

    draw_text(
        "LEARN PYTHON BY SHOOTING",
        FONT,
        WHITE,
        WIDTH // 2,
        145,
        True
    )

    normal = pygame.Rect(
        WIDTH // 2 - 180,
        240,
        360,
        70
    )

    advanced = pygame.Rect(
        WIDTH // 2 - 180,
        330,
        360,
        70
    )

    controls = pygame.Rect(
        WIDTH // 2 - 180,
        425,
        170,
        55
    )

    exit_btn = pygame.Rect(
        WIDTH // 2 + 10,
        425,
        170,
        55
    )

    draw_button(normal, "NORMAL MODE", GREEN)
    draw_button(advanced, "TEACHER ADVANCED", PURPLE)
    draw_button(controls, "CONTROLS", CYAN)
    draw_button(exit_btn, "EXIT GAME", RED)

    draw_text(
        "30 Normal Levels | 20 Advanced Levels | Boss",
        FONT_SMALL,
        GRAY,
        WIDTH // 2,
        525,
        True
    )

    draw_text(
        "Mouse = Aim & Shoot     1-4 = Answer     Ctrl+E = Exit",
        FONT_SMALL,
        GRAY,
        WIDTH // 2,
        555,
        True
    )


# =========================================================
# GUN
# =========================================================

def gun_position():

    return WIDTH - 145, HEIGHT - 110


def gun_angle():

    gx, gy = gun_position()

    mx, my = pygame.mouse.get_pos()

    return math.atan2(
        my - gy,
        mx - gx
    )


def draw_gun():

    gx, gy = gun_position()

    angle = gun_angle()

    gx -= math.cos(angle) * recoil
    gy -= math.sin(angle) * recoil

    # Body
    pygame.draw.circle(
        screen,
        (25, 35, 55),
        (int(gx), int(gy)),
        42
    )

    pygame.draw.circle(
        screen,
        CYAN,
        (int(gx), int(gy)),
        42,
        3
    )

    # Barrel
    barrel = 150

    ex = gx + math.cos(angle) * barrel
    ey = gy + math.sin(angle) * barrel

    pygame.draw.line(
        screen,
        (35, 50, 70),
        (gx, gy),
        (ex, ey),
        24
    )

    pygame.draw.line(
        screen,
        CYAN,
        (gx, gy),
        (ex, ey),
        5
    )

    pygame.draw.line(
        screen,
        WHITE,
        (gx, gy),
        (ex, ey),
        2
    )

    # Handle
    hx = gx - math.sin(angle) * 35
    hy = gy + math.cos(angle) * 35

    pygame.draw.line(
        screen,
        (30, 35, 45),
        (gx, gy),
        (hx, hy),
        22
    )

    # Muzzle
    pygame.draw.circle(
        screen,
        CYAN,
        (int(ex), int(ey)),
        8
    )

    if muzzle_flash > 0:

        pygame.draw.circle(
            screen,
            WHITE,
            (int(ex), int(ey)),
            20
        )

        pygame.draw.circle(
            screen,
            CYAN,
            (int(ex), int(ey)),
            34,
            4
        )


# =========================================================
# FIRE
# =========================================================

def fire():

    global bullets
    global recoil
    global muzzle_flash
    global state

    if bullets <= 0:

        state = "AMMO_OVER"
        return

    gx, gy = gun_position()

    angle = gun_angle()

    mx = gx + math.cos(angle) * 150
    my = gy + math.sin(angle) * 150

    speed = 28

    projectiles.append({
        "x": mx,
        "y": my,
        "vx": math.cos(angle) * speed,
        "vy": math.sin(angle) * speed,
        "life": 80,
        "trail": []
    })

    bullets -= 1

    recoil = 14
    muzzle_flash = 5


# =========================================================
# PROJECTILES
# =========================================================

def update_projectiles():

    global state
    global score
    global xp
    global hp
    global message
    global message_timer

    for bullet in projectiles[:]:

        bullet["trail"].append(
            (bullet["x"], bullet["y"])
        )

        if len(bullet["trail"]) > 8:
            bullet["trail"].pop(0)

        bullet["x"] += bullet["vx"]
        bullet["y"] += bullet["vy"]

        bullet["life"] -= 1

        # Trail
        for p in bullet["trail"]:

            pygame.draw.circle(
                screen,
                CYAN,
                (int(p[0]), int(p[1])),
                4
            )

        # Bullet
        pygame.draw.circle(
            screen,
            WHITE,
            (int(bullet["x"]), int(bullet["y"])),
            7
        )

        pygame.draw.circle(
            screen,
            CYAN,
            (int(bullet["x"]), int(bullet["y"])),
            12,
            2
        )

        bullet_rect = pygame.Rect(
            int(bullet["x"] - 8),
            int(bullet["y"] - 8),
            16,
            16
        )

        hit = False

        for target in targets:

            if not target["alive"]:
                continue

            if bullet_rect.colliderect(target["rect"]):

                target["alive"] = False
                target["result_timer"] = 30

                if target["index"] == current_answer:

                    target["result"] = "CORRECT"

                    score += 100
                    xp += 25

                    message = "✓ CORRECT HIT!"
                    message_timer = 70

                    create_explosion(
                        target["rect"].centerx,
                        target["rect"].centery,
                        GREEN
                    )

                    # next level
                    if mode == "NORMAL":

                        if normal_level >= 30:
                            state = "BOSS"

                        elif normal_level % 5 == 0:
                            state = "STAGE_CLEAR"

                        else:
                            next_level()

                    else:

                        if advanced_level >= 20:
                            state = "BOSS"

                        elif advanced_level % 5 == 0:
                            state = "STAGE_CLEAR"

                        else:
                            next_level()

                else:

                    target["result"] = "WRONG"

                    hp -= 25

                    message = "✗ WRONG TARGET!"
                    message_timer = 70

                    create_explosion(
                        target["rect"].centerx,
                        target["rect"].centery,
                        RED
                    )

                    if hp <= 0:

                        hp = 0

                        global player_out_reason
                        player_out_reason = "WRONG ANSWER"

                        state = "PLAYER_OUT"

                hit = True
                break

        if hit or bullet["life"] <= 0:

            if bullet in projectiles:
                projectiles.remove(bullet)


# =========================================================
# EXPLOSION
# =========================================================

def create_explosion(x, y, color):

    for _ in range(35):

        angle = random.uniform(
            0,
            math.pi * 2
        )

        speed = random.uniform(
            2,
            8
        )

        particles.append({
            "x": x,
            "y": y,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(15, 45),
            "size": random.randint(2, 7),
            "color": color
        })


def update_particles():

    for p in particles[:]:

        p["x"] += p["vx"]
        p["y"] += p["vy"]

        p["vy"] += 0.08

        p["life"] -= 1

        if p["life"] <= 0:

            particles.remove(p)

        else:

            pygame.draw.circle(
                screen,
                p["color"],
                (int(p["x"]), int(p["y"])),
                p["size"]
            )


# =========================================================
# QUESTION
# =========================================================

def draw_question():

    panel = pygame.Rect(
        60,
        80,
        1160,
        135
    )

    pygame.draw.rect(
        screen,
        (12, 20, 35),
        panel,
        border_radius=18
    )

    pygame.draw.rect(
        screen,
        CYAN,
        panel,
        3,
        border_radius=18
    )

    lines = current_question.split("\n")

    y = 115

    for line in lines:

        draw_text(
            line,
            FONT,
            WHITE,
            WIDTH // 2,
            y,
            True
        )

        y += 32


# =========================================================
# TARGETS
# =========================================================

def draw_targets():

    for target in targets:

        rect = target["rect"]

        # -------------------------------------------------
        # IMPORTANT:
        # NO CORRECT ANSWER COLOR BEFORE SHOOTING
        # -------------------------------------------------

        if target["result"] == "CORRECT":
            border = GREEN

        elif target["result"] == "WRONG":
            border = RED

        else:
            border = CYAN

        pygame.draw.rect(
            screen,
            (18, 28, 48),
            rect,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            border,
            rect,
            3,
            border_radius=15
        )

        # Number circle
        pygame.draw.circle(
            screen,
            border,
            (rect.x + 27, rect.y + 27),
            17
        )

        draw_text(
            target["index"] + 1,
            FONT_SMALL,
            BLACK,
            rect.x + 27,
            rect.y + 27,
            True
        )

        # Answer
        answer = current_options[
            target["index"]
        ]

        lines = answer.split("\n")

        y = rect.y + 58

        for line in lines[:3]:

            draw_text(
                line,
                FONT_SMALL,
                WHITE,
                rect.centerx,
                y,
                True
            )

            y += 21


# =========================================================
# HUD
# =========================================================

def draw_hud():

    level = (
        normal_level
        if mode == "NORMAL"
        else advanced_level
    )

    draw_text(
        mode,
        FONT,
        GREEN if mode == "NORMAL" else PURPLE,
        20,
        15
    )

    draw_text(
        f"LEVEL {level}",
        FONT,
        WHITE,
        180,
        15
    )

    draw_text(
        f"SCORE {score}",
        FONT,
        YELLOW,
        370,
        15
    )

    draw_text(
        f"XP {xp}",
        FONT,
        CYAN,
        550,
        15
    )

    # HP
    draw_text(
        "HP",
        FONT_SMALL,
        WHITE,
        20,
        55
    )

    hp_bg = pygame.Rect(
        60,
        56,
        200,
        20
    )

    pygame.draw.rect(
        screen,
        DARK,
        hp_bg,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        RED,
        (
            60,
            56,
            int(200 * hp / max_hp),
            20
        ),
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        WHITE,
        hp_bg,
        2,
        border_radius=8
    )

    draw_text(
        f"{hp}/100",
        FONT_SMALL,
        WHITE,
        270,
        53
    )

    draw_text(
        f"BULLETS: {bullets}",
        FONT,
        YELLOW if bullets > 2 else RED,
        430,
        53
    )

    remaining = get_time()

    draw_text(
        f"TIME: {remaining:.1f}",
        FONT,
        GREEN if remaining > 5 else RED,
        650,
        53
    )

    hint = pygame.Rect(
        890,
        15,
        80,
        42
    )

    ctrl = pygame.Rect(
        980,
        15,
        80,
        42
    )

    exit_btn = pygame.Rect(
        1070,
        15,
        170,
        42
    )

    draw_button(hint, "HINT", CYAN)
    draw_button(ctrl, "CTRL", PURPLE)
    draw_button(exit_btn, "EXIT GAME", RED)


# =========================================================
# TIMER
# =========================================================

def get_time():

    elapsed = (
        pygame.time.get_ticks()
        - level_start_time
    ) / 1000

    return max(
        0,
        time_limit - elapsed
    )


# =========================================================
# CROSSHAIR
# =========================================================

def draw_crosshair():

    mx, my = pygame.mouse.get_pos()

    pygame.draw.circle(
        screen,
        CYAN,
        (mx, my),
        14,
        2
    )

    pygame.draw.line(
        screen,
        CYAN,
        (mx - 23, my),
        (mx - 5, my),
        2
    )

    pygame.draw.line(
        screen,
        CYAN,
        (mx + 5, my),
        (mx + 23, my),
        2
    )

    pygame.draw.line(
        screen,
        CYAN,
        (mx, my - 23),
        (mx, my - 5),
        2
    )

    pygame.draw.line(
        screen,
        CYAN,
        (mx, my + 5),
        (mx, my + 23),
        2
    )


# =========================================================
# GAME DRAW
# =========================================================

def draw_game():

    screen.fill(BLACK)

    # Background grid
    for x in range(0, WIDTH, 40):

        pygame.draw.line(
            screen,
            (12, 22, 35),
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, 40):

        pygame.draw.line(
            screen,
            (12, 22, 35),
            (0, y),
            (WIDTH, y)
        )

    draw_question()
    draw_targets()
    draw_hud()

    update_projectiles()
    update_particles()

    draw_gun()
    draw_crosshair()

    if message_timer > 0:

        color = (
            GREEN
            if "CORRECT" in message
            else RED
        )

        draw_text(
            message,
            FONT_BIG,
            color,
            WIDTH // 2,
            650,
            True
        )


# =========================================================
# EXIT POPUP
# =========================================================

def draw_exit_popup():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 180)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    panel = pygame.Rect(
        WIDTH // 2 - 300,
        HEIGHT // 2 - 170,
        600,
        340
    )

    pygame.draw.rect(
        screen,
        (15, 22, 38),
        panel,
        border_radius=20
    )

    pygame.draw.rect(
        screen,
        RED,
        panel,
        3,
        border_radius=20
    )

    draw_text(
        "EXIT GAME?",
        FONT_BIG,
        RED,
        panel.centerx,
        panel.y + 65,
        True
    )

    draw_text(
        "Are you sure you want to exit?",
        FONT,
        WHITE,
        panel.centerx,
        panel.y + 115,
        True
    )

    yes = pygame.Rect(
        panel.x + 65,
        panel.y + 200,
        210,
        60
    )

    cancel = pygame.Rect(
        panel.x + 325,
        panel.y + 200,
        210,
        60
    )

    # Highlight selected option
    yes_color = GREEN if exit_selection == 0 else RED
    cancel_color = GREEN if exit_selection == 1 else CYAN

    draw_button(
        yes,
        "YES, EXIT",
        yes_color
    )

    draw_button(
        cancel,
        "CANCEL",
        cancel_color
    )

    draw_text(
        "← → Select     ENTER Confirm     ESC Cancel",
        FONT_SMALL,
        GRAY,
        panel.centerx,
        panel.y + 300,
        True
    )


# =========================================================
# HINT POPUP
# =========================================================

def draw_hint_popup():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 150)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    panel = pygame.Rect(
        WIDTH // 2 - 300,
        HEIGHT // 2 - 140,
        600,
        280
    )

    pygame.draw.rect(
        screen,
        (12, 20, 35),
        panel,
        border_radius=18
    )

    pygame.draw.rect(
        screen,
        CYAN,
        panel,
        3,
        border_radius=18
    )

    draw_text(
        "HINT",
        FONT_BIG,
        CYAN,
        panel.centerx,
        panel.y + 50,
        True
    )

    draw_text(
        current_explanation,
        FONT_SMALL,
        WHITE,
        panel.centerx,
        panel.y + 115,
        True
    )

    draw_text(
        "Press ESC to close",
        FONT_SMALL,
        GRAY,
        panel.centerx,
        panel.y + 210,
        True
    )


# =========================================================
# CONTROLS POPUP
# =========================================================

def draw_controls_popup():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 160)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    panel = pygame.Rect(
        WIDTH // 2 - 330,
        HEIGHT // 2 - 200,
        660,
        400
    )

    pygame.draw.rect(
        screen,
        (12, 20, 35),
        panel,
        border_radius=18
    )

    pygame.draw.rect(
        screen,
        PURPLE,
        panel,
        3,
        border_radius=18
    )

    draw_text(
        "CONTROLS",
        FONT_BIG,
        PURPLE,
        panel.centerx,
        panel.y + 50,
        True
    )

    controls = [
        "Mouse = Aim",
        "Left Click = Shoot",
        "1 / 2 / 3 / 4 = Shoot Answer",
        "Ctrl + H = Hint",
        "Ctrl + C = Controls",
        "Ctrl + E = Exit",
        "ESC = Close"
    ]

    y = panel.y + 105

    for item in controls:

        draw_text(
            item,
            FONT_SMALL,
            WHITE,
            panel.centerx,
            y,
            True
        )

        y += 38


# =========================================================
# PLAYER OUT
# =========================================================

player_out_reason = "PLAYER OUT"


def draw_player_out():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 190)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    draw_text(
        "PLAYER OUT!",
        FONT_HUGE,
        RED,
        WIDTH // 2,
        160,
        True
    )

    draw_text(
        player_out_reason,
        FONT,
        WHITE,
        WIDTH // 2,
        225,
        True
    )

    retry = pygame.Rect(
        WIDTH // 2 - 220,
        310,
        200,
        65
    )

    revive = pygame.Rect(
        WIDTH // 2 + 20,
        310,
        200,
        65
    )

    menu = pygame.Rect(
        WIDTH // 2 - 100,
        410,
        200,
        55
    )

    draw_button(
        retry,
        "RETRY STAGE",
        CYAN
    )

    draw_button(
        revive,
        "REVIVE",
        GREEN
    )

    draw_button(
        menu,
        "MAIN MENU",
        PURPLE
    )


# =========================================================
# AMMO OVER
# =========================================================

def draw_ammo_over():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 180)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    draw_text(
        "BULLETS ARE OVER",
        FONT_HUGE,
        RED,
        WIDTH // 2,
        210,
        True
    )

    draw_text(
        "Revive to reload your ammunition",
        FONT,
        WHITE,
        WIDTH // 2,
        275,
        True
    )

    revive = pygame.Rect(
        WIDTH // 2 - 120,
        350,
        240,
        65
    )

    draw_button(
        revive,
        "REVIVE",
        GREEN
    )


# =========================================================
# STAGE CLEAR
# =========================================================

def draw_stage_clear():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 180)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    draw_text(
        "STAGE CLEAR!",
        FONT_HUGE,
        GREEN,
        WIDTH // 2,
        180,
        True
    )

    draw_text(
        "Python knowledge increased!",
        FONT,
        WHITE,
        WIDTH // 2,
        250,
        True
    )

    next_btn = pygame.Rect(
        WIDTH // 2 - 130,
        320,
        260,
        65
    )

    menu_btn = pygame.Rect(
        WIDTH // 2 - 100,
        420,
        200,
        55
    )

    draw_button(
        next_btn,
        "NEXT STAGE",
        GREEN
    )

    draw_button(
        menu_btn,
        "MAIN MENU",
        PURPLE
    )


# =========================================================
# NEXT LEVEL
# =========================================================

def next_level():

    global normal_level
    global advanced_level

    if mode == "NORMAL":
        normal_level += 1
    else:
        advanced_level += 1

    load_level()


# =========================================================
# RETRY STAGE
# =========================================================

def retry_stage():

    global normal_level
    global advanced_level
    global hp
    global state

    hp = max_hp

    if mode == "NORMAL":
        normal_level = stage_start_level
    else:
        advanced_level = stage_start_level

    load_level()

    state = "PLAYING"


# =========================================================
# REVIVE
# =========================================================

def revive():

    global hp
    global bullets
    global state

    hp = 50
    bullets = max_bullets

    load_level()

    state = "PLAYING"


# =========================================================
# BOSS
# =========================================================

def draw_boss():

    screen.fill(
        (15, 5, 22)
    )

    for x in range(0, WIDTH, 50):

        pygame.draw.line(
            screen,
            (45, 15, 55),
            (x, 0),
            (x, HEIGHT)
        )

    draw_text(
        "FINAL PYTHON BOSS",
        FONT_HUGE,
        RED,
        WIDTH // 2,
        60,
        True
    )

    # Boss
    bx = WIDTH // 2
    by = 220

    pygame.draw.circle(
        screen,
        (55, 15, 70),
        (bx, by),
        105
    )

    pygame.draw.circle(
        screen,
        RED,
        (bx, by),
        105,
        5
    )

    pygame.draw.circle(
        screen,
        CYAN,
        (bx - 35, by - 15),
        15
    )

    pygame.draw.circle(
        screen,
        CYAN,
        (bx + 35, by - 15),
        15
    )

    # HP
    pygame.draw.rect(
        screen,
        DARK,
        (390, 340, 500, 30)
    )

    pygame.draw.rect(
        screen,
        RED,
        (
            390,
            340,
            int(500 * boss_hp / boss_max_hp),
            30
        )
    )

    draw_text(
        f"BOSS HP: {boss_hp}",
        FONT,
        WHITE,
        WIDTH // 2,
        390,
        True
    )

    q, answers, correct = BOSS_QUESTIONS[
        (boss_level - 1) % len(BOSS_QUESTIONS)
    ]

    panel = pygame.Rect(
        150,
        430,
        980,
        90
    )

    pygame.draw.rect(
        screen,
        (25, 15, 35),
        panel,
        border_radius=12
    )

    draw_text(
        q,
        FONT_SMALL,
        WHITE,
        WIDTH // 2,
        465,
        True
    )

    for i in range(4):

        rect = pygame.Rect(
            150 + i * 245,
            540,
            220,
            70
        )

        draw_button(
            rect,
            f"{i+1}. {answers[i]}",
            CYAN
        )

    exit_btn = pygame.Rect(
        1040,
        15,
        200,
        45
    )

    draw_button(
        exit_btn,
        "EXIT GAME",
        RED
    )


def boss_answer(index):

    global boss_hp
    global boss_level
    global state
    global score
    global xp

    q, answers, correct = BOSS_QUESTIONS[
        (boss_level - 1) % len(BOSS_QUESTIONS)
    ]

    if index == correct:

        boss_hp -= 20
        score += 300
        xp += 100

        if boss_hp <= 0:

            state = "WIN"

        else:

            boss_level += 1

    else:

        # Boss wrong answer damage
        pass


# =========================================================
# WIN
# =========================================================

def draw_win():

    screen.fill(BLACK)

    draw_text(
        "PYTHON STRIKE COMPLETE!",
        FONT_HUGE,
        GREEN,
        WIDTH // 2,
        180,
        True
    )

    draw_text(
        "PYTHON BOSS DEFEATED",
        FONT_BIG,
        CYAN,
        WIDTH // 2,
        250,
        True
    )

    draw_text(
        f"FINAL SCORE: {score}",
        FONT,
        YELLOW,
        WIDTH // 2,
        330,
        True
    )

    draw_text(
        f"XP EARNED: {xp}",
        FONT,
        WHITE,
        WIDTH // 2,
        375,
        True
    )

    menu = pygame.Rect(
        WIDTH // 2 - 130,
        450,
        260,
        65
    )

    draw_button(
        menu,
        "MAIN MENU",
        PURPLE
    )


# =========================================================
# MOUSE HANDLER
# =========================================================

def handle_mouse(pos):

    global state
    global show_exit
    global show_hint
    global show_controls

    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    if state == "MENU":

        normal = pygame.Rect(
            WIDTH // 2 - 180,
            240,
            360,
            70
        )

        advanced = pygame.Rect(
            WIDTH // 2 - 180,
            330,
            360,
            70
        )

        controls = pygame.Rect(
            WIDTH // 2 - 180,
            425,
            170,
            55
        )

        exit_btn = pygame.Rect(
            WIDTH // 2 + 10,
            425,
            170,
            55
        )

        if normal.collidepoint(pos):
            start_game("NORMAL")

        elif advanced.collidepoint(pos):
            start_game("ADVANCED")

        elif controls.collidepoint(pos):
            show_controls = True

        elif exit_btn.collidepoint(pos):
            pygame.quit()
            sys.exit()

        return

    # -----------------------------------------------------
    # EXIT POPUP
    # -----------------------------------------------------

    if show_exit:

        panel_x = WIDTH // 2 - 300
        panel_y = HEIGHT // 2 - 170

        yes = pygame.Rect(
            panel_x + 65,
            panel_y + 200,
            210,
            60
        )

        cancel = pygame.Rect(
            panel_x + 325,
            panel_y + 200,
            210,
            60
        )

        if yes.collidepoint(pos):

            pygame.quit()
            sys.exit()

        elif cancel.collidepoint(pos):

            show_exit = False

        return

    # -----------------------------------------------------
    # HINT
    # -----------------------------------------------------

    if show_hint:

        return

    # -----------------------------------------------------
    # CONTROLS
    # -----------------------------------------------------

    if show_controls:

        show_controls = False
        return

    # -----------------------------------------------------
    # PLAYING
    # -----------------------------------------------------

    if state == "PLAYING":

        exit_btn = pygame.Rect(
            1070,
            15,
            170,
            42
        )

        hint_btn = pygame.Rect(
            890,
            15,
            80,
            42
        )

        ctrl_btn = pygame.Rect(
            980,
            15,
            80,
            42
        )

        if exit_btn.collidepoint(pos):

            show_exit = True
            return

        if hint_btn.collidepoint(pos):

            show_hint = True
            return

        if ctrl_btn.collidepoint(pos):

            show_controls = True
            return

        # Actual shooting anywhere
        if pos[1] > 80:

            fire()

        return

    # -----------------------------------------------------
    # PLAYER OUT
    # -----------------------------------------------------

    if state == "PLAYER_OUT":

        retry = pygame.Rect(
            WIDTH // 2 - 220,
            310,
            200,
            65
        )

        revive_btn = pygame.Rect(
            WIDTH // 2 + 20,
            310,
            200,
            65
        )

        menu = pygame.Rect(
            WIDTH // 2 - 100,
            410,
            200,
            55
        )

        if retry.collidepoint(pos):

            retry_stage()

        elif revive_btn.collidepoint(pos):

            revive()

        elif menu.collidepoint(pos):

            state = "MENU"

        return

    # -----------------------------------------------------
    # AMMO
    # -----------------------------------------------------

    if state == "AMMO_OVER":

        revive_btn = pygame.Rect(
            WIDTH // 2 - 120,
            350,
            240,
            65
        )

        if revive_btn.collidepoint(pos):

            revive()

        return

    # -----------------------------------------------------
    # STAGE CLEAR
    # -----------------------------------------------------

    if state == "STAGE_CLEAR":

        next_btn = pygame.Rect(
            WIDTH // 2 - 130,
            320,
            260,
            65
        )

        menu = pygame.Rect(
            WIDTH // 2 - 100,
            420,
            200,
            55
        )

        if next_btn.collidepoint(pos):

            next_level()
            state = "PLAYING"

        elif menu.collidepoint(pos):

            state = "MENU"

        return

    # -----------------------------------------------------
    # BOSS
    # -----------------------------------------------------

    if state == "BOSS":

        exit_btn = pygame.Rect(
            1040,
            15,
            200,
            45
        )

        if exit_btn.collidepoint(pos):

            show_exit = True
            return

        for i in range(4):

            rect = pygame.Rect(
                150 + i * 245,
                540,
                220,
                70
            )

            if rect.collidepoint(pos):

                boss_answer(i)
                return

    # -----------------------------------------------------
    # WIN
    # -----------------------------------------------------

    if state == "WIN":

        menu = pygame.Rect(
            WIDTH // 2 - 130,
            450,
            260,
            65
        )

        if menu.collidepoint(pos):

            state = "MENU"


# =========================================================
# KEYBOARD
# =========================================================

def handle_keyboard(event):

    global show_exit
    global show_hint
    global show_controls
    global exit_selection
    global state

    # -----------------------------------------------------
    # ESC
    # -----------------------------------------------------

    if event.key == pygame.K_ESCAPE:

        if show_exit:

            show_exit = False

        elif show_hint:

            show_hint = False

        elif show_controls:

            show_controls = False

        return

    # -----------------------------------------------------
    # CTRL + E
    # -----------------------------------------------------

    if (
        event.key == pygame.K_e
        and pygame.key.get_mods() & pygame.KMOD_CTRL
    ):

        if state != "MENU":

            show_exit = True
            exit_selection = 0

        return

    # -----------------------------------------------------
    # EXIT POPUP KEYBOARD
    # -----------------------------------------------------

    if show_exit:

        if event.key == pygame.K_LEFT:

            exit_selection = 0

        elif event.key == pygame.K_RIGHT:

            exit_selection = 1

        elif event.key == pygame.K_RETURN:

            if exit_selection == 0:

                pygame.quit()
                sys.exit()

            else:

                show_exit = False

        return

    # -----------------------------------------------------
    # CTRL + H
    # -----------------------------------------------------

    if (
        event.key == pygame.K_h
        and pygame.key.get_mods() & pygame.KMOD_CTRL
    ):

        if state == "PLAYING":

            show_hint = not show_hint

        return

    # -----------------------------------------------------
    # CTRL + C
    # -----------------------------------------------------

    if (
        event.key == pygame.K_c
        and pygame.key.get_mods() & pygame.KMOD_CTRL
    ):

        if state == "PLAYING":

            show_controls = not show_controls

        return

    # -----------------------------------------------------
    # POPUPS BLOCK GAME
    # -----------------------------------------------------

    if show_hint or show_controls:

        return

    # -----------------------------------------------------
    # PLAYING
    # -----------------------------------------------------

    if state == "PLAYING":

        if event.key in [
            pygame.K_1,
            pygame.K_2,
            pygame.K_3,
            pygame.K_4
        ]:

            index = event.key - pygame.K_1

            if index < len(targets):

                target = targets[index]

                # Aim mouse at selected answer
                pygame.mouse.set_pos(
                    target["rect"].center
                )

                fire()

    # -----------------------------------------------------
    # BOSS
    # -----------------------------------------------------

    elif state == "BOSS":

        if event.key in [
            pygame.K_1,
            pygame.K_2,
            pygame.K_3,
            pygame.K_4
        ]:

            index = event.key - pygame.K_1

            boss_answer(index)


# =========================================================
# TIMER
# =========================================================

def check_timer():

    global state
    global player_out_reason

    if state != "PLAYING":
        return

    if get_time() <= 0:

        player_out_reason = "TIME OUT"

        state = "PLAYER_OUT"


# =========================================================
# MAIN LOOP
# =========================================================

running = True

while running:

    clock.tick(60)

    if recoil > 0:
        recoil -= 1

    if muzzle_flash > 0:
        muzzle_flash -= 1

    if message_timer > 0:
        message_timer -= 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            handle_keyboard(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                handle_mouse(event.pos)

    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    if state == "MENU":

        draw_menu()

    elif state == "PLAYING":

        check_timer()
        draw_game()

    elif state == "PLAYER_OUT":

        draw_game()
        draw_player_out()

    elif state == "AMMO_OVER":

        draw_game()
        draw_ammo_over()

    elif state == "STAGE_CLEAR":

        draw_game()
        draw_stage_clear()

    elif state == "BOSS":

        draw_boss()
        update_particles()

    elif state == "WIN":

        draw_win()

    # -----------------------------------------------------
    # POPUPS
    # -----------------------------------------------------

    if show_exit:

        draw_exit_popup()

    elif show_hint and state == "PLAYING":

        draw_hint_popup()

    elif show_controls and state == "PLAYING":

        draw_controls_popup()

    pygame.display.flip()


pygame.quit()
sys.exit()