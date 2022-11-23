#include "pch.h" // use stdafx.h in Visual Studio 2017 and earlier
#include <utility>
#include <limits.h>
#include "SageFirst.h"
#include <iostream>

struct SearchContext
{
    const Point* points_begin; const Point* points_end;
};
/* Load the provided points into an internal data structure. The pointers follow the STL iterator convention, where
"points_begin" points to the first element, and "points_end" points to one past the last element. The input points are
only guaranteed to be valid for the duration of the call. Return a pointer to the context that can be used for
consecutive searches on the data. */
extern "C" SAGEFIRST_API SearchContext* __stdcall  create(
    const Point* points_begin, const Point* points_end)
{
    SearchContext* sc = new SearchContext();
    sc->points_begin = points_begin;
    sc->points_end = points_end;
    return sc;
}
void print_create(const Point* points_begin, const Point* points_end)
{
    SearchContext* sc = new SearchContext();
    sc->points_begin = points_begin;
    sc->points_end = points_end;
    std::cout << "sc->points_begin  rank:"<< sc->points_begin->rank << std::endl;
}
/* Search for "count" points with the smallest ranks inside "rect" and copy them ordered by smallest rank first in
"out_points". Return the number of points copied. "out_points" points to a buffer owned by the caller that
can hold "count" number of Points.*/
extern "C" SAGEFIRST_API  int32_t __stdcall search(SearchContext * sc, const Rect * rect, const int32_t count, Point * out_points);

/* Release the resources associated with the context. Return nullptr if successful, "sc" otherwise. */
extern "C" SAGEFIRST_API  SearchContext * __stdcall destroy(SearchContext * sc);



// DLL internal state variables:
static unsigned long long previous_;  // Previous value, if any
static unsigned long long current_;   // Current sequence value
static unsigned index_;               // Current seq. position

// Initialize a Fibonacci relation sequence
// such that F(0) = a, F(1) = b.
// This function must be called before any other function.
void fibonacci_init(
    const unsigned long long a,
    const unsigned long long b)
{
    index_ = 0;
    current_ = a;
    previous_ = b; // see special case when initialized
}

// Produce the next value in the sequence.
// Returns true on success, false on overflow.
bool fibonacci_next()
{
    // check to see if we'd overflow result or position
    if ((ULLONG_MAX - previous_ < current_) ||
        (UINT_MAX == index_))
    {
        return false;
    }

    // Special case when index == 0, just return b value
    if (index_ > 0)
    {
        // otherwise, calculate next sequence value
        previous_ += current_;
    }
    std::swap(current_, previous_);
    ++index_;
    return true;
}

// Get the current value in the sequence.
unsigned long long fibonacci_current()
{
    return current_;
}

// Get the current index position in the sequence.
unsigned fibonacci_index()
{
    return index_;
}