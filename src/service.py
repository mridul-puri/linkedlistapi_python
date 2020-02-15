import modules

listOfLinkedLists = dict()

def create(name,birthyear):
	node = modules.ListNode(name,birthyear)
	li = modules.LinkedList()
	li.create(node)
	listOfLinkedLists[li.id] = li
	respMeta = modules.ResponseMeta(li.id,li.length)
	items = getListItems(li)
	resp = modules.GetResponse(respMeta.__dict__,items)
	return resp.__dict__

def push(listid,name,birthyear):
	if listid not in listOfLinkedLists.keys():
		return None
	li = listOfLinkedLists.get(listid)
	node = modules.ListNode(name, birthyear)
	li.pushAtEnd(node)
	respMeta = modules.ResponseMeta(listid, li.length)
	items = getListItems(li)
	resp = modules.GetResponse(respMeta.__dict__,items)
	return resp.__dict__

def pop(listid):
	if listid not in listOfLinkedLists.keys():
		return None
	li = listOfLinkedLists.get(listid)
	node = li.pop()
	if node is None:
		return None
	resp = modules.GetPopResponse(node.name, node.birthyear)
	return resp.__dict__

def remove(listid,name,birthyear):
	if listid not in listOfLinkedLists.keys():
		return None
	li = listOfLinkedLists.get(listid)
	li.remove(name,birthyear)
	respMeta = modules.ResponseMeta(listid, li.length)
	items = getListItems(li)
	resp = modules.GetResponse(respMeta.__dict__, items)
	return resp.__dict__

def list(listid):
	if listid not in listOfLinkedLists.keys():
		return None
	li = listOfLinkedLists.get(listid)
	respMeta = modules.ResponseMeta(listid, li.length)
	items = getListItems(li)
	resp = modules.GetResponse(respMeta.__dict__, items)
	return resp.__dict__

def reverse(listid):
	if listid not in listOfLinkedLists.keys():
		return None
	li = listOfLinkedLists.get(listid)
	node = li.reverse()
	li.head = node
	respMeta = modules.ResponseMeta(listid, li.length)
	items = getListItems(li)
	resp = modules.GetResponse(respMeta.__dict__, items)
	return resp.__dict__

def delete(listid):
	if listid not in listOfLinkedLists.keys():
		return None
	deleted = listOfLinkedLists.pop(listid,None)
	if deleted is None:
		return None
	else:
		return True

def getListItems(li):
	arr = []
	tmp = li.head
	while(tmp is not None):
		if(tmp.next is None):
			next = None
		else:
			next = tmp.next.id
		respObj = modules.ResponseObject(tmp.id,tmp.name,tmp.birthyear,next)
		arr.append(respObj.__dict__)
		tmp = tmp.next
	return arr