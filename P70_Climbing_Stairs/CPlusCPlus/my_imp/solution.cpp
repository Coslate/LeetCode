#include <solution.h>
#include <cmath>
#include <cstdlib>

size_t number_of_digits(int n) {
    std::ostringstream strs;
    strs << n;
    return strs.str().size();
}

void print_matrix(const int M[nmax][nmax], size_t n, size_t m) {
    size_t max_len_per_column[nmax];

    for (size_t j = 0; j < m; ++j) {
        size_t max_len {};

        for (size_t i = 0; i < n; ++i){
            const auto num_length {number_of_digits(M[i][j])};

            if (num_length > max_len){
                max_len = num_length;
            }
        }

        max_len_per_column[j] = max_len;
    }

    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < m; ++j)
            std::cout << (j == 0 ? "\n| " : "") << std::setw(max_len_per_column[j]) << M[i][j] << (j == m - 1 ? " |" : " ");

    std::cout << '\n';
}

int Solution::climbStairs(int n){
    //Dynamic Programming | Time: O(1) | Space: O(1), n is the input length of array
    //P(n) = P(n-1) + P(n-2), P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 5, P(5) = 8
    if(n == 1){
        return 1;
    }else if(n == 2){
        return 2;
    }

    int ans = 0;
    int* p = new int[n+1]();
    p[1] = 1;
    p[2] = 2;

    for(int i=3; i < n+1; ++i){
        p[i] = p[i-1]+p[i-2];
    }
    ans = p[n];
    delete [] p;

    return ans;
}

int OptSolution::climbStairs(int n){
    //Dynamic Programming | Time: O(logn) | Space: O(1), n is the input length of array
    //P(n) = P(n-1) + P(n-2), P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 5, P(5) = 8
    //Declare long type of matrix for situations that multipling result may surpass the integer range.
    long q[2][2] = {
                       {1, 1},
                       {1, 0}
    };
    long res[2][2] {};
    matrixPower<long, 2, 2>(q, res, n);
    return res[0][0];
}

