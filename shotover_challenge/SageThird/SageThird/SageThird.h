#pragma once

#include <stdint.h>
#include <vector>
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
struct SearchContext
{
	const Point* points_begin;
	const Point* points_end;
};

void print_point(const Point* tmp);
SearchContext* create_i(const Point* points_begin, const Point* points_end);
/* Search for "count" points with the smallest ranks inside "rect" and copy them ordered by smallest rank first in
"out_points". Return the number of points copied. "out_points" points to a buffer owned by the caller that
can hold "count" number of Points. */
int32_t search_i(SearchContext* sc, const Rect* rect, const int32_t count, Point* out_points);
bool comparePoints(const Point x, const Point y);
void insertionSort(std::vector<Point>& arr);
SearchContext* destroy_i(SearchContext* sc);
int32_t search_slow(SearchContext* sc, const Rect* rect, const int32_t count, Point* out_points);
