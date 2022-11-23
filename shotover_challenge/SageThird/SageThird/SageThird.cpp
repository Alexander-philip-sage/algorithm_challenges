
// SageThird.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include "SageThird.h"
#include <vector>

void insertionSort(int array[], int size) 
{
    for (int step = 1; step < size; step++) 
    {
        int key = array[step];
        int j = step - 1;

        // Compare key with each element on the left of it until an element smaller than
        // it is found.
        // For descending order, change key<array[j] to key>array[j].
        while (key < array[j] && j >= 0) {
            array[j + 1] = array[j];
            --j;
        }
        array[j + 1] = key;
    }
}

void print_point(const Point* tmp) {
    std::cout <<"rank:" << tmp->rank << "\t";
    std::cout << "id:" << tmp->id << std::endl;
    std::cout << "x:" << tmp->x<<"\t";
    std::cout << "y:" << tmp->y<< std::endl;
}

void print_create(const Point* points_begin, const Point* points_end)
{
    
    std::cout << "points_begin ";
    print_point(points_begin);
    std::cout << "points_end ";
    print_point(points_end);

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
            ++found;
            in_border.push_back(*pt);
        }
    }
    for (int i =0;i<count; i++)
    {
        out_points[i] = in_border[i];
    }
    //out_points = sort(in_border)
    return count;
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
