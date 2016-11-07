#!/usr/bin/python

indexValue = 0

class Node(object):

	def __init__(self, parent, children_list, value):
		"""Constructor for Node type object, defines the essential elements of the object:
		the parent, the children, and an integer indexValue to help reffering to the node(will
		be unique and assigned automatically), and a generic value"""
		global indexValue
		self.parent = parent
		if parent != None:
			parent.children_list.append(self)
		self.children_list = children_list
		self.indexValue = indexValue
		indexValue += 1
		self.value = value

	def createPathToRoot(self):
		"""Given a node, the function will create a path to the root"""
		res = [self.indexValue]
		if self.isRoot():
			res.append(self.indexValue)
		else:
			node = self
			
			while node.parent != None:
				node = node.parent
				res.append(node.indexValue)
			
		return res

	def level(self):
		"""Given a node, the function will create a path to the root"""
		res = 1
		if self.parent == None:
			res += 1
		else:
			node = self
			
			while node.parent != None:
				node = node.parent
				res += 1
			
		return res

	def setAsChild(self, parent):
		"""Given a node, the function will set it as child of given 'parent' node"""
		self.parent = parent
		parent.children_list.append(self)

	def deleteSubtree(self):
		"""Deletes whole subtree"""
		self.parent.children_list.remove(self)
		self.parent = None

	def deleteNodeAndRelink(self):
		"""Deletes given node from tree and links it's children with it's parent"""
		while len(self.children_list) > 0:
			child = self.children_list[0]
			child.parent = None
			child.setAsChild(self.parent)
			self.children_list.remove(child)

		self.parent.children_list.remove(self)
		self.parent = None

	def isRoot(self):
		"""1 if given node is a tree's root
		   0 otherwise"""
		if self.parent == None:
			return 1
		else:
			return 0

	def isLeaf(self):
		"""1 if given node is a leaf
		   0 otherwise"""
		if len(self.children_list) == 0:
			return 1
		else:
			return 0;

	def printTree(self):
		"""Function for nicely print the subtree of a given node(or whole tree if root given).
		Resembles bash's `tree` command, showing the tree like this:
		parent
		  |-son1
		    |-son of son 1
		    |-another son of son1
		...
		"""
		if self.isRoot():
			print self
		for child in self.children_list:
			print child
			child.printTree()

	def __repr__(self):
		"""Function for printing a single node with it's indexValue"""
		tabs = ""
		if not self.isRoot():
			for i in range(0, self.level() - 1):
				tabs = tabs + "  "
		return "%s|-Node with indexValue %s and value %s" % (tabs, self.indexValue, self.value)