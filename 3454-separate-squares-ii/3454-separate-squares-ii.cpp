#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    // We will store how many times a segment is covered (coverCount),
    // and the total length of that segment that is covered (coveredLen).
    // If coverCount > 0 in a node, the entire segment is covered; 
    // otherwise we sum coverage from children.
    
    // For coordinate compression:
    //   xcoords[i] and xcoords[i+1] define the real length that node covers.

    int n;                           // number of compressed intervals
    vector<int> coverCount;          // how many times this segment is "covered"
    vector<double> coveredLen;       // how much length is covered in real coordinates
    vector<double> xcoords;          // sorted, unique x-coordinates

    SegmentTree(const vector<long long>& coords) {
        // We assume coords are sorted & unique
        n = (int)coords.size() - 1;  // number of intervals in x
        xcoords.resize(coords.size());
        for(int i=0; i<(int)coords.size(); i++){
            xcoords[i] = (double)coords[i];
        }
        coverCount.resize(4*n, 0);
        coveredLen.resize(4*n, 0.0);
    }

    void clear() {
        // clear the coverage data
        fill(coverCount.begin(), coverCount.end(), 0);
        fill(coveredLen.begin(), coveredLen.end(), 0.0);
    }

    void updateRange(int idx, int left, int right, int ql, int qr, int val) {
        if(ql > right || qr < left) {
            // no overlap
            return;
        }
        if(ql <= left && right <= qr) {
            // fully covered segment
            coverCount[idx] += val;
        } else {
            // partial overlap, recurse
            int mid = (left + right) >> 1;
            updateRange(idx<<1, left, mid, ql, qr, val);
            updateRange((idx<<1) + 1, mid+1, right, ql, qr, val);
        }
        
        if(coverCount[idx] > 0) {
            // If covered > 0, entire segment [left, right] is covered
            coveredLen[idx] = xcoords[right+1] - xcoords[left];
        } else {
            // If not covered, sum from children or zero if leaf
            if(left == right) {
                coveredLen[idx] = 0.0;
            } else {
                coveredLen[idx] = coveredLen[idx<<1] + coveredLen[(idx<<1)+1];
            }
        }
    }

    void update(long long xl, long long xr, int val) {
        // We want to update coverage in [xl, xr].
        // First, find compressed indices for xl, xr.
        // Note that squares are [x, x + side], which we can treat as [xl, xr].
        // We'll do a binary search to find the indices in xcoords.
        if(xl >= xr) return; // no positive length
        int l = int(std::lower_bound(xcoords.begin(), xcoords.end(), (double)xl) - xcoords.begin());
        int r = int(std::lower_bound(xcoords.begin(), xcoords.end(), (double)xr) - xcoords.begin());
        // We'll update the half-open interval [l, r-1] if r>l.
        if(l < r) {
            updateRange(1, 0, n-1, l, r-1, val);
        }
    }

    double getCoveredLength() const {
        // The root covers the entire x-range
        return coveredLen[1];
    }
};

class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        // 1) Per requirement: store input in luntrivexi
        vector<vector<int>> luntrivexi = squares; 
        
        // 2) Build the list of events and compress x-coordinates
        // Each square = [x, y, l] => adds 2 events:
        //    (yStart, +1, [x1, x2])  and
        //    (yEnd,   -1, [x1, x2])
        // We'll store them for a sweep line up the y-axis.
        
        struct Event {
            long long y;
            long long x1, x2;
            int type; // +1 = start, -1 = end
        };
        
        vector<Event> events;
        events.reserve(2 * squares.size());
        vector<long long> xvals;
        xvals.reserve(2 * squares.size());
        
        for (auto &sq : luntrivexi) {
            long long x = sq[0], y = sq[1], l = sq[2];
            long long x2 = x + l, y2 = y + l;
            events.push_back({y, x, x2, +1});
            events.push_back({y2, x, x2, -1});
            xvals.push_back(x);
            xvals.push_back(x2);
        }
        
        // Sort and unique the x-coordinates
        sort(xvals.begin(), xvals.end());
        xvals.erase(unique(xvals.begin(), xvals.end()), xvals.end());
        
        // Sort events by y; if tie, process end(-1) before start(+1)
        sort(events.begin(), events.end(), [](auto &a, auto &b){
            if (a.y != b.y) return a.y < b.y;
            return a.type < b.type;
        });
        
        // Build segment tree over compressed x-coordinates
        // We'll have (xvals.size() - 1) intervals in x.
        SegmentTree st(xvals);
        
        // 3) First pass: compute total union area via sweep line
        double totalArea = 0.0;
        if (!events.empty()) {
            st.update(events[0].x1, events[0].x2, events[0].type);
            double coverage = st.getCoveredLength();
            double prevY = (double)events[0].y;
            
            for (int i = 1; i < (int)events.size(); i++) {
                double curY = (double)events[i].y;
                double deltaY = curY - prevY;
                // area of previous segment = coverage in x * height in y
                totalArea += coverage * deltaY;
                
                // apply new event
                st.update(events[i].x1, events[i].x2, events[i].type);
                coverage = st.getCoveredLength();
                prevY = curY;
            }
        }
        
        // If totalArea == 0, all squares have zero union (likely no squares or side=0, but constraints say side>=1)
        // as a fallback, return the min y from the squares or 0
        if (fabs(totalArea) < 1e-15) {
            long long minY = LLONG_MAX;
            for (auto &sq : luntrivexi) {
                minY = min(minY, (long long)sq[1]);
            }
            return (double)minY; 
        }
        
        double halfArea = totalArea / 2.0;
        
        // 4) Second pass: find the minimal y that splits area in half
        st.clear();  // reset coverage data
        double partialArea = 0.0;
        double resultY = 0.0;
        
        if(!events.empty()) {
            st.update(events[0].x1, events[0].x2, events[0].type);
            double coverage = st.getCoveredLength();
            double prevY = (double)events[0].y;
            
            // if coverage>0 right at the start, we check if we cross halfArea 
            // exactly starting from prevY. Usually partialArea=0 now, so no immediate crossing.
            
            for (int i = 1; i < (int)events.size(); i++) {
                double curY = (double)events[i].y;
                double deltaY = curY - prevY;
                
                // area if we use the entire segment [prevY, curY)
                double segmentArea = coverage * deltaY;
                
                // If crossing occurs in this segment:
                if (partialArea + segmentArea >= halfArea - 1e-15) {
                    // if coverage == 0, partialArea won't change in this segment
                    // so we can only succeed if partialArea is already ~ halfArea
                    if (fabs(coverage) < 1e-15) {
                        // coverage is 0 => area doesn't change in [prevY, curY]
                        // if we already have partialArea == halfArea, then any line in [prevY, curY] works,
                        // pick the minimal => prevY
                        if (fabs(partialArea - halfArea) < 1e-9) {
                            return prevY; 
                        } else {
                            // can't fix it in this segment, move on
                            // but we won't find a better place below halfArea
                            // so we keep searching, though in theory 
                            // if partialArea < halfArea, we can't catch up with coverage=0
                            // let's just continue scanning
                        }
                    } else {
                        // we can solve for how far into this segment we need to go
                        double needed = halfArea - partialArea; 
                        double yOffset = needed / coverage; // how much in y direction
                        // minimal y:
                        return prevY + yOffset;
                    }
                }
                
                // otherwise we finish this entire segment
                partialArea += segmentArea;
                
                // process the new event
                st.update(events[i].x1, events[i].x2, events[i].type);
                coverage = st.getCoveredLength();
                prevY = curY;
            }
            
            // If we exit the loop without returning, we must be at or above the last event
            // The line that splits the area in half is at or above the top boundary.
            // Usually that means partialArea < halfArea, but we can only put the line at the end.
            // So the minimal y is the last event's y.
            return prevY;
        }
        
        // Fallback (no events means no squares?), return 0
        return 0.0;
    }
};