#include <stdio.h>

__declspec(dllexport) void say_hello() {
    printf("Hello from C!\n");
}
