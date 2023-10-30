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
	listint_t *head = list->next;

	if (head->next == NULL)
		return (0);
	fast = head->next;
	slow = head;
	while (fast != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
