import ctypes
day_lib = ctypes.CDLL("./day_15_so.so")


_start_game = day_lib.init_memory_game
_start_game.argtypes = None  # [ctypes.POINTER(ctypes.c_int * 0), ctypes.c_int, ctypes.c_int]
_start_game.restype = None


_play_to_turn = day_lib.play_memory_game
_play_to_turn.argtypes = [ctypes.c_int]
_play_to_turn.restype = ctypes.c_int

_memory = None


def start_game(starting_memory: list, starting_turn: int, memory_size: int):

    _memory = (ctypes.c_int * memory_size)(*starting_memory)
    memory_ptr = ctypes.cast(_memory, ctypes.POINTER(ctypes.c_int * memory_size))

    _start_game.argtypes = [ctypes.POINTER(ctypes.c_int * memory_size), ctypes.c_int, ctypes.c_int]
    _start_game(memory_ptr, ctypes.c_int(memory_size), ctypes.c_int(starting_turn))


def play_to_turn(run_to_turn: int) -> int:
    return _play_to_turn(ctypes.c_int(run_to_turn))
