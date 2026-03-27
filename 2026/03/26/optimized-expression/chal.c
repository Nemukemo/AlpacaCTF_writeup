#include<stdio.h>
#include<stdint.h>
#include<string.h>

#define TABLE_SIZE 34
const uint8_t table[TABLE_SIZE][2] = {
    {13, 2},
    {21, 3},
    {22, 0},
    {19, 6},
    {19, 1},
    {19, 6},
    {24, 4},
    {13, 5},
    {21, 0},
    {23, 6},
    {21, 0},
    {23, 3},
    {21, 0},
    {22, 6},
    {22, 5},
    {19, 4},
    {19, 0},
    {24, 2},
    {19, 4},
    {15, 0},
    {23, 5},
    {21, 3},
    {23, 4},
    {21, 0},
    {22, 0},
    {21, 3},
    {21, 0},
    {19, 1},
    {19, 6},
    {23, 4},
    {21, 0},
    {22, 6},
    {22, 5},
    {25, 6},
};

int is_correct(const char *buf)
{
    if (strlen(buf) != TABLE_SIZE)
    {
        return 1;
    }

    for (int i = 0; i < TABLE_SIZE; ++i)
    {
        uint64_t x = (uint8_t)buf[i];
        uint64_t y = (x * 3435973837) >> 34;
        uint64_t t = (x * 613566757) >> 32;
        uint64_t z = x - ((((x - t) >> 1) + t) >> 2) * 7;

        if (y != table[i][0] || z != table[i][1])
        {
            return 1;
        }
    }

    return 0;
}

int main()
{
    char buf[TABLE_SIZE + 1];
    scanf("%s", buf);

    if (!is_correct(buf))
    {
        printf("Correct! The flag is %s\n", buf);
        return 0;
    }
    else
    {
        printf("Incorrect...\n");
        return 1;
    }
}
