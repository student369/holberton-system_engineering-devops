#include <stdio.h>
struct word
{
	char c;
	struct word *next;
}
int _is_palin(struct list *h);
int _is_palin(struct list *h)
{
	int i = 0;
	struct word *tmp, *tmp2;
	tmp = h;
	while (tmp->next != NULL)
	{
		i++;
	}
	tmp = h;
	while (tmp->next != NULL)
	{
		i++;
	}
	char copy[i];
	return (i);
}
int main(void)
{
	char c1 = "e";
	char c2 = "y";
	char c3 = "e";

	struct head = (struct word*)malloc(sizeof(word));
	struct mid = (struct word*)malloc(sizeof(word));
	struct end = (struct word*)malloc(sizeof(word));

	head->c = c1;
	mid->c = c2;
	end->c = c3;
	head->next = mid;
	mid->next = end;
	end->next = NULL;
	if (_is_palin(&head))
	{
		printf("Is palindrom\n");
	}
	else
	{
		printf("Is not palindrom\n");
	}
	return (0);
}
