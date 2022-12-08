#include <stdio.h>
#include <stdlib.h>

/**
 * add_dnodeint_end - a function that adds a new node at the end of a list
 * @head: the node whose previous is NULL
 * @n: address of the new element
 *
 * return: address of the new element or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{

	if (list == NULL)
	{
		printf("The list is empty\n");
		return;
	}
	dlistint_t *current = list;

	while (current != NULL)
	{
		printf("%d\n", current = list);
		current = current->next;
	}
}
