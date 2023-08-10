#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * insert_node - inserts a number node in sorted ascending order
 * @head: pointer to linked list head
 * @number: number to insert
 *
 * Return: address of the new node on success
 * NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL, *nextnode = NULL, *nodep = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	nodep = *head;
	if (nodep == NULL)
	{
		*head = newnode;
		newnode->next = NULL;
	}
	else if (nodep->n > number)
	{
		newnode->next = nodep;
		*head = newnode;
	}
	else
	{
		while (nodep)
		{
			nextnode = nodep->next;
			if (nextnode != NULL && nextnode->n > number)
			{
				nodep->next = newnode;
				newnode->next = nextnode;
				break;
			}
			else if (nextnode == NULL)
			{
				nodep->next = newnode;
				newnode->next = NULL;
				break;
			}
			nodep = nodep->next;
		}
	}

	return (newnode);
}
