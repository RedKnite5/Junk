#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>



double _v(double m1, double m2, double hue) {
	hue = fmod(hue+1.0, 1.0);
	if (hue < 1.0/6.0) {
		return m1 + (m2 - m1) * hue * 6.0;
	}
	if (hue < 0.5) {
		return m2;
	}
	if (hue < 2.0/3.0) {
		return m1 + (m2-m1) * (2.0/3.0 - hue) * 6.0;
	}
	return m1;
}


static PyObject *method_hls_to_rgb(PyObject *self, PyObject *args) {
	double h, l, s = 0.0;
	
	if (!PyArg_ParseTuple(args, "ddd", &h, &l, &s)) {
		return NULL;
	}
	
	if (s == 0.0) {
		return Py_BuildValue("ddd", l, l, l);
	}
	double m2;
	if (l <= .5) {
		m2 = l * (1.0 + s);
	} else {
		m2 = l + s - (l * s);
	}
	double m1 = 2.0 * l - m2;
	
	return Py_BuildValue("ddd", _v(m1, m2, h + 1.0/3.0), _v(m1, m2, h), _v(m1, m2, h - 1.0/3.0));
}

/*
def point(A, B, size, zoom, loc[0], loc[1], iter):
	z = 0
	# convert canvas coordinates to mandelbrot numbers 
	a = (((A/(100*size))-2)/zoom)+loc[0]
	b = (((B/(100*size))-2)/zoom)+loc[1]
	for k in range(iter):
		if c.polar(z)[0] > 2:
			return k
		z = z*z + (a+b*1j)
	return iter
*/

static PyObject *method_point(PyObject *self, PyObject *args) {
	
	int A, B, iter = 0;
	double size, zoom, x, y = 0.0;
	
	if (!PyArg_ParseTuple(args, "iiddddi", &A, &B, &size, &zoom, &x, &y, &iter)) {
		return NULL;
	}
	
	double zr, zi, old_zr = 0.0;
	/* convert canvas coordinates to mandelbrot numbers */
	double a = (((double)A) / (100.0 * size) - 2.0) / zoom + x;
	double b = (((double)B) / (100.0 * size) - 2.0) / zoom + y;
	
	for (int i=0; i<iter; i++) {
		if (sqrt(zr * zr + zi * zi) > 2.0) {
			return PyLong_FromLong(i);
		}
		old_zr = zr;
		zr = zr * zr + a - zi * zi;
		zi = 2 * old_zr * zi + b;
	}
	return PyLong_FromLong(iter);
}


static PyObject *method_html_color(PyObject *self, PyObject *args) {
	double red, green, blue;
	
	if (!PyArg_ParseTuple(args, "ddd", &red, &green, &blue)) {
		return NULL;
	}
	
	char color[7];
	snprintf(color, sizeof(color), "%02x%02x%02x", (int) (red + .5), (int) (green + .5), (int) (blue + .5));
	
	return Py_BuildValue("s", color);
}


static PyMethodDef MandelbrotMethods[] = {
    {"hls_to_rgb", method_hls_to_rgb, METH_VARARGS, "Convert from the hls colorspace to the rgb colorspace. Done in C"},
	{"point", method_point, METH_VARARGS, "Get the hue of a point int the mandelbrot set from canvas coordinates"},
	{"html_color", method_html_color, METH_VARARGS, "Convert 8-bit rgb values to a hexstring"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef mandelbrotmodule = {
    PyModuleDef_HEAD_INIT,
    "mandelbrot",
    "Code for calculating the mandelbrot set quickly",
    -1,
    MandelbrotMethods
};



PyMODINIT_FUNC PyInit_mandelbrot_lib(void) {
    return PyModule_Create(&mandelbrotmodule);
}










