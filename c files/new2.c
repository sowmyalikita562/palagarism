#include <stdio.h>
 
void main()
{
    long num1, temp1, digit1, sum1 = 0;
 
    printf("Enter the number \n");
    scanf("%ld", &num1);
    temp = num1;
    while (num1 > 0)
    {
        digit1 = num1 % 10;
        sum1  = sum1 + digit1;
        num1 /= 10;
    }
    printf("Given number = %ld\n", temp);
    printf("Sum of the digits %ld = %ld\n", temp, sum1);
}