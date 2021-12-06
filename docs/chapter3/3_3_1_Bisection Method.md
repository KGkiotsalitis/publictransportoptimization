### ALGORITHM
::: sourcecode.chapter3.3_3_1 Bisection Method

### EXAMPLE 1

``` python linenums="1"
def f(x):
    return(x**2-1)

print(bisection(f,0,3,1e-12))
```

### OUTCOME

``` python 
c=1.0000000000004547
```

### EXAMPLE 2

``` python linenums="1"
def f(x):
    return(x**2-x-1)

print(bisection(f,0,10,1e-6))
```

### OUTCOME

``` python 
c=1.6180336475372314
```