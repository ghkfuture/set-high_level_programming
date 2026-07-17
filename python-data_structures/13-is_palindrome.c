#include "lists.h"
#include <stddef.h>

/**
 * sc_p - checks recursive symmetry
 * @left: address of head pointer
 * @right: right side moving pointer
 * Return: 1 if symmetric match, 0 otherwise
 */
int sc_p(listint_t **left, listint_t *right)
{
int res;

if (right == NULL)
return (1);

res = sc_p(left, right->next) && ((*left)->n == right->n);
*left = (*left)->next;
return (res);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head pointer double reference
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (1);
return (sc_p(head, *head));
}
