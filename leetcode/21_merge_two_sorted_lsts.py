class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        prev = head
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        while list1 is not None:
            prev.next = list1
            prev = list1
            list1 = list1.next
        while list2 is not None:
            prev.next = list2
            prev = list2
            list2 = list2.next
        prev.next = None
        return head
