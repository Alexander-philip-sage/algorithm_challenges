#pragma once
////////////////////////////////////

/* This standard header defines the sized types used. */
#include <stdint.h>

/* The following structs are packed with no padding. */
#pragma pack(push, 1)

/* Defines a point in 2D space with some additional attributes like id and rank. */
struct Point
{
	int8_t id;
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
struct SearchContext;
////////////////////////////////////

enum Quadrant
{
	BOTTOMLEFT = 0,
	BOTTOMRIGHT = 1,
	TOPLEFT = 2,
	TOPRIGHT = 3,
	// Masks
	RIGHT = 1,
	TOP = 2,
};

class QuadNode;

class QuadTree
{
private:
	QuadNode* root;
	Rect extents;
	Point* allPoints;
	int nAllPoints;

public:
	QuadTree(const Point* points_begin, const Point* points_end);
	~QuadTree();
	int32_t Search(const Rect* rect, const int32_t count, Point* out_points);
};

class QuadNode
{
private:
	static const int leaf_capacity = 4096;
	static const int branch_capacity = 256;
	static const int max_depth = 256;

	Point* allPoints;
	bool isLeaf;
	std::vector<int32_t> points;
	QuadNode* child[4];
	Rect bounds;

public:
	QuadNode(Point*, Rect);
	~QuadNode();
	void Insert(Point, int = 0);
	int Count();
	void Sort();
	void Search(const Rect rect, const int32_t count, std::vector<int32_t>& results);
};
