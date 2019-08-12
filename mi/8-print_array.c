#include <stdio.h>
void print_array(int *a, int n);
void print_array(int *a, int n)
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		if (i == (n - 1))
		{
			printf("%d", a[i]);
		}
		else
		{
			printf("%d,  ", a[i]);
		}
	}
	printf("\n");
}
int main(void)
{
	int arr[] = {1, 2, 3};
	print_array(arr, 3);
	return (0);
}
