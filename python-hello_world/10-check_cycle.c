#include "lists.h"

/**
 * check_cycle - Evaluates if a singly linked list architecture contains cycles
 * @list: Target head pointer reference node
 * Return: 0 if linear configuration sequence, 1 if loop/cycle detected
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1);
}

return (0);
}
