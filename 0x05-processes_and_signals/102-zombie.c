#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - An infinite loop
 *
 * Return: Alrays 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - PID
 *
 * Return: Alrays 0.
 */
int main(void)
{
	int pids, i;

	for (i = 4; i >= 0; --i)
	{
		pid = fork();
		if (pids != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			return (0);
	}
	infinite_while();
	return (0);
}
