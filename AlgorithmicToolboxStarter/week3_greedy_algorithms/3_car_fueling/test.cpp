#include <stdio.h>
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    if (a > b)
    {
        int temp = a + b;
        if (temp < 0)
        {
            if (temp * temp < 0)
                printf("PATH1.1");
            else
                printf("PATH1.2");
        }
        else if (temp == 0)
        {
            temp = -999;
            printf("PATH1.3");
        }

        if (temp > 0)
            printf("PATH1.4");
    }
    else
    {
        if (a != b)
            printf("PATH2.1");
        else if (a < b)
            printf("PATH2.2");
        else
            printf("PATH2.3");
    }
    return 0;
}
