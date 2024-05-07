#pragma once

#include <solution.h>
#include <sstream>
#include <iomanip>

template<class T, std::size_t rows, std::size_t cols>
void OptSolution::copyData(const T (&q)[rows][cols], T (&res)[rows][cols]){
    for(std::size_t i=0; i < rows; ++i){
        for(std::size_t j=0; j < cols; ++j){
            res[i][j] = q[i][j];
        }
    }
}

template<class T, std::size_t rows, std::size_t cols>
void OptSolution::matrixPower(const T (&q)[rows][cols], T (&res)[rows][cols], const int k){
    int power = k;
    T multi_square_q[rows][cols] {};
    T multi_operand_a[rows][cols] {};
    T multi_operand_b[rows][cols] {};
    T multi_operand_res[rows][cols] {};

    //set res = I
    for(std::size_t i=0; i < rows; ++i){
        for(std::size_t j=0; j < cols; ++j){
            if(i == j){
                res[i][j] = 1;
            }
        }
    }

    //copy from q to multi_square_q
    copyData(q, multi_square_q);

    while(power > 0){
        if(power & 1){
            copyData(res, multi_operand_res);
            matrixMultiply<T, rows, cols>(multi_square_q, multi_operand_res, res);
        }
        copyData(multi_square_q, multi_operand_a);
        copyData(multi_square_q, multi_operand_b);
        matrixMultiply<T, rows, cols>(multi_operand_a, multi_operand_b, multi_square_q);
        power = power >> 1;
    }
}

template<class T, std::size_t rows, std::size_t cols>
void OptSolution::matrixMultiply(const T (&a)[rows][cols], const T (&b)[cols][rows], T res[rows][rows]){
    for(std::size_t i = 0; i < rows; ++i){
        for(std::size_t j = 0; j < cols; ++j){
            res[i][j] = 0;
            for(std::size_t k = 0; k < cols; ++k)
                res[i][j] += a[i][k] * b[k][j];
        }
    }
}
