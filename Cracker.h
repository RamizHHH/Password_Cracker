#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <string.h>

void dict_attack(FILE *wordList, char *hashedPassword, char *hash_type);
char **readWordList(FILE *wordList);
