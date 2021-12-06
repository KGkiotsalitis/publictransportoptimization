### ALGORITHM
::: sourcecode.chapter3.3_3_1 Newton Raphson Method

### EXAMPLE

``` python linenums="1"
def f(x):
    return(x**2-x-1)
def f_der(x):
    return(2*x-1)
print(newton_raphson(f,f_der,10,1e-6))
```

### OUTCOME

``` python 
r=1.6180339887500548
```