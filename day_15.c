#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// gcc -shared -o day_15.so -fPIC day_15.c

int *memory;
int memory_len;

int *current_play;
int current_turn;
int next_play;

void init_memory_game(int *_memory, int _memory_len, int _starting_turn)
{
    memory = _memory;
    memory_len = _memory_len; // Unused, but good pratice?
    current_turn = _starting_turn + 1;
    next_play = 0;
}

int play_memory_game(int to_turn)
{
    for (; current_turn < to_turn; current_turn++)
    {
        current_play = (memory + next_play);

        if (*current_play != 0)
        {
            next_play = current_turn - *current_play;
        }
        else
        {
            next_play = 0;
        }

        *current_play = current_turn;
    }

    return next_play;
}
