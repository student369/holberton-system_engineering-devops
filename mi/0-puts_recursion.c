#include <stdio.h>
#include <unistd.h>
void _puts_recursion(char *s);
int _putchar(char c);
/**
 * _putchar - writes the character c to stdout
 * @c: The character to print
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int _putchar(char c)
{
	return (write(1, &c, 1));
}
void _puts_recursion(char *s)
{
	if (*s == '\0')
	{
		_putchar('\n');
		return;
	}
	_putchar(*s);
	_puts_recursion(s + 1);
}
int main(void)
{
	_puts_recursion("Betty Holberton");
	return (0);
}
