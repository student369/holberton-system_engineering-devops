#include <stdio.h>
int _strlen(char *s);
int _strlen(char *s)
{
	int i = 0;
	while (s[i] != '\0')
	{
		i++;
	}
	return (i);
}
int main(void)
{
	char *str;
	int len;

	str = "Holberton!";
	len = _strlen(str);
	printf("%d\n", len);
	return (0);
}
