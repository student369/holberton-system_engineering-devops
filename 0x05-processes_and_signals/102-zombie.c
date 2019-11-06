#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

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
	pid_t pids[5];
	int i;

	for (i = 4; i >= 0; --i)
	{
		pids[i] = fork();
		if (pids[i] == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			infinite_while();
			_exit(0);
		}
	}
	for (i = 4; i >= 0; --i)
		waitpid(pids[i], NULL, 0);
	return (0);
}
