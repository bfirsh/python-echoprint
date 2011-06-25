#include <Codegen.h>
#include <Python.h>
#include <stdio.h>

static PyObject * echoprint_codegen(PyObject *self, PyObject *args) {
    PyObject *py_samples;
    int start_offset = 0;
    PyObject *item;
    float *samples;
    uint num_samples;
    uint i;
    Codegen *pCodegen;
    PyObject *result;
    std::ostringstream version_string;
    
    if (!PyArg_ParseTuple(args, "O|i", &py_samples, &start_offset)) {
        return NULL;
    }
    if (!PySequence_Check(py_samples)) {
        PyErr_SetString(PyExc_TypeError, "expected sequence");
        return NULL;
    }
    num_samples = PySequence_Size(py_samples);
    samples = new float[num_samples];
    for (i = 0; i < num_samples; i++) {
        item = PySequence_GetItem(py_samples, i);
        if (!PyFloat_Check(item)) {
            delete[] samples;
            PyErr_SetString(PyExc_TypeError, "expected sequence of floats");
            return NULL;
        }
        samples[i] = (float)PyFloat_AsDouble(item);
        Py_DECREF(item);
    }
    pCodegen = new Codegen(samples, num_samples, start_offset);
    version_string << pCodegen->getVersion();
    result = Py_BuildValue("{s:s,s:s}",
        "code", pCodegen->getCodeString().c_str(),
        "version", version_string.str().c_str()
    );
    delete pCodegen;
    delete[] samples;
    return result;
}

static PyMethodDef echoprint_methods[] = {
    {"codegen", echoprint_codegen, METH_VARARGS,
     "Generates a echoprint code for a list of floating point PCM data sampled at 11025 Hz and mono. Optionally takes a second integer argument to hint the server on where the sample is taken from in the original file if known."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initechoprint(void)
{
    (void) Py_InitModule("echoprint", echoprint_methods);
}


