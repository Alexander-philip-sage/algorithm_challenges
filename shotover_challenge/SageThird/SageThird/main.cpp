#include <iostream>
#include <stdint.h>
#include "SageThird.h"


int main()
{
    const int32_t N = 10;
    Point all_points[N];
    const int32_t count = 3;
    Point out_points[count];
    const Rect border = { 2,2,6,6 };
    for (int  i = 0; i < N; i++) {
        all_points[i].id = i;
        all_points[i].rank = N-i;
        all_points[i].y = i;
        all_points[i].x = i;
    }
    const Point* points_begin = all_points;
    const Point* points_end = all_points+N-1;
    SearchContext* sc = create(points_begin, points_end);
    int32_t res = search(sc, border, count, out_points);
    if (res != count) {
        std::cout << "error in search" << std::endl;
    }
    std::cout << std::endl << "Points found in border" << std::endl;
    for (auto pt= out_points; pt < (out_points + count); pt++)
    {
        print_point(pt);
    }
    std::cout << "End Function!\n";
}
