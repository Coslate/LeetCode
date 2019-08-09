#ifndef _SOLUTION_H_
#define _SOLUTION_H_

class ListNode{
    public : 
        int val;
        ListNode* next;
        ListNode() : val(0), next(NULL){};
        ListNode(const int value) : val(value), next(NULL){};
};

class Solution {
public:
    Solution(){};
    ~Solution(){};

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2);
};

#endif
