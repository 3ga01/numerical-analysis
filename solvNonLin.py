import numpy as np
import matplotlib.pyplot as plt


choice = input("Choose a method:\n(1) Bisection\n(2) Fixed-Point\n(3) Newton-Raphson\n")

if choice == '1':
    functionExpression = input("Enter the function: ")
    func = lambda x: eval(functionExpression)

    x00 = float(input("Enter the first starting point x0: "))
    x11 = float(input("Enter the second starting point x1: "))
    relApproxError = float(input("Enter the convergence criterion for the relative approximate error: "))
    funcValue = float(input("How close should f(x) be to zero to stop: "))
    maxIterations = int(input("Maximum number of iterations: "))

    x0 = x00
    x1 = x11
    x2_prev = 0
    iteration = 0

    xValues = []
    yValues = []
    errorVal = []
    iterationVal = []

    while iteration < maxIterations:
        iteration = iteration + 1

        x2 = (x0 + x1) / 2
        b = func(x0) * func(x2)
        if func(x0) * func(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        a = abs((x2 - x2_prev) / x2)
        if abs((x2 - x2_prev) / x2) < relApproxError:
            Root = x2
            flag = 1
            print('flag 1: relative approximate error encountered')
            print('Root:', Root)
            break

        if abs(func(x2)) < funcValue:
            Root = x2
            flag = 2
            print('flag 2: convergence criterion for the function value encountered')
            print('Root:', Root)
            break

        x2_prev = x2

        xValues = np.linspace(x00, x11, iteration)
        yValues = np.zeros_like(xValues)

        for i in range(iteration):
            yValues[i] = func(xValues[i])

        w = iteration
        errorVal.append(a)
        iterationVal.append(iteration)

    if iteration == maxIterations:
        flag = 3
        print('flag 3: Max iterations exceeded')

    plt.figure()
    plt.plot(xValues, yValues)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of f(x) vs x')
    plt.grid(True)

    x_highlight = x2
    f_highlight = func(x2)
    highlight = [x_highlight, f_highlight]

    plt.plot(x_highlight, f_highlight, 'ro', markersize=10)
    plt.text(x_highlight, f_highlight, f'({x_highlight}, {f_highlight})', verticalalignment='bottom')
    plt.show()

    plt.figure()
    plt.plot(iterationVal, errorVal)
    plt.xlabel('iteration number')
    plt.ylabel('approximate relative')
    plt.title('Plot of approximate relative Vs iteration Number')
    plt.grid(True)
    plt.show()


elif choice == '3':
    functionExpression = input("Enter the function: ")
    func = lambda x: eval(functionExpression)

    df_expression = input("Enter the derivative of f(x): ")
    df = lambda x: eval(df_expression)

    x0 = float(input("Enter the starting point: "))
    epsilon1 = float(input("Enter the convergence criterion for relative approximate errors: "))
    epsilon2 = float(input("Enter the convergence criterion for the function value: "))
    maxIterations = int(input("Enter the maximum number of iterations: "))

    # Rest of the code for Newton-Raphson method

    # Initialize variables
    flag = 0
    iteration = 0
    x_old = x0
    error = 1

    errorVal = []
    iterationVal = []

    # Newton-Raphson iteration
    while error > epsilon1 and abs(func(x_old)) > epsilon2 and iteration < maxIterations:
        x_new = x_old - func(x_old) / df(x_old)
        error = abs((x_new - x_old) / x_new)
        x_old = x_new
        iteration = iteration + 1

        w = iteration
        errorVal.append(error)
        iterationVal.append(iteration)

        if error < epsilon1:
            flag = 1  # Relative approximate error convergence criterion met
            break
        elif abs(func(x_new)) < epsilon2:
            flag = 2  # Function value convergence criterion met
            break

    if iteration == maxIterations:
        flag = 3
        print('flag 3: Max iterations exceeded')

    print('Root: {:.6f}'.format(x_new))
    if flag == 1:
        print('Stopping Criteria Flag: flag 1: relative approximate error encountered')
    elif flag == 2:
        print('Stopping Criteria Flag: flag 2: convergence criterion for the function value encountered')
    elif flag == 3:
        print('Stopping Criteria Flag: flag 3: Max iterations exceeded')

    # Plot f(x) vs. x
    x_vals = np.linspace(x0 - 1, x0 + 1, 100)
    f_vals = func(x_vals)

    x_highlight = x_new
    f_highlight = 0

    plt.figure()
    plt.plot(x_vals, f_vals)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f(x) vs. x')
    plt.grid(True)

    plt.plot(x_highlight, f_highlight, 'ro', markersize=10)
    plt.text(x_highlight, f_highlight, f'({x_highlight}, {f_highlight})', verticalalignment='bottom')
    plt.show()

    # Plot the approximate relative error vs. iteration number
    plt.figure()
    plt.plot(iterationVal, errorVal)
    plt.xlabel('iteration number')
    plt.ylabel('approximate relative')
    plt.title('Plot of approximate relative Vs iteration Number')
    plt.grid(True)
    plt.show()

elif choice == '2':
    functionExpression = input("Enter the function g(x): ")
    g = lambda x: eval(functionExpression)  # Create a lambda function based on user input
    x0 = float(input('Enter the starting point: '))
    tol_rel = float(input('Enter the convergence criterion for relative approximate errors: '))
    tol_func = float(input('Enter the convergence criterion for the function value: '))
    max_iterations = int(input('Enter the maximum number of iterations: '))

    x = x0
    flag = 0
    iteration = 0
    f_values = []
    x_vals = []
    errorVal = []
    iterationVal = []

    while iteration < max_iterations:
        x_prev = x

        x = g(x_prev)  # Evaluate the function g(x) at x

        f = g(x_prev) - x_prev  # Calculate the function value at the current x

        if abs(x) < 1e-8:
            approx_error = float('inf')
        else:
            approx_error = abs((x - x_prev) / x)  # Calculate the relative approximate error

        iteration += 1
        errorVal.append(approx_error)
        iterationVal.append(iteration)

        f_values.append(g(x))
        x_vals.append(x)

        if approx_error < tol_rel:
            flag = 1  # Relative approximate error convergence criterion met
            break
        elif abs(f) < tol_func:
            flag = 2  # Function value convergence criterion met
            break

    if iteration == max_iterations:
        flag = 3
        print('flag 3: Max iterations exceeded')

    print('Root: {:.6f}'.format(x))
    if flag == 1:
        print('Stopping Criteria Flag: flag 1: relative approximate error encountered')
    elif flag == 2:
        print('Stopping Criteria Flag: flag 2: convergence criterion for the function value encountered')
    elif flag == 3:
        print('Stopping Criteria Flag: flag 3: Max iterations exceeded')

    x_highlight = x
    f_highlight = g(x)

    import matplotlib.pyplot as plt

    plt.figure()
    plt.plot(x_vals, f_values)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of f(x) vs. x')
    plt.grid(True)

    plt.plot(x_highlight, f_highlight, 'ro', markersize=10)
    plt.text(x_highlight, f_highlight, f'({x_highlight}, {f_highlight})', verticalalignment='bottom')
    plt.show()

    plt.figure()
    plt.plot(iterationVal, errorVal)
    plt.xlabel('iteration number')
    plt.ylabel('approximate relative')
    plt.title('Plot of approximate relative Vs iteration Number')
    plt.grid(True)
    plt.show()


