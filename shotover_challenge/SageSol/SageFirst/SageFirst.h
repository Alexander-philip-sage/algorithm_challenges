#pragma once

#ifdef SAGEFIRST_EXPORTS
#define SAGEFIRST_API __declspec(dllexport)
#else
#define SAGEFIRST_API __declspec(dllimport)
#endif

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


extern "C" SAGEFIRST_API void fibonacci_init(
    const unsigned long long a, const unsigned long long b);

// Produce the next value in the sequence.
// Returns true on success and updates current value and index;
// false on overflow, leaves current value and index unchanged.
extern "C" SAGEFIRST_API bool fibonacci_next();

// Get the current value in the sequence.
extern "C" SAGEFIRST_API unsigned long long fibonacci_current();

// Get the position of the current value in the sequence.
extern "C" SAGEFIRST_API unsigned fibonacci_index();

extern "C" SAGEFIRST_API void print_create(const Point * points_begin, const Point * points_end);