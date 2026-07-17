#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints info about a Python bytes object
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
ssize_t size, i, limit;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
str = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

limit = (size >= 10) ? 10 : size + 1;
printf("  first %ld bytes:", limit);
for (i = 0; i < limit; i++)
printf(" %02x", (unsigned char)str[i]);
printf("\n");
}

/**
 * print_python_list - Prints info about a Python list object
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
ssize_t size, alloc, i;
PyObject *obj;

printf("[*] Python list info\n");
if (!PyList_Check(p))
return;

size = ((PyVarObject *)p)->ob_size;
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
obj = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", i, obj->ob_type->tp_name);
if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}
