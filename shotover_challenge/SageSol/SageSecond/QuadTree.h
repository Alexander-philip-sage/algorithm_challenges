#pragma once

enum Quadrant
{
  BOTTOMLEFT  = 0,
  BOTTOMRIGHT = 1,
  TOPLEFT     = 2,
  TOPRIGHT    = 3,
  // Masks
  RIGHT       = 1,
  TOP         = 2,
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
  static const int leaf_capacity    = 4096;
  static const int branch_capacity  = 256;
  static const int max_depth        = 256;

  Point* allPoints;
  bool isLeaf;
  std::vector<int32_t> points;
  QuadNode* child[4];
  Rect bounds;

public:
  QuadNode(Point*, Rect);
  ~QuadNode();
  void Insert(Point, int=0);
  int Count();
  void Sort();
  void Search(const Rect rect, const int32_t count, std::vector<int32_t>& results);
};
