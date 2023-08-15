#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a list has a palindrome
 * @head: the header of the list
 *
 * Return: 1 if palindrome
 * 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *nextnode, *prevnode, *nodep = NULL;
	int dif = 0,  n = 0, i = 1, status = 0, mirror = 0;

	nodep = *head;
	while (nodep && (nextnode = nodep->next))
	{
		n++;
		dif = nextnode - nodep;
		if (nodep->n == nextnode->n)
		{
			if (n == 1 && nextnode->next == NULL)
				status = 1;
			else if (n == 1 && nextnode->next)
				status = 0;
			else
				mirror = 1;
			break;
		}
		nodep = nextnode;
	}
	if (mirror)
	{
		nextnode = nextnode->next;
		prevnode = nodep - dif;
		while (nextnode && nextnode->n == prevnode->n)
		{
			i++;
			if (i == n && nextnode->next == NULL)
				return (1);
			else if (i == n && nextnode->next)
				return (0);
			nextnode = nextnode->next;
			prevnode = prevnode - dif;
		}
	}
	printf("nodep address after loop block: %p\n", (void *)nodep);
	printf("previous node->n: %d address: %p\n", prevnode->n, (void *)prevnode);

	return (status);
}
