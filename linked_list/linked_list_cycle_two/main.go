package linkedlistcycletwo

type ListNode struct {
	Val int
	Next *ListNode
}
func detectCycle(head *ListNode) *ListNode {
	slow := head
	fast := head
	loopCompleted := true
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			loopCompleted = false
			break
		}
	}
	if loopCompleted {
		return nil
	}

	for head != slow {
		head = head.Next
		slow = slow.Next
	}

	return slow
}
