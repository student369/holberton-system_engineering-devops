#include <stdio.h>
char *last_first(char *s);
char *last_first(char *s)
{
	int i = 0;
	char first, last, lastone, lastone2;

	while (s[i] != '\0')
	{
		if (i == 0)
			first = s[i];
		i++;
	}
	char s2[i];
	i = 0;
	while (s[i] != '\0')
	{
		s2[i] = s[i];
		i++;
	}
	s2[i] = '\0';
	last = s[i - 1];
	i = 0;
	while (s[i] != '\0')
	{
		if (i == 0)
		{
			lastone = s[i];
			s[i] = last;
		}
		else
			s[i] = s2[i - 1];
		i++;
	}
	return s;
}
int main(void)
{
	char arr[] = "Holberton";
	printf("%s\n", last_first(arr));
	return (0);
}
