
    
function x = gauss(A, b)
    % Gaussian elimination with partial pivoting
    
    n = size(A, 1);
    Aug = [A b]; % Augmented matrix
    
    % Forward elimination
    for k = 1:n-1
        % Partial pivoting
        [~, maxRow] = max(abs(Aug(k:n, k)));
        maxRow = maxRow + k - 1;
        
        % Swap rows
        Aug([k maxRow], :) = Aug([maxRow k], :);
        
        % Elimination
        for i = k+1:n
            factor = Aug(i, k) / Aug(k, k);
            Aug(i, k:n+1) = Aug(i, k:n+1) - factor * Aug(k, k:n+1);
        end
    end
    
    % Back substitution
    x = zeros(n, 1);
    x(n) = Aug(n, n+1) / Aug(n, n);
    
    for k = n-1:-1:1
        x(k) = (Aug(k, n+1) - Aug(k, k+1:n) * x(k+1:n)) / Aug(k, k);
    end
end
