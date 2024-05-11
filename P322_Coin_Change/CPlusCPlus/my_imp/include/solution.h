#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

constexpr size_t nmax {2};
size_t number_of_digits(int n);
void print_matrix(const int M[nmax][nmax], size_t n, size_t m);

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int climbStairs(int n);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int climbStairs(int n);
    template<class T, std::size_t rows, std::size_t cols>
    void matrixPower(const T (&q)[rows][cols], T (&res)[rows][cols], const int k);
    template<class T, std::size_t rows, std::size_t cols>
    void matrixMultiply(const T (&a)[rows][cols], const T (&b)[cols][rows], T res[rows][rows]);
    template<class T, std::size_t rows, std::size_t cols>
    void copyData(const T (&q)[rows][cols], T (&res)[rows][cols]);
};

#include <solution.imp.h>
#endif
