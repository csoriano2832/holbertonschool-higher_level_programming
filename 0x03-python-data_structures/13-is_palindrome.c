#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to first element in list
 *
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = NULL, *slow = NULL, *firstHalf = NULL, *secondHalf = NULL;

	if (head == NULL)
		return (1);

	fast = *head;
	slow = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	firstHalf = *head;
	secondHalf = reverse(slow->next);

	while (firstHalf != NULL && secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
			return (0);

		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}

/**
 * reverse - creates a new head to traverse the list in reverse
 * @head: the element in the middle of the list
 *
 * Return: the new head
 */
listint_t *reverse(listint_t *head)
{
	listint_t *newHead = NULL;
	listint_t *tmp = NULL;

	while (head != NULL)
	{
		tmp = head->next;
		head->next = newHead;
		newHead = head;
		head = tmp;
	}
	return (newHead);
}
