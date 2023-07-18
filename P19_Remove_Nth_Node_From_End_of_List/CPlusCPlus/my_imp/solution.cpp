#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>

LinkedList::~LinkedList(){
    ListNode *cur_head = head;
    while(cur_head != NULL){
        ListNode *next_head = cur_head->next;
        cur_head->next = NULL;
        delete cur_head;
        cur_head = next_head;
    }
}

void LinkedList::insertBackNode(const int &val){
    if(head == NULL){
        head = new ListNode(val);
    }else{
        ListNode *cur_head = head;
        while(cur_head->next != NULL){
            cur_head = cur_head->next;
        }
        cur_head->next = new ListNode(val);
    }
}

void LinkedList::printLinkedList(){
    ListNode *cur_head = head;
    std::cout<<"[";
    while(cur_head != NULL){
        if(cur_head->next == NULL){
            std::cout<<cur_head->val;
        }else{
            std::cout<<cur_head->val<<", ";
        }
        cur_head = cur_head->next;
    }
    std::cout<<"]";
}

ListNode* Solution::removeNthFromEnd(ListNode* head, int n){
    // LinkedList Traversing | Time: O(n) | Space: O(1)
    int length = 0;
    ListNode *cur_head = head;
    ListNode *pre_head = head;
    int del_pos = 0;
    int cnt = 0;

    while(cur_head != NULL){
        ++length;
        cur_head = cur_head->next;
    }

    del_pos = length-n;
    cur_head = head;

    if(del_pos == 0){
        head = head->next;
    }else{
        while(cnt < del_pos){
            pre_head = cur_head;
            cur_head = cur_head->next;
            cnt += 1;
        }
        pre_head->next = cur_head->next;
    }

    cur_head->next = NULL;
    delete cur_head;
    cur_head = NULL;
    return head;
}
