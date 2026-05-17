#include "Cracker.h"

void dict_attack(FILE *wordList, char *hashedPassword, char *hash_type)
{
    time_t startTime = time(NULL);

    int attempts = 0;

    char **words = readWordList(&wordList);
}

char **readWordList(FILE *wordList)
{
    size_t capacity = 256;
    char **words = malloc(capacity * sizeof(char *));
    char buffer[256];

    if (words == NULL)
    {
        printf("Malloc Failed\n");
        return NULL;
    }

    size_t count = 0;
    while (fgets(buffer, sizeof(buffer), wordList) != NULL)
    {
        buffer[strcspn(buffer, "\n")] = '\0';

        if (count + 1 >= capacity)
        {
            capacity *= 2;
            char **temp = realloc(words, capacity * sizeof(char *));
            if (temp == NULL)
            {
                printf("Realloc Failed\n");
                for (size_t i = 0; i < count; i++)
                {
                    free(words[i]);
                }
                free(words);
                return NULL;
            }
            words = temp;
        }

        words[count] = malloc(strlen(buffer) + 1);
        if (words[count] == NULL)
        {
            printf("Malloc Failed\n");
            for (size_t i = 0; i < count; i++)
            {
                free(words[i]);
            }
            free(words);
            return NULL;
        }

        strcpy(words[count], buffer);
        count++;
    }

    words[count] = NULL;
    return words;
}
