#include <stdio.h>
#include <getopt.h>
#include <unistd.h>

int main(int argc, char **argv)
{

    int opt;
    char *hash;
    char *hash_type;
    char *filepath;

    while ((opt = getopt(argc, argv, "h:t:w:")) != -1)
    {
        switch (opt)
        {
        case 'h':
            hash = optarg;
            break;

        case 't':
            hash_type = optarg;
            break;

        case 'w':
            filepath = optarg;
            break;
        }
    }
}