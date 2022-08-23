class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Creating a list
        temp = []
        
        # Looping till the end
        while(head):
            
            # Appending each value of head to the list we've created earlier as temp
            temp.append(head.val)
            
            # Moving further and hence incrementing head with head.next
            head = head.next
            
        # If the temp list is equal to the reversal of the temp list
        if(temp==temp[::-1]):
            
            # It means that the linked list is a palindrome
            return True
        
        # Otherwise
        else:
            # It is not a palindrome
            return False