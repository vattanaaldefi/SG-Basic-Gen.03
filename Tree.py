class Node :
	def __init__(self, val) :
		self.info = val
		self.left = None
		self.right = None
	def insert(self, val) :
		if val < self.info :
			if (self.left is None) :
				self.left = Node(val)
			else :
				self.left.insert(val)
		elif val > self.info :
			if self.right is None :
				self.right = Node(val)
			else :
				self.right.insert(val)

	def in_order(self):
		if self.left :
			self.left.in_order()
		print (self.info, end=" ")
		if self.right :
			self.right.in_order()

	def pre_order(self):
		print (self.info, end=" ")
		if self.left :
			self.left.in_order()
		if self.right :
			self.right.in_order()

	def post_order(self):
		if self.left :
			self.left.in_order()
		if self.right :
			self.right.in_order()
		print (self.info,end=" ")

	def search(self, val) :
		if val < self.info :
			if (self.left is None) :
				return self.left.search(val)
			else :
				return False
		elif val > self.info :
			if self.right is None :
				return self.right.search(val)
			else :
				return False
		else :
			return True

def heighttree(node):
	if node is None:
		return 0 ; 

	else :
		kiri = heighttree(node.left)
		kanan = heighttree(node.right)

		if (kiri > kanan):
			return kiri+1
		else:
			return kanan+1			

BT = Node(23)
BT.insert(10)
BT.insert(16)
BT.insert(19)
BT.insert(65)
BT.insert(45)
BT.insert(24)
BT.insert(30)
BT.insert(67)
BT.in_order()
print(" ")
BT.pre_order()
print(" ")
BT.post_order()
print(" ")
print(BT.search(23))
print(BT.search(1))
print(BT.search(2))
print(heighttree(BT))