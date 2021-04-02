#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;
long long MaxPairwiseProduct(const vector<int> &numbers) //naive solution
{
    long long max_product = 0;
    int n = numbers.size();
    for (int first = 0; first < n; ++first) //quadratic complexity
    {
        for (int second = first + 1; second < n; ++second)
        {
            long long res = (long long)numbers[first] * (long long)numbers[second];
            if (res > max_product)
            {
                max_product = res;
            }
        }
    }
    return max_product;
}
long long MaxPairwiseProductFast(const vector<int> &numbers) //fast solution
{
    int n = numbers.size();
    int firstIndex = -1, secondIndex = -1;
    for (int i = 0; i < n; ++i)
    {
        if (firstIndex == -1 || numbers[firstIndex] < numbers[i])
        {
            firstIndex = i;
        }
    }

    for (int i = 0; i < n; ++i)
    {
        if (i != firstIndex && (secondIndex == -1 || numbers[secondIndex] < numbers[i]))
        {
            secondIndex = i;
        }
    }
    //cout << firstIndex << ' ' << secondIndex << endl;
    return (long long)numbers[firstIndex] * (long long)numbers[secondIndex];
}

void stressTest() //compile with: g++ -pipe -O2 -std=c++11 max_pairwise_product.cpp -o stress_test
{
    //Stress test: infinitely generate random input and test all solution we implement until some bad stuff occur
    //Test with naive algorithm(slow+suck) to make sure the test is reliable
    while (true)
    {
        //rand() without seed will always produce the same result
        int n = rand() % 1000 + 2; //generate number of elements to input(small number to make it fast)
        cout << n << endl;
        vector<int> a;
        for (int i = 0; i < n; i++) //push_back random number to Vector
        {
            a.push_back(rand() % 100000);
        }
        for (int i = 0; i < n; i++)
        {
            cout << a[i] << ' '; //show each random number
        }
        cout << endl;
        long long res1 = MaxPairwiseProduct(a);
        long long res2 = MaxPairwiseProductFast(a);
        if (res1 != res2) //'assert' solution result
        {
            cout << "Wrong answer: " << res1 << ' ' << res2 << endl;
            break;
        }
        else
        {
            cout << "OK\n";
        }
    }
}

int main()
{
    //stressTest();
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> numbers[i];
    }

    cout << MaxPairwiseProductFast(numbers) << endl;
    return 0;
}
