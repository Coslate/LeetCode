#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>

ListNode* Solution::addTwoNumbers(ListNode* l1, ListNode* l2){
    ListNode* l1_trav = l1;
    ListNode* l2_trav = l2;
    ListNode* dummy_head = new ListNode(0);
    ListNode* ans = dummy_head;
    int carrier = 0;

    while((l1_trav != NULL) || (l2_trav != NULL)){
        int tmp_num = 0;
            
        if(l1_trav != NULL){
            tmp_num += l1_trav->val;
        }
        if(l2_trav != NULL){
            tmp_num += l2_trav->val;
        }
            
        tmp_num+=carrier;
        carrier = tmp_num/10;
        ListNode* tmp_node = new ListNode(tmp_num%10);
            
        ans->next = tmp_node;
        ans = ans->next;
        if(l1_trav != NULL) l1_trav = l1_trav->next;
        if(l2_trav != NULL) l2_trav = l2_trav->next;
    }
        
    if(carrier == 1){
        ListNode* tmp_node = new ListNode(carrier);
        ans->next = tmp_node;
    }

    return dummy_head->next;
}
