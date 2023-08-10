#include "lists.h"

/**
 * check_cycle - checks if the linked list has a cycle
 * @list: pointer to a linked list
 *
 * Return: 1 if it has a cycle
 * 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *nodep;

	nodep = list;
	while (nodep)
	{
		if (nodep <= nodep->next)
			return (1);
		nodep = nodep->next;
	}
	return (0);
}
