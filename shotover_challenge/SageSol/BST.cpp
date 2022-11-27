/* Binary Tree */
//stolen from
//https://www.bogotobogo.com/cplusplus/binarytree.php
#include <deque>
#include <climits>
#include <vector>
#include "SageThird.h"
#include "BST.h"

namespace bst
{


	struct Tree* newTreeNode(const Point* data)
	{
		Tree* node = new Tree;
		node->data = data;
		node->left = NULL;
		node->right = NULL;
		node->parent = NULL;

		return node;
	}

	struct Tree* insertTreeNode(struct Tree* node, const Point* data)
	{
		static Tree* p;
		Tree* retNode;

		//if(node != NULL) p = node;

		if ((node == NULL) || node->data == NULL) {
			retNode = newTreeNode(data);
			retNode->parent = p;
			return retNode;
		}
		if (comparePoints(*data, *(node->data))) {
			p = node;
			node->left = insertTreeNode(node->left, data);
		}
		else {
			p = node;
			node->right = insertTreeNode(node->right, data);
		}
		return node;
	}

	int treeSize(struct Tree* node)
	{
		if (node == NULL) return 0;
		else
			return treeSize(node->left) + 1 + treeSize(node->right);
	}

	/* Tree Minimum */
	Tree* minTree(struct Tree* node)
	{
		if (node == NULL) return NULL;
		while (node->left)
			node = node->left;
		return node;
	}

	/* Tree Maximum */
	Tree* maxTree(struct Tree* node)
	{
		while (node->right)
			node = node->right;
		return node;
	}

	/* In Order Successor - a node which has the next higher key */
	Tree* succesorInOrder(struct Tree* node)
	{
		/* if the node has right child, seccessor is Tree-Minimum */
		if (node->right != NULL) return minTree(node->right);

		Tree* y = node->parent;
		while (y != NULL && node == y->right) {
			node = y;
			y = y->parent;
		}
		return y;
	}

	/* In Order Predecessor - a node which has the next lower key */
	Tree* predecessorInOrder(struct Tree* node)
	{
		/* if the node has left child, predecessor is Tree-Maximum */
		if (node->left != NULL) return maxTree(node->left);

		Tree* y = node->parent;
		/* if it does not have a left child,
		predecessor is its first left ancestor */
		while (y != NULL && node == y->left) {
			node = y;
			y = y->parent;
		}
		return y;
	}

	void clear(struct Tree* node)
	{
		if (node != NULL) {
			clear(node->left);
			clear(node->right);
			delete node;
		}
	}



	/* Converting a BST into an Array */
	void TreeToArray(struct Tree* node, Point a[]) {
		static int pos = 0;

		if (node) {
			TreeToArray(node->left, a);
			a[pos++] = *(node->data);
			TreeToArray(node->right, a);
		}
	}
	/* Converting a BST into an Array */
	void TreeToArray(struct Tree* node, Point a[], int max_size) {
		static int pos = 0;

		if (node) {
			TreeToArray(node->left, a, max_size);
			a[pos++] = *(node->data);
			if (pos == (max_size - 1)) { return; }
			TreeToArray(node->right, a, max_size);
		}
	}
}