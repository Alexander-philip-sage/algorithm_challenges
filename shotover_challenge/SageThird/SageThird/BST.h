#pragma once
/* Binary Tree */

#include <iostream>
#include <deque>
#include <climits>
#include <vector>
namespace bst
{

	struct Tree
	{
		const Point* data;
		Tree* left;
		Tree* right;
		Tree* parent;
	};

	struct Tree* newTreeNode(const Point* data);

	struct Tree* insertTreeNode(struct Tree* node, const Point* data);

	int treeSize(struct Tree* node);

	/* Tree Minimum */
	Tree* minTree(struct Tree* node);

	/* Tree Maximum */
	Tree* maxTree(struct Tree* node);

	/* In Order Successor - a node which has the next higher key */
	Tree* succesorInOrder(struct Tree* node);

	/* In Order Predecessor - a node which has the next lower key */
	Tree* predecessorInOrder(struct Tree* node);


	void clear(struct Tree* node);
	/* print tree in order */
	/* 1. Traverse the left subtree.
	   2. Visit the root.
	   3. Traverse the right subtree.
	*/


	/* levelPrint()
	prints nodes at the same level
	This is simpler than the BreadthFirstTraversal(root) above
	It takes 2D vector with the same size of level (= MaxDepth+1)
	and fills elements as we traverse (preOrder) */

	/* Converting a BST into an Array */
	void TreeToArray(struct Tree* node, Point a[]);
	//copying first 'max_size' of the tree to an array
	void TreeToArray(struct Tree* node, Point a[], int max_size);
}