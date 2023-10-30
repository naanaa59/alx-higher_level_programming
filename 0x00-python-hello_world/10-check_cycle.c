#include "lists.h"

/**
 * check_cycle - check if there is a cycle in the list
 *
 * @list: the list to check
 *
 * Return: 0 if there is no cycle or 1 if there is a cycle
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
		return (0);
	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
