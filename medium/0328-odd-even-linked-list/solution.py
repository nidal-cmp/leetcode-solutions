
        odd = head
        even = odd.next

        while odd and even:
            odd = odd.next.next
            even = even.next.next

        return head
        
