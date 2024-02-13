/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode p = new ListNode(-1);
        ListNode pre = new ListNode(-1);
        if(head == null || head.next == null) return head;
        p.next = head;
        // pre.next = head;
        while(p.next != null){
            pre = p;
            boolean in = false;
            while(p.next != null && p.next.next != null && p.next.val == p.next.next.val){
                p.next.next = p.next.next.next;
                in = true;
            }
            if(pre == null) return null;
            if(in)
                pre.next = p.next.next;
            else p = p.next;
        }
    return head;
    }
}