#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: the head pointer to the list
 *
 * Return: 0 it is not a palindrome and 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *rev_list, *head2;
	int count = 0, i;

	if (*head == NULL)
		return (0);
	current = *head;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	head2 = rev_half(head, count);
	rev_list = head2;
	current = *head;
	for (i = 0; i < count / 2; i++)
	{
		if (current->n != rev_list->n)
		{
			free_listint(head2);
			return (0);
		}
		current = current->next;
		rev_list = rev_list->next;
	}
	free_listint(head2);
	return (1);
}
/**
 * add_to_beginning - add a node to beginning of a list
 *
 * @head: head of the list
 *
 * @n: the data to add
 *
 * Return: returns the list
 *
 */
listint_t *add_to_beginning(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
 * rev_half - adds to a list a half of another reversed
 *
 * @head: head of the list
 *
 * Return the list
 */
listint_t *rev_half(listint_t **head, int length)
{
	listint_t *current_list;
	listint_t *reversed_list = NULL;
	int i;

	current_list = *head;
	for (i = 0; i < (length / 2); i++)
		current_list = current_list->next;

	while (current_list != NULL)
	{
		add_to_beginning(&reversed_list, current_list->n);
		current_list = current_list->next;
	}
	return (reversed_list);


}
















