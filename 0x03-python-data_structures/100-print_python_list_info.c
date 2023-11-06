#include <stdio.h>
#include <Python.h>


void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * @p: pointer to the pyobject which is the list
 *
 */
void print_python_list_info(PyObject *p)
{
	int size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}

}
