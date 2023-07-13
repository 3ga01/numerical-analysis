% Non-linear equation solver
choice = input("Choose a method:\n(1) Bisection\n(2) Fixed-Point\n(3) Newton-Raphson\n");

if (choice == 1)
    functionExpression = input("Enter the function: ", "s");
    func = str2func(['@(x) ' functionExpression]);

    x00 = input("Enter the first starting point x0: ");
    x11 = input("Enter the second starting point x1: ");
    relApproxError = input('Enter the convergence criterion for the relative approximate error: ');
    funcValue = input("How close should f(x) be to zero to stop: ");
    maxIterations = input("Maximum number of iterations: ");

    x0 = x00;
    x1 = x11;
    x2_prev = 0;
    iteration = 0;

    xValues = [];
    yValues = [];
    errorVal = [];
    itrationVal = [];

    while iteration < maxIterations

    iteration = iteration + 1;

    x2 = (x0 + x1) / 2;
    b=func(x0) * func(x2);
    if func(x0) * func(x2) < 0
        x1 = x2;
    else 
        x0 = x2;
    end 
  
    a = abs((x2-x2_prev)/x2);
    if abs((x2-x2_prev)/x2) < relApproxError
        Root = x2;
        flag =1;
         disp('flag1: relative approximate error criteria reached');
          disp(['Root: ',num2str(Root)]);
        break;
    end

     if abs(func(x2)) < funcValue
        Root = x2;
        flag = 2;
         disp('flag2: function value criteria reached');
          disp(["Root: ",num2str(Root)]);
     break;
     end

    x2_prev = x2;

    xValues = linspace(x00, x11, iteration);
    yValues = zeros(size(xValues));

    for i = 1:iteration
    yValues(i) = func(xValues(i));
    end

    w=iteration;
    errorVal(w) = a;
    iterationVal(w) = iteration;

   
   

    end

    disp('flag3: Maximum number of iterations reached.');
     flag = 3;
     Root = x2;
     disp(["Root: ",num2str(Root)]);
    figure
    plot(xValues, yValues);
    xlabel('x');
    ylabel('f(x)');
    title('Plot of f(x) vs x');
    grid on;

    x_highlight = x2;
    f_highlight = 0;
    highlight = [x_highlight,f_highlight];

    hold on;
    plot(x_highlight, f_highlight, 'ro', 'MarkerSize', 10);
    text(x_highlight, f_highlight,['(' num2str(x_highlight) ', ' num2str(f_highlight) ')'], 'VerticalAlignment', 'bottom');
    hold off;   


    figure;
    plot(iterationVal, errorVal);
     xlabel("iteration number");
     ylabel("approximate relative");
     title("Plot of approximate relative Vs iteration Number");
     grid on;
end

if choice == 3
    functionExpression = input("Enter the function: ", "s");
func = str2func(['@(x) ' functionExpression]);

df = input('Enter the derivative of f(x): ','s');
x0 = input('Enter the starting point: ');

df = str2func(['@(x) ' df]);

epsilon1 = input('Enter the convergence criterion for relative approximate errors: ');
epsilon2 = input('Enter the convergence criterion for the function value: ');
maxIterations = input('Enter the maximum number of iterations: ');

% Initialize variables
iter = 0;
x_old = x0;
error = 1;

errorVal = [];
itrationVal = [];


% Newton-Raphson iteration
while error > epsilon1 && abs(func(x_old)) > epsilon2 && iter < maxIterations
    x_new = x_old - func(x_old) / df(x_old);
    error = abs((x_new - x_old) / x_new);
    x_old = x_new;
    iter = iter + 1;

     w=iter;
    errorVal(w) = error;
    iterationVal(w) = iter;
end

% Check convergence
if iter == maxIterations
    disp('Maximum number of iterations reached without convergence.');
else
    root = x_new;
    fprintf('Root: %.6f\n', root);
end
% Plot f(x) vs. x
x_vals = linspace(x0 - 1, x0 + 1, 100);
f_vals = func(x_vals);

figure;
plot(x_vals, f_vals);
xlabel('x');
ylabel('f(x)');
title('f(x) vs. x');

% Plot the approximate relative error vs. iteration number


 figure;
    plot(iterationVal, errorVal);
     xlabel("iteration number");
     ylabel("approximate relative");
     title("Plot of approximate relative Vs iteration Number");
     grid on;

end

if choice == 2
    % Step 1: Ask for g(x) and the starting point
    g = input('Enter g(x): ','s');
    g = str2func(['@(x) ' g]);

    x0 = input('Enter the starting point: ');

    % Step 2: Ask for stopping criteria
    tol_rel = input('Enter the convergence criterion for relative approximate errors: ');
    tol_func = input('Enter the convergence criterion for the function value: ');
    max_iterations = input('Enter the maximum number of iterations: ');

    % Step 3: Perform fixed-point iteration
    x = x0;
    flag = 0;
    iter = 0;
    f_values = [];
    approx_errors = [];

    while iter < max_iterations
        x_prev = x;

        % Calculate the new value of x using the fixed-point iteration formula
        x = g(x_prev);

        % Calculate the function value at the current x
        f = x - g(x);

        % Calculate the relative approximate error
        approx_error = abs((x - x_prev) / x);

        % Add current values to the lists for plotting
        f_values = [f_values; f];
        approx_errors = [approx_errors; approx_error];

        % Check stopping criteria
        if approx_error < tol_rel
            flag = 1; % Relative approximate error convergence criterion met
            break;
        elseif abs(f) < tol_func
            flag = 2; % Function value convergence criterion met
            break;
        end

        iter = iter + 1;
    end

    % Step 4: Display results
    fprintf('Root: %.6f\n', x);
    fprintf('Stopping Criteria Flag: %d\n', flag);

    % Plot f(x) vs. x
    figure;
    plot(x0:x, f_values);
    xlabel('x');
    ylabel('f(x)');
    title('Plot of f(x) vs. x');

    % Plot the approximate relative error vs. iteration number
    figure;
    plot(1:iter, approx_errors);
    xlabel('Iteration');
    ylabel('Approximate Relative Error');
    title('Plot of Approximate Relative Error vs. Iteration Number');
end




 



   

    
   

