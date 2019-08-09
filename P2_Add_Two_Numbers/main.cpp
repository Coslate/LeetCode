#include <iostream>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <vector>
#include <solution.h>

int main(){
    //Declare final solution container.
    ListNode* L1_N0 = new ListNode(2);
    ListNode* L1_N1 = new ListNode(4);
    ListNode* L1_N2 = new ListNode(3);

    ListNode* L2_N0 = new ListNode(5);
    ListNode* L2_N1 = new ListNode(6);
    ListNode* L2_N2 = new ListNode(4);

    L1_N0->next = L1_N1;
    L1_N1->next = L1_N2;

    L2_N0->next = L2_N1;
    L2_N1->next = L2_N2;

    //Calculation body
    Solution sol_obj;
    ListNode* final_answer = sol_obj.addTwoNumbers(L1_N0, L2_N0);

    //Print the result.
    int count = 0;

    while(L1_N0 != NULL){
        if(count == 0){
            printf("Question = [%d", L1_N0->val);
        }else if(L1_N0->next == NULL){
            printf(", %d]", L1_N0->val);
        }else{
            printf(", %d", L1_N0->val);
        }

        L1_N0 = L1_N0->next;
        ++count;
    }

    count = 0;
    printf(" + ");

    while(L2_N0 != NULL){
        if(count == 0){
            printf("[%d", L2_N0->val);
        }else if(L2_N0->next == NULL){
            printf(", %d] = ?\n", L2_N0->val);
        }else{
            printf(", %d", L2_N0->val);
        }

        L2_N0 = L2_N0->next;
        ++count;
    }

    count = 0;

    while(final_answer != NULL){
        if(count == 0){
            printf("answer = [%d", final_answer->val);
        }else if(final_answer->next == NULL){
            printf(", %d]\n", final_answer->val);
        }else{
            printf(", %d", final_answer->val);
        }

        final_answer = final_answer->next;
        ++count;
    }

    return EXIT_SUCCESS;
}
