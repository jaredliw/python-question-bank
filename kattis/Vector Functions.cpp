// CPU: 0.03 s
#include "vectorfunctions.h"
#include <numeric>
#include <algorithm>

void backwards(std::vector<int>& vec){
    reverse(vec.begin(), vec.end());
}

std::vector<int> everyOther(const std::vector<int>& vec){
    std::vector<int> res;
    for (int i = 0; i < vec.size(); i += 2)
        res.push_back(vec[i]);
    return res;
}

int smallest(const std::vector<int>& vec){
    return *min_element(vec.begin(), vec.end());
}

int sum(const std::vector<int>& vec){
    return accumulate(vec.begin(), vec.end(), 0);
}

int veryOdd(const std::vector<int>& vec){
    int count = 0;
    for (int i = 1; i < vec.size(); i += 2) {
        if (vec[i] % 2 == 1)
            count++;
    }
    return count;
}
