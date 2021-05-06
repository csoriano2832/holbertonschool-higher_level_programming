#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: a list object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	size_t size = PyList_Size(p);
	size_t idx;
	PyObject *item;

	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);

	if (size > 0)
	{
		for (idx = 0; idx < size; idx++)
		{
			item = PyList_GetItem(p, idx);
			printf("Element %zu: %s\n", idx, Py_TYPE(item)->tp_name);
		}
	}
}
