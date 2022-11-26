#include <iostream>
#include <stdint.h>
#include "SageThird.h"
#include <ctime>

#include <cstdlib>
void orderly_points(Point all_points[], const int32_t N)
{
    for (int i = 0; i < N; i++) {
        all_points[i].id = i;
        all_points[i].rank = N - i;
        all_points[i].y = i;
        all_points[i].x = i;
    }
}
void random_points(Point all_points[], const int32_t N)
{
    std::srand(std::time(0));
    for (int i = 0; i < N; i++) {
        all_points[i].id = (int8_t)((rand() % 100) - 50);
        all_points[i].rank = (int32_t)((rand() % 200)-100);
        all_points[i].y = (float)((rand() % 100) - 50);
        all_points[i].x = (float)((rand() % 100) - 50);
    }
}
int main()
{
    const int32_t N = 10000;
    Point all_points[N];
    const int32_t count = 10;
    Point out_points[count];
    const Rect border = { 2,2,6,6 };
    random_points(all_points, N);
    const Point* points_begin = all_points;
    const Point* points_end = all_points+N-1;
    SearchContext* sc = create_i(points_begin, points_end);
    int32_t res = search_i(sc, &border, count, out_points);
    if (res != count) {
        std::cout << "Warning in search. found <"<< (int)count<< "  values in rectangle. Could be an error." << std::endl;
    }
    std::cout << std::endl << "Points found in border: " <<(int)res<< std::endl;
    for (auto pt= out_points; pt < (out_points + res); pt++)
    {
        print_point(pt);
    }
    std::cout << "End Function!\n";
    destroy_i(sc);
}
