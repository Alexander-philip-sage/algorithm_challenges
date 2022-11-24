
// SageThird.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include "SageThird.h"
#include <vector>
#include <algorithm>

bool comparePoints(const Point x, const Point y){ return x.rank < y.rank;}
void insertionSort(std::vector<Point>& arr) 
{
    if (arr.size() < 2) { 
        std::cout << "error insertionSort. array too small to sort. arr.size() " <<arr.size() << std::endl;
        return;
    }
    //copying a lot of Point values
    for (int step = 1; step < arr.size(); step++)
    {
        Point key = arr[step];
        int j = step - 1;

        // Compare key with each element on the left of it until an element smaller than
        // it is found.
        // For descending order, change key<arr[j] to key>arr[j].
        while ((j >= 0)&&(key.rank < arr[j].rank))
        {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

void print_point(const Point* tmp) {
    std::cout <<"rank:" << tmp->rank << "\t";
    std::cout << "id:" << tmp->id << std::endl;
    std::cout << "x:" << tmp->x<<"\t";
    std::cout << "y:" << tmp->y<< std::endl;
}

SearchContext* create(const Point* points_begin, const Point* points_end)
{
    SearchContext* sc = new SearchContext;
    sc->points_begin = points_begin;
    sc->points_end = points_end;
    return sc;
}

int32_t search(SearchContext* sc, const Rect rect, const int32_t count, Point* out_points)
{
    std::vector<Point> in_border;
    //std::vector<Point*> in_border;
    //Point* in_border = new Point[count];
    //Point** in_border = new Point*[count];
    int32_t found=0;
    for (auto pt = sc->points_begin; pt < sc->points_end; pt++) {
        if ((pt->x > rect.lx) && (pt->x < rect.hx) && (pt->y > rect.ly) && (pt->y < rect.hy)&&(found < count)) 
        {
            //copy value - slow
            in_border.push_back(*pt);
            ++found;
        }
    }
    std::sort(in_border.begin(), in_border.end(), comparePoints); 
    //insertionSort(in_border);
    for (int i =0;i<count; i++)
    {
        out_points[i] = in_border[i];
    }
    //out_points = sort(in_border)
    return count;
}

int32_t search_slow(SearchContext* sc, const Rect rect, const int32_t count, Point* out_points)
{
    //written to measure against. intentionally slow.
    std::vector<Point> all_points;
    for (auto pt = sc->points_begin; pt < sc->points_end; pt++) {
        all_points.push_back(*pt);
    }
    int32_t found = 0;
    std::sort(all_points.begin(), all_points.end(), comparePoints);
    for (auto pt : all_points) {
        if ((pt.x > rect.lx) && (pt.x < rect.hx) && (pt.y > rect.ly) && (pt.y < rect.hy) && (found < count))
        {
            //copy value - slow
            out_points[found] = pt;
            ++found;
            if (found == count) {
                break;
            }
        }
    }
    //std::sort(in_border.begin(), in_border.end(), comparePoints);
    //insertionSort(in_border);
    return count;
}

SearchContext* destroy(SearchContext* sc)
{
    if (sc)
    {
        delete sc;
    }

    return nullptr;
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
