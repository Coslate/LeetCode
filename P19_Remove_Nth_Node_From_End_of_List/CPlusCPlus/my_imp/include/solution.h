#ifndef _SOLUTION_H_
#define _SOLUTION_H_


class ListNode {
    int       val;
    ListNode *next;

    public:
        ListNode(): val(0), next(NULL){};
        ListNode(const int &val): val(val), next(NULL){};
        friend class LinkedList;
        friend class Solution;
};

class LinkedList{
    ListNode *head;

    public:
        LinkedList(): head(NULL){};
        ~LinkedList();
        void insertBackNode(const int &val);
        void setHead(ListNode * const in_head){head = in_head;}
        void printLinkedList();
        ListNode* getHead(){return head;}
};



class Solution {
public:
    Solution(){};
    ~Solution(){};

    ListNode* removeNthFromEnd(ListNode* head, int n);
};

#endif
