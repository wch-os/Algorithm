/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        // 0글자 또는 1글자
        if (head == null || head.next == null)
            return head;

        ListNode second = head.next;
        ListNode third = second.next; // 무한 재귀 방지

        second.next = head;
        head.next = swapPairs(third);

        return second;
    }
}