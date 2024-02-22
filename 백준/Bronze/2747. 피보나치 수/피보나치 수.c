#include <stdio.h>

int fibo(int num) {
    if (num == 0)
        return 0;
    if (num == 1)
        return 1;

    int a = 0, b = 1;
    for (int i = 2; i <= num; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    int num;
    scanf("%d", &num);
    printf("%d", fibo(num));
    return 0;
}