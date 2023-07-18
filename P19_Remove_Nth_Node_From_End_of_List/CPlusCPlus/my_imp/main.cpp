#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

int main(){
    //Declare final solution container.
    LinkedList llist_obj;
    llist_obj.insertBackNode(1);
    llist_obj.insertBackNode(2);
    llist_obj.insertBackNode(3);
    llist_obj.insertBackNode(4);
    llist_obj.insertBackNode(5);

    std::cout<<"head = ";
    llist_obj.printLinkedList();
    std::cout<<std::endl;

    //Calculation body
    Solution sol_obj;
    ListNode *new_head = sol_obj.removeNthFromEnd(llist_obj.getHead(), 2);
    llist_obj.setHead(new_head);

    //Print the result.
    std::cout<<"ans = ";
    llist_obj.printLinkedList();
    std::cout<<std::endl;

    return EXIT_SUCCESS;
}
