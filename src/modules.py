class ListNode:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        self.next = None
		
class LinkedList:
	inc = 100
	def __init__(self):
		LinkedList.inc += 1
		self.length = 1
		self.id = LinkedList.inc
		self.nodeid = 0

	def create(self,node):
		self.head = node
		node.id = 1
		self.nodeid += 1

	def pushAtEnd(self,node):
		if self.head is None:
			self.head = node
			node.id = 1
		else:
			tmp = self.head
			while(tmp.next is not None):
				tmp = tmp.next
			tmp.next = node
		self.length += 1
		self.nodeid += 1
		node.id = self.nodeid

	def pop(self):
		if self.head is None:
			return None
		p = self.head
		q = None
		next = p.next
		if next is None:
			self.head = None
			self.length -= 1
			return p
		next = p.next
		while next is not None:
			q = p
			p = next
			next = p.next
		q.next  = None
		self.length -= 1
		return p

	def remove(self,name,birthyear):
		if self.head is None:
			return None
		q = self.head
		p = None
		while(q is not None):
			if q.name.casefold() == name.casefold() and q.birthyear == birthyear:
				if p is None:
					p = q
					q = p.next
					self.head = q
				else:
					p.next = q.next
					q = p.next
				self.length -= 1
			else:
				p = q
				q = q.next

	def reverse(self):
		prev = None
		curr = self.head
		next = None
		while curr is not None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev

class ResponseMeta:
	def __init__(self,id,length):
		self.id = id
		self.length = length

class ResponseObject:
	def __init__(self,id, name, birthyear, next):
		self.id = id
		self.name = name
		self.birthyear = birthyear
		self.next = next

class GetResponse:
	def __init__(self,meta,object):
		self.meta = meta
		self.object = object

class GetPopResponse:
	def __init__(self,name,birthyear):
		self.name = name
		self.birthyear = birthyear

