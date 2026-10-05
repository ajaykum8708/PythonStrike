import pygame
import math
import random
import sys

# ============================================================
# PYTHON STRIKE - LEARN PYTHON BY SHOOTING
# COMPLETE VERSION
# Normal Mode: 30 Levels -> Final Boss
# Advanced Mode: 20 Levels -> Final Boss
# ============================================================

pygame.init()

try:
    pygame.mixer.init()
except pygame.error:
    pass

WIDTH, HEIGHT = 1200, 720

SCREEN = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.RESIZABLE | pygame.SCALED
)

fullscreen = False

pygame.display.set_caption(
    "Python Strike - Learn Python by Shooting"
)

CLOCK = pygame.time.Clock()

# ============================================================
# COLORS
# ============================================================

BG = (8, 12, 24)
PANEL = (18, 25, 45)

CYAN = (50, 220, 255)
BLUE = (40, 120, 255)
GREEN = (60, 230, 120)
RED = (255, 70, 80)
YELLOW = (255, 215, 70)
WHITE = (240, 245, 255)
GRAY = (145, 155, 180)
PURPLE = (180, 90, 255)
ORANGE = (255, 145, 50)
DARK = (4, 7, 15)

# ============================================================
# FONTS
# ============================================================

FONT_BIG = pygame.font.SysFont("consolas", 42, bold=True)
FONT_TITLE = pygame.font.SysFont("consolas", 34, bold=True)
FONT_MED = pygame.font.SysFont("consolas", 24, bold=True)
FONT = pygame.font.SysFont("consolas", 19)
FONT_SMALL = pygame.font.SysFont("consolas", 16)

# ============================================================
# SOUND
# ============================================================

def make_sound(kind):
    try:
        rate = 44100

        duration = {
            "shoot": 0.07,
            "correct": 0.18,
            "wrong": 0.16,
            "explosion": 0.22,
            "timeout": 0.35,
            "revive": 0.30,
            "clear": 0.30,
            "win": 0.55,
        }.get(kind, 0.15)

        n = int(rate * duration)
        buf = bytearray()

        for i in range(n):

            t = i / rate

            if kind == "shoot":
                freq = 700 - 500 * t / duration
                amp = 7000 * (1 - t / duration)

            elif kind == "correct":
                freq = 500 + 700 * t / duration
                amp = 6500 * (1 - t / duration)

            elif kind == "wrong":
                freq = 220 - 80 * t / duration
                amp = 6500 * (1 - t / duration)

            elif kind == "explosion":
                freq = 90 + random.random() * 120
                amp = 9000 * (1 - t / duration)

            elif kind == "timeout":
                freq = 150
                amp = 7000 * (1 - t / duration)

            elif kind == "revive":
                freq = 300 + 900 * t / duration
                amp = 7000 * (1 - t / duration)

            elif kind == "clear":
                freq = 450 + 500 * t / duration
                amp = 7000 * (1 - t / duration)

            else:
                freq = 500 + 1000 * t / duration
                amp = 8000 * (1 - t / duration)

            value = int(
                math.sin(2 * math.pi * freq * t) * amp
            )

            value = max(-32767, min(32767, value))

            sample = value.to_bytes(
                2,
                byteorder="little",
                signed=True
            )

            buf += sample + sample

        return pygame.mixer.Sound(buffer=bytes(buf))

    except Exception:
        return None


SOUNDS = {
    k: make_sound(k)
    for k in [
        "shoot",
        "correct",
        "wrong",
        "explosion",
        "timeout",
        "revive",
        "clear",
        "win"
    ]
}


def play_sound(name):

    sound = SOUNDS.get(name)

    if sound:

        try:
            sound.play()

        except pygame.error:
            pass


# ============================================================
# NORMAL QUESTIONS - 30
# ============================================================

NORMAL_QUESTIONS = [

    (
        "What is the output of print(2 + 3)?",
        ["4", "5", "6", "23"],
        1
    ),

    (
        "Which symbol is used for a comment in Python?",
        ["//", "#", "<!--", "/*"],
        1
    ),

    (
        "Which function displays text?",
        ["show()", "echo()", "print()", "write()"],
        2
    ),

    (
        "What is the type of 10?",
        ["str", "float", "int", "bool"],
        2
    ),

    (
        "Which keyword creates a function?",
        ["func", "define", "def", "function"],
        2
    ),

    (
        "What is 10 // 3?",
        ["2", "3", "3.33", "1"],
        1
    ),

    (
        "What is 10 % 3?",
        ["0", "1", "2", "3"],
        1
    ),

    (
        "Which operator means power?",
        ["^", "**", "//", "%%"],
        1
    ),

    (
        "What does == check?",
        [
            "Assignment",
            "Equality",
            "Identity only",
            "Division"
        ],
        1
    ),

    (
        "Which keyword is used for a condition?",
        ["if", "when", "case", "check"],
        0
    ),

    (
        "Which loop is commonly used to iterate over a list?",
        ["repeat", "for", "loop", "each"],
        1
    ),

    (
        "What does range(3) produce?",
        [
            "1,2,3",
            "0,1,2",
            "0,1,2,3",
            "3 only"
        ],
        1
    ),

    (
        "Which keyword stops a loop?",
        ["stop", "exit", "break", "end"],
        2
    ),

    (
        "Which keyword skips to the next iteration?",
        ["skip", "continue", "next", "pass"],
        1
    ),

    (
        "What does len([1,2,3]) return?",
        ["2", "3", "4", "1"],
        1
    ),

    (
        "Which brackets create a list?",
        ["()", "{}", "[]", "<>"],
        2
    ),

    (
        "Which brackets create a tuple?",
        ["()", "[]", "{}", "<>"],
        0
    ),

    (
        "Which method adds an item to a list?",
        ["add()", "append()", "push()", "insertEnd()"],
        1
    ),

    (
        "What does 'Python'[0] return?",
        ["P", "y", "n", "Python"],
        0
    ),

    (
        "Which type stores key-value pairs?",
        ["list", "tuple", "dict", "set"],
        2
    ),

    (
        "What does return do in a function?",
        [
            "Prints",
            "Ends function and sends a value",
            "Loops",
            "Imports"
        ],
        1
    ),

    (
        "Which keyword imports a module?",
        ["include", "using", "import", "module"],
        2
    ),

    (
        "What does bool(0) return?",
        ["True", "False", "0", "None"],
        1
    ),

    (
        "Which is a valid variable name?",
        ["2name", "my-name", "my_name", "class"],
        2
    ),

    (
        "What does str(123) return?",
        [
            "123 as string",
            "123 as int",
            "True",
            "None"
        ],
        0
    ),

    (
        "What is a dictionary key used for?",
        [
            "Indexing by name/key",
            "Looping only",
            "Math only",
            "Printing"
        ],
        0
    ),

    (
        "Which collection removes duplicate values?",
        ["list", "tuple", "set", "dict"],
        2
    ),

    (
        "What does input() return by default?",
        ["int", "float", "str", "bool"],
        2
    ),

    (
        "Which keyword handles an exception?",
        ["catch", "except", "error", "handle"],
        1
    ),

    (
        "Which block runs whether an exception happens or not?",
        ["finally", "always", "last", "done"],
        0
    ),
]


# ============================================================
# ADVANCED QUESTIONS - 20
# ============================================================

ADVANCED_QUESTIONS = [

    (
        "What does len('Python') return?",
        ["5", "6", "7", "0"],
        1
    ),

    (
        "Which keyword defines a function?",
        ["func", "def", "function", "lambda"],
        1
    ),

    (
        "What is the output of x = [1,2,3]; print(x[-1])?",
        ["1", "2", "3", "Error"],
        2
    ),

    (
        "What is the output of print(2 ** 3 ** 1)?",
        ["64", "16", "8", "6"],
        2
    ),

    (
        "What is the output of [x*x for x in range(4) if x%2==0]?",
        ["[0,1,4]", "[0,4]", "[1,4]", "[2,4]"],
        1
    ),

    (
        "What does LEGB stand for?",
        [
            "Local, Enclosed, Global, Built-in",
            "List, Enum, Global, Boolean",
            "Local, External, General, Base",
            "Loop, Expression, Global, Block"
        ],
        0
    ),

    (
        "What is the output? f=lambda x:x+2; print(f(5))",
        ["5", "7", "10", "25"],
        1
    ),

    (
        "What does map() return in Python 3?",
        [
            "A list",
            "A map iterator",
            "A tuple",
            "A set"
        ],
        1
    ),

    (
        "What does filter() use to select values?",
        [
            "A condition/function",
            "A class",
            "A file",
            "A loop keyword"
        ],
        0
    ),

    (
        "Which import is needed for reduce()?",
        [
            "math",
            "functools",
            "collections",
            "operator"
        ],
        1
    ),

    (
        "What does *args collect?",
        [
            "Keyword arguments",
            "Positional arguments",
            "Files",
            "Classes"
        ],
        1
    ),

    (
        "What does **kwargs collect?",
        [
            "Positional arguments",
            "Keyword arguments",
            "Only integers",
            "Lists"
        ],
        1
    ),

    (
        "A closure can remember variables from which scope?",
        [
            "Enclosing scope",
            "Only global",
            "Only built-in",
            "No scope"
        ],
        0
    ),

    (
        "What does a generator function normally use?",
        [
            "yield",
            "return only",
            "generate",
            "nextonly"
        ],
        0
    ),

    (
        "What does iter(obj) return?",
        [
            "Iterator",
            "List",
            "String",
            "Boolean"
        ],
        0
    ),

    (
        "What does next(iterator) do?",
        [
            "Creates a list",
            "Gets the next item",
            "Deletes iterator",
            "Sorts it"
        ],
        1
    ),

    (
        "What is a decorator commonly used for?",
        [
            "Wrapping/extending function behavior",
            "Creating RAM",
            "Deleting classes",
            "Opening files only"
        ],
        0
    ),

    (
        "Which method initializes an object?",
        [
            "__start__",
            "__init__",
            "__newobject__",
            "init()"
        ],
        1
    ),

    (
        "What is inheritance?",
        [
            "A class receiving behavior from another class",
            "Copying a file",
            "Looping",
            "Importing a package"
        ],
        0
    ),

    (
        "What is polymorphism?",
        [
            "Same interface/name can work with different object types",
            "Only one class",
            "Only recursion",
            "Memory deletion"
        ],
        0
    )
]


# ============================================================
# FINAL BOSS QUESTIONS
# ============================================================

BOSS_QUESTIONS = [

    (
        "What is the output?\n"
        "def f(a=[]):\n"
        "    a.append(1)\n"
        "    return a\n"
        "print(f()); print(f())",

        [
            "[1] then [1]",
            "[1] then [1, 1]",
            "Error",
            "None"
        ],

        1
    ),

    (
        "What is the output?\n"
        "x = [1,2,3]\n"
        "print(x[::-1])",

        [
            "[1,2,3]",
            "[3,2,1]",
            "[2,1]",
            "Error"
        ],

        1
    ),

    (
        "Which statement about generators is correct?",

        [
            "They store every result immediately",
            "They produce values lazily",
            "They cannot use yield",
            "They are always lists"
        ],

        1
    ),

    (
        "What is the purpose of __name__ == '__main__'?",

        [
            "Runs code only when the file is executed directly",
            "Creates a class",
            "Imports every module",
            "Deletes variables"
        ],

        0
    ),

    (
        "What does this create: {x: x*x for x in range(3)}?",

        [
            "A set",
            "A dictionary",
            "A list",
            "A tuple"
        ],

        1
    )
]


# ============================================================
# GAME STATE
# ============================================================

state = "MENU"
mode = None

level = 1
stage = 1

score = 0
xp = 0

bullets = 6
hp = 100

time_left = 60.0

stage_start_level = 1

question = None
options = []
correct_index = 0

targets = []
projectiles = []
particles = []

hits_this_question = 0

message = ""
message_color = WHITE
message_timer = 0

show_hint = False
show_controls = False
show_exit = False

exit_choice = 0

boss_index = 0
boss_hp = 100

advanced_level = 1

# ============================================================
# SPEED
# ============================================================

SPEED_LEVELS = [
    1.0 + 0.5 * i
    for i in range(19)
]

speed_index = 0
speed_multiplier = SPEED_LEVELS[speed_index]


# ============================================================
# HELPERS
# ============================================================

def text(surface, s, font, color, pos, center=False):

    img = font.render(str(s), True, color)

    rect = img.get_rect()

    if center:
        rect.center = pos
    else:
        rect.topleft = pos

    surface.blit(img, rect)

    return rect


def clamp(v, a, b):

    return max(a, min(b, v))


def set_message(msg, color=WHITE, duration=1.2):

    global message
    global message_color
    global message_timer

    message = msg
    message_color = color
    message_timer = duration


# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    global level
    global stage
    global score
    global xp
    global bullets
    global hp
    global time_left
    global stage_start_level
    global boss_index
    global boss_hp
    global advanced_level
    global state
    global show_hint
    global show_controls
    global show_exit
    global exit_choice
    global speed_index
    global speed_multiplier

    level = 1
    stage = 1

    score = 0
    xp = 0

    bullets = 6
    hp = 100

    time_left = 60.0

    stage_start_level = 1

    boss_index = 0
    boss_hp = 100

    advanced_level = 1

    speed_index = 0
    speed_multiplier = SPEED_LEVELS[speed_index]

    show_hint = False
    show_controls = False
    show_exit = False

    exit_choice = 0

    state = "PLAYING"

    load_question()


# ============================================================
# STAGE
# ============================================================

def stage_for_level(lv):

    return ((lv - 1) // 5) + 1


# ============================================================
# GET CURRENT QUESTION
# ============================================================

def get_question():

    if mode == "NORMAL":

        index = (level - 1) % len(NORMAL_QUESTIONS)

        return NORMAL_QUESTIONS[index]

    elif mode == "ADVANCED":

        index = advanced_level - 1

        index = max(
            0,
            min(
                index,
                len(ADVANCED_QUESTIONS) - 1
            )
        )

        return ADVANCED_QUESTIONS[index]

    return NORMAL_QUESTIONS[0]


# ============================================================
# LOAD QUESTION
# ============================================================

def load_question():

    global question
    global options
    global correct_index
    global bullets
    global time_left
    global targets
    global projectiles
    global show_hint
    global hits_this_question

    question, original_options, original_correct = get_question()

    pairs = list(
        enumerate(original_options)
    )

    random.shuffle(pairs)

    options = [
        item[1]
        for item in pairs
    ]

    correct_index = next(
        i
        for i, item in enumerate(pairs)
        if item[0] == original_correct
    )

    bullets = max(
        bullets,
        6
    )

    time_left = 60.0

    show_hint = False

    projectiles = []

    hits_this_question = 0

    create_targets()


# ============================================================
# CREATE TARGETS
# ============================================================

def create_targets():

    global targets

    targets = []

    positions = [
        (260, 285),
        (480, 285),
        (700, 285),
        (920, 285)
    ]

    for i, option in enumerate(options):

        x, y = positions[i]

        angle = random.uniform(
            0,
            math.pi * 2
        )

        speed = random.uniform(
            18,
            34
        )

        targets.append({

            "x": float(x),
            "y": float(y),

            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,

            "r": 55,

            "text": option,

            "index": i,

            "alive": True,

            "hit": False
        })


# ============================================================
# RETRY STAGE
# ============================================================

def reset_to_stage_start():

    global level
    global stage
    global hp
    global bullets
    global time_left
    global state

    level = stage_start_level

    hp = 100

    bullets = 6

    time_left = 60.0

    state = "PLAYING"

    load_question()

    set_message(
        f"RETRYING STAGE {stage}",
        YELLOW,
        1.5
    )


# ============================================================
# ADVANCE LEVEL
# ============================================================

def advance_level():

    global level
    global stage
    global stage_start_level
    global state
    global xp
    global score
    global advanced_level

    # ========================================================
    # NORMAL MODE
    # ========================================================

    if mode == "NORMAL":

        score += 100
        xp += 20

        play_sound("correct")

        old_stage = stage

        level += 1

        # Level 30 complete
        if level > 30:

            start_boss()

            return

        stage = stage_for_level(level)

        if stage != old_stage:

            stage_start_level = level

            set_message(
                f"STAGE {stage} START!",
                CYAN,
                1.5
            )

        else:

            set_message(
                "✓ CORRECT HIT!",
                GREEN,
                0.9
            )

        load_question()

        return

    # ========================================================
    # ADVANCED MODE
    # ========================================================

    if mode == "ADVANCED":

        score += 150
        xp += 30

        play_sound("correct")

        # Level 20 completed
        if advanced_level >= 20:

            set_message(
                "ADVANCED MODE COMPLETE!",
                PURPLE,
                1.5
            )

            start_boss()

            return

        # Next level
        advanced_level += 1

        set_message(
            f"ADVANCED LEVEL {advanced_level}!",
            PURPLE,
            1.0
        )

        load_question()


# ============================================================
# PLAYER OUT
# ============================================================

def player_out(reason="PLAYER OUT"):

    global state

    if state != "PLAYING":
        return

    if reason == "TIME OUT!":

        play_sound("timeout")

    else:

        play_sound("wrong")

    set_message(
        reason,
        RED,
        1.5
    )

    state = "OUT"


# ============================================================
# REVIVE
# ============================================================

def revive():

    global hp
    global bullets
    global time_left
    global state

    hp = 100

    bullets = 6

    time_left = 60.0

    state = "PLAYING"

    load_question()

    play_sound("revive")

    set_message(
        "PLAYER REVIVED!",
        GREEN,
        1.8
    )


# ============================================================
# HINT
# ============================================================

def use_hint():

    global score
    global show_hint

    if score < 30:

        set_message(
            "Need 30 SCORE for a hint!",
            YELLOW,
            1.3
        )

        return

    score -= 30

    show_hint = not show_hint


# ============================================================
# BOSS START
# ============================================================

def start_boss():

    global boss_index
    global boss_hp
    global state

    boss_index = 0

    boss_hp = 100

    state = "BOSS"

    play_sound("clear")


# ============================================================
# BOSS ANSWER
# ============================================================

def boss_answer(index):

    global boss_index
    global boss_hp
    global state
    global score
    global xp
    global hp

    if index == BOSS_QUESTIONS[boss_index][2]:

        boss_hp -= 20

        score += 200

        xp += 50

        play_sound("correct")

        explode(
            WIDTH // 2,
            260,
            30
        )

        set_message(
            "BOSS HIT! -20 HP",
            GREEN,
            1.0
        )

        boss_index += 1

        if boss_index >= len(BOSS_QUESTIONS):

            state = "WIN"

            play_sound("win")

            return

    else:

        hp -= 15

        set_message(
            "WRONG BOSS ANSWER! -15 HP",
            RED,
            1.0
        )

        play_sound("wrong")

        if hp <= 0:

            hp = 0

            state = "OUT"


# ============================================================
# SHOOT
# ============================================================

def shoot_toward(mx, my):

    global bullets

    if bullets <= 0:

        set_message(
            "BULLETS OVER - PLAYER KNOCKED DOWN!",
            RED,
            1.5
        )

        player_out(
            "BULLETS OVER - PLAYER KNOCKED DOWN!"
        )

        return

    bullets -= 1

    play_sound("shoot")

    gun_x = 1030
    gun_y = 600

    dx = mx - gun_x
    dy = my - gun_y

    dist = max(
        1,
        math.hypot(dx, dy)
    )

    projectiles.append({

        "x": float(gun_x),
        "y": float(gun_y),

        "vx": dx / dist * 900,
        "vy": dy / dist * 900,

        "life": 1.2
    })


# ============================================================
# UPDATE PROJECTILES
# ============================================================

def update_projectiles(dt):

    global projectiles
    global hits_this_question
    global hp

    remaining = []

    for p in projectiles:

        p["x"] += p["vx"] * dt

        p["y"] += p["vy"] * dt

        p["life"] -= dt

        hit = False

        for target in targets:

            if not target["alive"]:
                continue

            d = math.hypot(
                p["x"] - target["x"],
                p["y"] - target["y"]
            )

            if d < target["r"] + 10:

                target["alive"] = False
                target["hit"] = True

                hits_this_question += 1

                explode(
                    target["x"],
                    target["y"],
                    20
                )

                # Correct
                if target["index"] == correct_index:

                    advance_level()

                # Wrong
                else:

                    hp -= 25

                    play_sound("wrong")

                    set_message(
                        "✗ WRONG TARGET! -25 HP",
                        RED,
                        1.2
                    )

                    if hp <= 0:

                        hp = 0

                        player_out()

                hit = True

                break

        if (
            not hit
            and p["life"] > 0
            and -50 < p["x"] < WIDTH + 50
            and -50 < p["y"] < HEIGHT + 50
        ):

            remaining.append(p)

    projectiles = remaining

    # All bullets used
    if (
        state == "PLAYING"
        and bullets <= 0
        and not projectiles
    ):

        player_out(
            "BULLETS OVER - PLAYER KNOCKED DOWN!"
        )


# ============================================================
# UPDATE TARGETS
# ============================================================

def update_targets(dt):

    for t in targets:

        if not t["alive"]:
            continue

        t["x"] += (
            t["vx"]
            * speed_multiplier
            * dt
        )

        t["y"] += (
            t["vy"]
            * speed_multiplier
            * dt
        )

        if t["x"] < 180 or t["x"] > 950:

            t["vx"] *= -1

            t["x"] = clamp(
                t["x"],
                180,
                950
            )

        if t["y"] < 200 or t["y"] > 430:

            t["vy"] *= -1

            t["y"] = clamp(
                t["y"],
                200,
                430
            )

        if random.random() < 0.008:

            angle = (
                math.atan2(
                    t["vy"],
                    t["vx"]
                )
                + random.uniform(
                    -0.35,
                    0.35
                )
            )

            speed = random.uniform(
                18,
                34
            )

            t["vx"] = (
                math.cos(angle)
                * speed
            )

            t["vy"] = (
                math.sin(angle)
                * speed
            )


# ============================================================
# EXPLOSION
# ============================================================

def explode(x, y, count=15):

    for _ in range(count):

        a = random.random() * math.pi * 2

        speed = random.uniform(
            50,
            220
        )

        particles.append({

            "x": x,
            "y": y,

            "vx": math.cos(a) * speed,
            "vy": math.sin(a) * speed,

            "life": random.uniform(
                0.3,
                0.8
            ),

            "r": random.randint(
                2,
                5
            )
        })

    play_sound("explosion")


# ============================================================
# UPDATE PARTICLES
# ============================================================

def update_particles(dt):

    for p in particles:

        p["x"] += p["vx"] * dt

        p["y"] += p["vy"] * dt

        p["vy"] += 160 * dt

        p["life"] -= dt

    particles[:] = [
        p
        for p in particles
        if p["life"] > 0
    ]


# ============================================================
# SPEED
# ============================================================

def cycle_speed():

    global speed_index
    global speed_multiplier

    speed_index = (
        speed_index + 1
    ) % len(SPEED_LEVELS)

    speed_multiplier = SPEED_LEVELS[
        speed_index
    ]

    set_message(
        f"TARGET SPEED: {speed_multiplier:g}X",
        ORANGE if speed_multiplier >= 5 else CYAN,
        1.0
    )


# ============================================================
# WINDOW
# ============================================================

def toggle_window_size():

    global fullscreen
    global SCREEN

    try:

        import ctypes

        hwnd = pygame.display.get_wm_info().get(
            "window"
        )

        if hwnd:

            user32 = ctypes.windll.user32

            SW_RESTORE = 9
            SW_MAXIMIZE = 3

            if user32.IsZoomed(hwnd):

                user32.ShowWindow(
                    hwnd,
                    SW_RESTORE
                )

                set_message(
                    "WINDOW RESTORED",
                    CYAN,
                    1.0
                )

            else:

                user32.ShowWindow(
                    hwnd,
                    SW_MAXIMIZE
                )

                set_message(
                    "WINDOW MAXIMIZED",
                    GREEN,
                    1.0
                )

            return

    except Exception:
        pass

    fullscreen = not fullscreen

    flags = (
        pygame.FULLSCREEN | pygame.SCALED
        if fullscreen
        else pygame.RESIZABLE | pygame.SCALED
    )

    SCREEN = pygame.display.set_mode(
        (WIDTH, HEIGHT),
        flags
    )


# ============================================================
# DRAW BACKGROUND
# ============================================================

def draw_background():

    SCREEN.fill(BG)

    for x in range(
        0,
        WIDTH,
        50
    ):

        pygame.draw.line(
            SCREEN,
            (13, 25, 45),
            (x, 0),
            (x, HEIGHT),
            1
        )

    for y in range(
        0,
        HEIGHT,
        50
    ):

        pygame.draw.line(
            SCREEN,
            (13, 25, 45),
            (0, y),
            (WIDTH, y),
            1
        )

    pygame.draw.line(
        SCREEN,
        CYAN,
        (0, 90),
        (WIDTH, 90),
        2
    )

    pygame.draw.line(
        SCREEN,
        (20, 90, 130),
        (0, 655),
        (WIDTH, 655),
        1
    )


# ============================================================
# MENU
# ============================================================

def draw_menu():

    draw_background()

    text(
        SCREEN,
        "PYTHON STRIKE",
        FONT_BIG,
        CYAN,
        (WIDTH // 2, 90),
        True
    )

    text(
        SCREEN,
        "LEARN PYTHON BY SHOOTING",
        FONT,
        GRAY,
        (WIDTH // 2, 135),
        True
    )

    buttons = [

        ("NORMAL MODE", 220, GREEN),

        ("ADVANCED MODE", 300, PURPLE),

        ("CONTROLS", 380, CYAN),

        ("EXIT GAME", 460, RED)
    ]

    for label, y, color in buttons:

        rect = pygame.Rect(
            350,
            y,
            500,
            58
        )

        pygame.draw.rect(
            SCREEN,
            PANEL,
            rect,
            border_radius=12
        )

        pygame.draw.rect(
            SCREEN,
            color,
            rect,
            2,
            border_radius=12
        )

        text(
            SCREEN,
            label,
            FONT_MED,
            color,
            rect.center,
            True
        )

    text(
        SCREEN,
        "Mouse = Aim & Shoot   |   1-4 = Quick Shoot",
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, 570),
        True
    )


# ============================================================
# CONTROLS
# ============================================================

def draw_controls():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 210)
    )

    SCREEN.blit(
        overlay,
        (0, 0)
    )

    rect = pygame.Rect(
        230,
        105,
        740,
        500
    )

    pygame.draw.rect(
        SCREEN,
        PANEL,
        rect,
        border_radius=18
    )

    pygame.draw.rect(
        SCREEN,
        CYAN,
        rect,
        2,
        border_radius=18
    )

    text(
        SCREEN,
        "CONTROLS",
        FONT_TITLE,
        CYAN,
        (WIDTH // 2, 145),
        True
    )

    lines = [

        "Mouse: Aim gun",

        "Left Click: Shoot energy projectile",

        "1 / 2 / 3 / 4: Auto-aim + shoot option 1-4",

        "CTRL + H: Hint",

        "CTRL + C: Controls",

        "CTRL + E: Exit Game",

        "ESC: Close popup",

        "If all bullets miss: PLAYER OUT + REVIVE",

        "CTRL + S: SPEED UP (1X -> 10X)",

        "CTRL + R: REVIVE when PLAYER OUT",

        "CTRL + M: Maximize / Restore Window",

        "F11: Fullscreen / Window"
    ]

    y = 195

    for line in lines:

        text(
            SCREEN,
            line,
            FONT,
            WHITE,
            (300, y)
        )

        y += 40

    text(
        SCREEN,
        "Press any key or click to close",
        FONT_SMALL,
        YELLOW,
        (WIDTH // 2, 565),
        True
    )


# ============================================================
# EXIT POPUP
# ============================================================

def draw_exit_popup():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 180)
    )

    SCREEN.blit(
        overlay,
        (0, 0)
    )

    rect = pygame.Rect(
        350,
        230,
        500,
        250
    )

    pygame.draw.rect(
        SCREEN,
        PANEL,
        rect,
        border_radius=18
    )

    pygame.draw.rect(
        SCREEN,
        RED,
        rect,
        2,
        border_radius=18
    )

    text(
        SCREEN,
        "EXIT GAME?",
        FONT_TITLE,
        WHITE,
        (WIDTH // 2, 280),
        True
    )

    yes = pygame.Rect(
        410,
        350,
        160,
        55
    )

    no = pygame.Rect(
        630,
        350,
        160,
        55
    )

    pygame.draw.rect(
        SCREEN,
        RED if exit_choice == 0 else PANEL,
        yes,
        border_radius=10
    )

    pygame.draw.rect(
        SCREEN,
        GREEN if exit_choice == 1 else PANEL,
        no,
        border_radius=10
    )

    pygame.draw.rect(
        SCREEN,
        RED,
        yes,
        2,
        border_radius=10
    )

    pygame.draw.rect(
        SCREEN,
        GREEN,
        no,
        2,
        border_radius=10
    )

    text(
        SCREEN,
        "YES, EXIT",
        FONT,
        WHITE,
        yes.center,
        True
    )

    text(
        SCREEN,
        "CANCEL",
        FONT,
        WHITE,
        no.center,
        True
    )

    text(
        SCREEN,
        "LEFT / RIGHT + ENTER",
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, 430),
        True
    )


# ============================================================
# HUD
# ============================================================

def draw_hud():

    if mode == "ADVANCED":

        text(
            SCREEN,
            "MODE: TEACHER SPECIAL",
            FONT_SMALL,
            PURPLE,
            (20, 18)
        )

        text(
            SCREEN,
            f"ADVANCED LEVEL: {advanced_level}/20",
            FONT,
            WHITE,
            (20, 43)
        )

        text(
            SCREEN,
            "ADVANCED",
            FONT_SMALL,
            PURPLE,
            (20, 72)
        )

    else:

        text(
            SCREEN,
            "MODE: NORMAL",
            FONT_SMALL,
            GREEN,
            (20, 18)
        )

        text(
            SCREEN,
            f"LEVEL: {level}/30",
            FONT,
            WHITE,
            (20, 43)
        )

        text(
            SCREEN,
            f"STAGE: {stage}",
            FONT,
            CYAN,
            (20, 72)
        )

    text(
        SCREEN,
        f"SCORE: {score}",
        FONT,
        YELLOW,
        (300, 18)
    )

    text(
        SCREEN,
        f"XP: {xp}",
        FONT,
        PURPLE,
        (300, 48)
    )

    text(
        SCREEN,
        f"BULLETS: {bullets}",
        FONT,
        ORANGE,
        (500, 18)
    )

    speed_color = (
        ORANGE
        if speed_multiplier >= 5
        else CYAN
    )

    text(
        SCREEN,
        f"SPEED: {speed_multiplier:g}x",
        FONT_SMALL,
        speed_color,
        (500, 50)
    )

    # HP
    text(
        SCREEN,
        "HP",
        FONT_SMALL,
        WHITE,
        (740, 18)
    )

    pygame.draw.rect(
        SCREEN,
        (50, 50, 60),
        (775, 20, 180, 18),
        border_radius=5
    )

    pygame.draw.rect(
        SCREEN,
        GREEN if hp > 35 else RED,
        (
            775,
            20,
            int(180 * hp / 100),
            18
        ),
        border_radius=5
    )

    # Timer
    timer_color = (
        GREEN
        if time_left > 20
        else RED
    )

    text(
        SCREEN,
        f"TIME: {max(0, int(time_left))}s",
        FONT,
        timer_color,
        (980, 45)
    )


# ============================================================
# QUESTION
# ============================================================

def draw_question():

    if not question:
        return

    panel = pygame.Rect(
        120,
        105,
        900,
        80
    )

    pygame.draw.rect(
        SCREEN,
        PANEL,
        panel,
        border_radius=14
    )

    pygame.draw.rect(
        SCREEN,
        CYAN,
        panel,
        2,
        border_radius=14
    )

    lines = question.split("\n")

    y = (
        panel.centery
        - (len(lines) - 1) * 11
    )

    for line in lines:

        text(
            SCREEN,
            line,
            FONT,
            WHITE,
            (panel.centerx, y),
            True
        )

        y += 24


# ============================================================
# TARGETS
# ============================================================

def draw_targets():

    for t in targets:

        if not t["alive"]:
            continue

        x = int(t["x"])
        y = int(t["y"])
        r = int(t["r"])

        pygame.draw.circle(
            SCREEN,
            (10, 30, 45),
            (x, y),
            r + 5
        )

        pygame.draw.circle(
            SCREEN,
            CYAN,
            (x, y),
            r + 5,
            2
        )

        pygame.draw.circle(
            SCREEN,
            (18, 45, 65),
            (x, y),
            r
        )

        pygame.draw.circle(
            SCREEN,
            (25, 90, 115),
            (x, y),
            r - 10,
            2
        )

        text(
            SCREEN,
            str(t["index"] + 1),
            FONT_MED,
            YELLOW,
            (x, y - 18),
            True
        )

        opt = t["text"]

        if len(opt) > 22:

            opt = opt[:20] + "..."

        text(
            SCREEN,
            opt,
            FONT_SMALL,
            WHITE,
            (x, y + 17),
            True
        )


# ============================================================
# GUN
# ============================================================

def draw_gun():

    mx, my = pygame.mouse.get_pos()

    gx = 1030
    gy = 600

    angle = math.atan2(
        my - gy,
        mx - gx
    )

    length = 105

    bx = (
        gx
        + math.cos(angle) * length
    )

    by = (
        gy
        + math.sin(angle) * length
    )

    pygame.draw.line(
        SCREEN,
        (60, 70, 90),
        (gx, gy),
        (bx, by),
        22
    )

    pygame.draw.line(
        SCREEN,
        CYAN,
        (gx, gy),
        (bx, by),
        8
    )

    barrel_len = 48

    sx = (
        bx
        + math.cos(angle) * barrel_len
    )

    sy = (
        by
        + math.sin(angle) * barrel_len
    )

    pygame.draw.line(
        SCREEN,
        WHITE,
        (bx, by),
        (sx, sy),
        10
    )

    grip_end = (
        gx - 10,
        gy + 55
    )

    pygame.draw.line(
        SCREEN,
        PURPLE,
        (gx, gy),
        grip_end,
        18
    )

    pygame.draw.circle(
        SCREEN,
        CYAN,
        (gx, gy),
        14
    )

    pygame.draw.circle(
        SCREEN,
        WHITE,
        (gx, gy),
        5
    )

    if (
        0 <= mx <= WIDTH
        and 0 <= my <= HEIGHT
    ):

        pygame.draw.circle(
            SCREEN,
            CYAN,
            (mx, my),
            13,
            1
        )

        pygame.draw.line(
            SCREEN,
            CYAN,
            (mx - 20, my),
            (mx + 20, my),
            1
        )

        pygame.draw.line(
            SCREEN,
            CYAN,
            (mx, my - 20),
            (mx, my + 20),
            1
        )


# ============================================================
# PROJECTILES
# ============================================================

def draw_projectiles():

    for p in projectiles:

        x = int(p["x"])
        y = int(p["y"])

        pygame.draw.circle(
            SCREEN,
            WHITE,
            (x, y),
            8
        )

        pygame.draw.circle(
            SCREEN,
            CYAN,
            (x, y),
            15,
            2
        )


# ============================================================
# PARTICLES
# ============================================================

def draw_particles():

    for p in particles:

        pygame.draw.circle(
            SCREEN,
            ORANGE,
            (
                int(p["x"]),
                int(p["y"])
            ),
            max(
                1,
                int(p["r"])
            )
        )


# ============================================================
# BOTTOM BUTTONS
# ============================================================

def draw_bottom_buttons():

    hint = pygame.Rect(
        20,
        660,
        145,
        42
    )

    controls = pygame.Rect(
        175,
        660,
        175,
        42
    )

    exitb = pygame.Rect(
        360,
        660,
        145,
        42
    )

    windowb = pygame.Rect(
        515,
        660,
        180,
        42
    )

    buttons = [

        (
            hint,
            "HINT [CTRL+H]",
            YELLOW
        ),

        (
            controls,
            "CONTROLS [CTRL+C]",
            CYAN
        ),

        (
            exitb,
            "EXIT [CTRL+E]",
            RED
        ),

        (
            windowb,
            "MAX/RESTORE [CTRL+M]",
            GREEN
        )
    ]

    for rect, label, color in buttons:

        pygame.draw.rect(
            SCREEN,
            PANEL,
            rect,
            border_radius=8
        )

        pygame.draw.rect(
            SCREEN,
            color,
            rect,
            2,
            border_radius=8
        )

        text(
            SCREEN,
            label,
            FONT_SMALL,
            color,
            rect.center,
            True
        )

    text(
        SCREEN,
        f"SPEED: {speed_multiplier:g}X",
        FONT_SMALL,
        ORANGE if speed_multiplier >= 5 else WHITE,
        (790, 681),
        True
    )


# ============================================================
# GAME DRAW
# ============================================================

def draw_game():

    draw_background()

    draw_hud()

    draw_question()

    draw_targets()

    draw_projectiles()

    draw_particles()

    draw_gun()

    draw_bottom_buttons()

    if show_hint:

        rect = pygame.Rect(
            780,
            535,
            390,
            80
        )

        pygame.draw.rect(
            SCREEN,
            PANEL,
            rect,
            border_radius=12
        )

        pygame.draw.rect(
            SCREEN,
            YELLOW,
            rect,
            2,
            border_radius=12
        )

        text(
            SCREEN,
            "HINT: Look carefully at the Python rule",
            FONT_SMALL,
            YELLOW,
            rect.center,
            True
        )

    if message_timer > 0:

        text(
            SCREEN,
            message,
            FONT_MED,
            message_color,
            (WIDTH // 2, 620),
            True
        )


# ============================================================
# OUT SCREEN
# ============================================================

def draw_out():

    draw_background()

    text(
        SCREEN,
        "PLAYER OUT",
        FONT_BIG,
        RED,
        (WIDTH // 2, 155),
        True
    )

    text(
        SCREEN,
        "Choose what you want to do",
        FONT,
        WHITE,
        (WIDTH // 2, 215),
        True
    )

    revive_btn = pygame.Rect(
        350,
        275,
        500,
        62
    )

    retry = pygame.Rect(
        350,
        355,
        500,
        62
    )

    menu = pygame.Rect(
        350,
        435,
        500,
        62
    )

    buttons = [

        (
            revive_btn,
            GREEN,
            "REVIVE [CTRL+R]"
        ),

        (
            retry,
            YELLOW,
            "RETRY STAGE"
        ),

        (
            menu,
            CYAN,
            "MAIN MENU"
        )
    ]

    for rect, color, label in buttons:

        pygame.draw.rect(
            SCREEN,
            PANEL,
            rect,
            border_radius=12
        )

        pygame.draw.rect(
            SCREEN,
            color,
            rect,
            2,
            border_radius=12
        )

        text(
            SCREEN,
            label,
            FONT_MED,
            color,
            rect.center,
            True
        )


# ============================================================
# BOSS
# ============================================================

def draw_boss():

    draw_background()

    title = "FINAL PYTHON BOSS"

    if mode == "ADVANCED":

        title = (
            "TEACHER SPECIAL - FINAL BOSS"
        )

    text(
        SCREEN,
        title,
        FONT_TITLE,
        RED,
        (WIDTH // 2, 65),
        True
    )

    # Boss
    bx = WIDTH // 2
    by = 245

    pygame.draw.circle(
        SCREEN,
        (40, 20, 60),
        (bx, by),
        100
    )

    pygame.draw.circle(
        SCREEN,
        PURPLE,
        (bx, by),
        100,
        4
    )

    pygame.draw.circle(
        SCREEN,
        RED,
        (bx - 35, by - 15),
        12
    )

    pygame.draw.circle(
        SCREEN,
        RED,
        (bx + 35, by - 15),
        12
    )

    pygame.draw.arc(
        SCREEN,
        WHITE,
        (
            bx - 45,
            by - 5,
            90,
            65
        ),
        0,
        math.pi,
        4
    )

    # Boss HP
    pygame.draw.rect(
        SCREEN,
        (50, 50, 60),
        (400, 355, 400, 24),
        border_radius=8
    )

    pygame.draw.rect(
        SCREEN,
        RED,
        (
            400,
            355,
            int(400 * boss_hp / 100),
            24
        ),
        border_radius=8
    )

    text(
        SCREEN,
        f"BOSS HP: {boss_hp}",
        FONT,
        WHITE,
        (WIDTH // 2, 395),
        True
    )

    q, opts, ans = BOSS_QUESTIONS[boss_index]

    panel = pygame.Rect(
        120,
        425,
        960,
        80
    )

    pygame.draw.rect(
        SCREEN,
        PANEL,
        panel,
        border_radius=12
    )

    pygame.draw.rect(
        SCREEN,
        RED,
        panel,
        2,
        border_radius=12
    )

    lines = q.split("\n")

    yy = panel.top + 10

    for line in lines[:3]:

        text(
            SCREEN,
            line,
            FONT_SMALL,
            WHITE,
            (panel.centerx, yy),
            True
        )

        yy += 20

    for i, opt in enumerate(opts):

        r = pygame.Rect(
            120 + i * 240,
            525,
            220,
            65
        )

        pygame.draw.rect(
            SCREEN,
            PANEL,
            r,
            border_radius=10
        )

        pygame.draw.rect(
            SCREEN,
            CYAN,
            r,
            2,
            border_radius=10
        )

        text(
            SCREEN,
            f"{i + 1}. {opt}",
            FONT_SMALL,
            WHITE,
            r.center,
            True
        )

    text(
        SCREEN,
        "Shoot the correct answer / press 1-4",
        FONT_SMALL,
        YELLOW,
        (WIDTH // 2, 625),
        True
    )


# ============================================================
# WIN
# ============================================================

def draw_win():

    draw_background()

    text(
        SCREEN,
        "PYTHON STRIKE COMPLETE!",
        FONT_BIG,
        GREEN,
        (WIDTH // 2, 180),
        True
    )

    text(
        SCREEN,
        "CONGRATULATIONS!",
        FONT_TITLE,
        CYAN,
        (WIDTH // 2, 250),
        True
    )

    text(
        SCREEN,
        f"FINAL SCORE: {score}",
        FONT_MED,
        YELLOW,
        (WIDTH // 2, 320),
        True
    )

    text(
        SCREEN,
        f"XP EARNED: {xp}",
        FONT_MED,
        PURPLE,
        (WIDTH // 2, 360),
        True
    )

    text(
        SCREEN,
        "Press ENTER for Main Menu",
        FONT,
        WHITE,
        (WIDTH // 2, 470),
        True
    )


# ============================================================
# INPUT
# ============================================================

def handle_menu_click(pos):

    global mode
    global state
    global show_controls

    x, y = pos

    if 220 <= y <= 278:

        mode = "NORMAL"

        reset_game()

    elif 300 <= y <= 358:

        mode = "ADVANCED"

        reset_game()

    elif 380 <= y <= 438:

        show_controls = True

    elif 460 <= y <= 518:

        pygame.quit()

        sys.exit()


# ============================================================
# GAME CLICK
# ============================================================

def handle_game_click(pos):

    global show_controls
    global show_exit

    if show_exit:

        yes = pygame.Rect(
            410,
            350,
            160,
            55
        )

        no = pygame.Rect(
            630,
            350,
            160,
            55
        )

        if yes.collidepoint(pos):

            pygame.quit()

            sys.exit()

        if no.collidepoint(pos):

            show_exit = False

        return

    if show_controls:

        show_controls = False

        return

    if pygame.Rect(
        20,
        660,
        150,
        42
    ).collidepoint(pos):

        use_hint()

        return

    if pygame.Rect(
        175,
        660,
        175,
        42
    ).collidepoint(pos):

        show_controls = True

        return

    if pygame.Rect(
        360,
        660,
        145,
        42
    ).collidepoint(pos):

        show_exit = True

        return

    if pygame.Rect(
        515,
        660,
        180,
        42
    ).collidepoint(pos):

        toggle_window_size()

        return

    if state == "PLAYING":

        shoot_toward(*pos)


# ============================================================
# BOSS CLICK
# ============================================================

def handle_boss_click(pos):

    if 525 <= pos[1] <= 590:

        for i in range(4):

            r = pygame.Rect(
                120 + i * 240,
                525,
                220,
                65
            )

            if r.collidepoint(pos):

                boss_answer(i)

                return


# ============================================================
# OUT CLICK
# ============================================================

def handle_out_click(pos):

    global state

    revive_btn = pygame.Rect(
        350,
        275,
        500,
        62
    )

    retry = pygame.Rect(
        350,
        355,
        500,
        62
    )

    menu = pygame.Rect(
        350,
        435,
        500,
        62
    )

    if revive_btn.collidepoint(pos):

        revive()

    elif retry.collidepoint(pos):

        reset_to_stage_start()

    elif menu.collidepoint(pos):

        state = "MENU"


# ============================================================
# MAIN LOOP
# ============================================================

running = True

while running:

    dt = CLOCK.tick(60) / 1000.0

    dt = min(
        dt,
        0.05
    )

    if message_timer > 0:

        message_timer -= dt

    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # ====================================================
        # KEYBOARD
        # ====================================================

        elif event.type == pygame.KEYDOWN:

            # -----------------------------------------------
            # F11 FULLSCREEN
            # -----------------------------------------------

            if event.key == pygame.K_F11:

                fullscreen = not fullscreen

                if fullscreen:

                    SCREEN = pygame.display.set_mode(
                        (WIDTH, HEIGHT),
                        pygame.FULLSCREEN | pygame.SCALED
                    )

                else:

                    SCREEN = pygame.display.set_mode(
                        (WIDTH, HEIGHT),
                        pygame.RESIZABLE | pygame.SCALED
                    )

                continue

            # -----------------------------------------------
            # ESC FULLSCREEN
            # -----------------------------------------------

            if (
                event.key == pygame.K_ESCAPE
                and fullscreen
                and not show_exit
                and not show_controls
            ):

                fullscreen = False

                SCREEN = pygame.display.set_mode(
                    (WIDTH, HEIGHT),
                    pygame.RESIZABLE | pygame.SCALED
                )

                continue

            # -----------------------------------------------
            # CTRL + S SPEED
            # -----------------------------------------------

            if (
                event.key == pygame.K_s
                and pygame.key.get_mods()
                & pygame.KMOD_CTRL
            ):

                cycle_speed()

                continue

            # -----------------------------------------------
            # CTRL + M WINDOW
            # -----------------------------------------------

            if (
                event.key == pygame.K_m
                and pygame.key.get_mods()
                & pygame.KMOD_CTRL
            ):

                toggle_window_size()

                continue

            # -----------------------------------------------
            # CTRL + R REVIVE
            # -----------------------------------------------

            if (
                event.key == pygame.K_r
                and pygame.key.get_mods()
                & pygame.KMOD_CTRL
            ):

                if state == "OUT":

                    revive()

                else:

                    set_message(
                        "REVIVE IS AVAILABLE WHEN PLAYER IS OUT",
                        YELLOW,
                        1.2
                    )

                continue

            # -----------------------------------------------
            # EXIT POPUP
            # -----------------------------------------------

            if show_exit:

                if event.key in (
                    pygame.K_LEFT,
                    pygame.K_RIGHT
                ):

                    exit_choice = (
                        1 - exit_choice
                    )

                elif event.key == pygame.K_RETURN:

                    if exit_choice == 0:

                        pygame.quit()

                        sys.exit()

                    else:

                        show_exit = False

                elif event.key == pygame.K_ESCAPE:

                    show_exit = False

                continue

            # -----------------------------------------------
            # CONTROLS POPUP
            # -----------------------------------------------

            if show_controls:

                show_controls = False

                continue

            # -----------------------------------------------
            # CTRL + C
            # -----------------------------------------------

            if (
                event.key == pygame.K_c
                and pygame.key.get_mods()
                & pygame.KMOD_CTRL
            ):

                show_controls = True

                continue

            # -----------------------------------------------
            # CTRL + H
            # -----------------------------------------------

            if (
                event.key == pygame.K_h
                and pygame.key.get_mods()
                & pygame.KMOD_CTRL
            ):

                use_hint()

                continue

            # -----------------------------------------------
            # CTRL + E
            # -----------------------------------------------

            if (
                event.key == pygame.K_e
                and pygame.key.get_mods()
                & pygame.KMOD_CTRL
            ):

                show_exit = True

                exit_choice = 1

                continue

            # =================================================
            # MENU
            # =================================================

            if state == "MENU":

                if event.key == pygame.K_ESCAPE:

                    running = False

            # =================================================
            # PLAYING
            # =================================================

            elif state == "PLAYING":

                if event.key in (
                    pygame.K_1,
                    pygame.K_2,
                    pygame.K_3,
                    pygame.K_4
                ):

                    idx = (
                        event.key
                        - pygame.K_1
                    )

                    if (
                        idx < len(targets)
                        and targets[idx]["alive"]
                    ):

                        shoot_toward(
                            targets[idx]["x"],
                            targets[idx]["y"]
                        )

                elif event.key == pygame.K_ESCAPE:

                    state = "MENU"

            # =================================================
            # OUT
            # =================================================

            elif state == "OUT":

                if event.key == pygame.K_RETURN:

                    reset_to_stage_start()

                elif event.key == pygame.K_m:

                    state = "MENU"

            # =================================================
            # BOSS
            # =================================================

            elif state == "BOSS":

                if event.key in (
                    pygame.K_1,
                    pygame.K_2,
                    pygame.K_3,
                    pygame.K_4
                ):

                    boss_answer(
                        event.key
                        - pygame.K_1
                    )

                elif event.key == pygame.K_ESCAPE:

                    state = "MENU"

            # =================================================
            # WIN
            # =================================================

            elif state == "WIN":

                if event.key == pygame.K_RETURN:

                    state = "MENU"

        # ====================================================
        # MOUSE
        # ====================================================

        elif (
            event.type
            == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):

            if state == "MENU":

                handle_menu_click(
                    event.pos
                )

            elif state == "PLAYING":

                handle_game_click(
                    event.pos
                )

            elif state == "OUT":

                handle_out_click(
                    event.pos
                )

            elif state == "BOSS":

                handle_boss_click(
                    event.pos
                )

    # ========================================================
    # UPDATE
    # ========================================================

    if state == "PLAYING":

        time_left -= dt

        if time_left <= 0:

            time_left = 0

            player_out(
                "TIME OUT!"
            )

        else:

            update_targets(dt)

            update_projectiles(dt)

    update_particles(dt)

    # ========================================================
    # DRAW
    # ========================================================

    if state == "MENU":

        draw_menu()

        if show_controls:

            draw_controls()

    elif state == "PLAYING":

        draw_game()

        if show_controls:

            draw_controls()

        if show_exit:

            draw_exit_popup()

    elif state == "OUT":

        draw_out()

    elif state == "BOSS":

        draw_boss()

    elif state == "WIN":

        draw_win()

    pygame.display.flip()


# ============================================================
# EXIT
# ============================================================

pygame.quit()