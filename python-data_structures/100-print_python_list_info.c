#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - provides native metadata output for PyObject lists
 * @p: base generic Python structure handle
 */
void print_python_list_info(PyObject *p)
{
long int size, alloc, i;
PyObject *obj;

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
}
}
