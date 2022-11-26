#pragma once

#include <stdint.h>
#include <vector>
#include <limits.h>
/* The following structs are packed with no padding. */
#pragma pack(push, 1)

/* Defines a point in 2D space with some additional attributes like id and rank. */
struct Point
{
	int id;
	int32_t rank;
	float x;
	float y;
};

/* Defines a rectangle, where a point (x,y) is inside, if x is in [lx, hx] and y is in [ly, hy]. */
struct Rect
{
	float lx;
	float ly;
	float hx;
	float hy;
};
#pragma pack(pop)

/* Declaration of the struct that is used as the context for the calls. */
struct SearchContext
{
	const Point* points_begin;
	const Point* points_end;
};

class Node {
public:
	Point pt;
	Node* next;
	Node* prev;
	Node(const Point&);
};
class sortedLinkedList {
private:
	int size=0;
	int max_size = 0;
	Node* access;
	Node* head;
	Node* tail;
	int max_rank = INT_MIN;
public:
	sortedLinkedList(int);
	bool insert(const Point&);
	Node* get_access();
	Node* get_head();
};
sortedLinkedList::sortedLinkedList(int s, int ms) {
	size = s;
	max_size = ms;
}
void sortedLinkedLIst::insert(const Point& pt) {
	if (size == 0)
	{
		head = new Node(pt);
		access = head;
		tail = head;
		size++;
		max_rank = pt.rank;
	}
	else {
		Node* current;
		if ((size < max_size)||(pt.rank < max_rank)) {
			current = head;
			size++;
		}
		
		if (size > max_size) {
			//linked list is too big, remove last one
			Node* ptrm =  tail;
			tail = tail->prev;
			delete ptrm;
		}
	}
}
Node::Node(const Point& point) {
	pt=point;
}
/* function to insert a new_node
in a list. Note that this
function expects a pointer to
head_ref as this can modify the
head of the input linked list
(similar to push())*/
void sortedInsert(Node** head_ref,
	Node* new_node)
{
	Node* current;
	/* Special case for the head end */
	if (*head_ref == NULL
		|| (*head_ref)->data
		>= new_node->data) {
		new_node->next = *head_ref;
		*head_ref = new_node;
	}
	else {
		/* Locate the node before the
 point of insertion */
		current = *head_ref;
		while (current->next != NULL
			&& current->next->data
			< new_node->data) {
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
}

void print_point(const Point* tmp);
SearchContext* create(const Point* points_begin, const Point* points_end);
/* Search for "count" points with the smallest ranks inside "rect" and copy them ordered by smallest rank first in
"out_points". Return the number of points copied. "out_points" points to a buffer owned by the caller that
can hold "count" number of Points. */
int32_t search(SearchContext* sc, const Rect rect, const int32_t count, Point* out_points);
bool comparePoints(const Point x, const Point y);
void insertionSort(std::vector<Point>& arr);
SearchContext* destroy(SearchContext* sc);
int32_t search_slow(SearchContext* sc, const Rect rect, const int32_t count, Point* out_points);
