# Leet Code 75


| #   | Problem Name                                                                                                | Solution                                    | Description                                                                                                                                                                                      |
|-----|-------------------------------------------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | [Two Sum](https://leetcode.com/problems/two-sum/)                                                           | [Solution](two-sum.py)                      | Use a hash map to keep track of seen numbers                                                                                                                                                     |
| 121 | [Best Time to Buy and Sell Stocks](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)          | [Solution](two-pointer.py)                  | Iterate over prices, if found lower price update buy date else keep searching for better profit                                                                                                  |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)                                     | [Solution](contains-duplicate.py)           | Compare len of array vs len of set; alternatively add elements to set if element already seen return true                                                                                        |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)                 | [Solution](product-of-array-except-self.py) | Calculate Prefix on one pass and then multiple with postfix on next pass                                                                                                                         |
| 53  | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                         | [Solution](max-subarray.py)                 | Iterate while keeping track of cur sum, if it is negative discard it then start cur sum again. Take maximum of cur sum and maximum sum seen so far                                               |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)                         | [Solution](max-product-subarray.py)         | Iterate while keeping a curmin and curmax, update it when seeing a number, negative x negative will update in max being updated                                                                  |
| 153 | [Find minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Solution](min-sorted-array.py)             | Set left to first element, right to last value, find middle. If middle is smaller than left than search left else search right                                                                   |
| 33  | [Search in rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/)             | [Solution](search-rotated-array.py)         | Use middle to find if you're in the left part of the sorted array or the right part, then update search area based on the middle value and the extreme value                                     |
| 15  | [3Sum](https://leetcode.com/problems/3sum/)                                                                 | [Solution](three-sum.py)                    | O(n2): Sort the array, Fix a starting point then look for left and right, if total > 0, move right inwards, else if target < 0, move left outwards, otherwise move to next fixed number          |
| 11  | [Container with Most Water](https://leetcode.com/problems/container-with-most-water/)                       | [Solution](water-container.py)              | Two pointer solution, start with extremes move whichever side is lower to  the opposite side                                                                                                     |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)                                         | [Solution](hamming-weight.py)               | Mod number with 2, then keep count, shift number using bit shift operator                                                                                                                        |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/)                                               | [Solution](counting-bits.py)                | Dynamic Programming, keep an offset (power of two) and for every number find significant digit and add 1 for that and resst is the same number of bits as number - offset, eg: 7 = 1 + same as 4 |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/)                                             | [Solution](missing-number.py)               | Subtract from sub of n numbers formula or xor with every number in that range                                                                                                                    |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                                 | [Solution](reverse-bits.py)                 | Iterate over length, find ith bit by doing and, shift that by n - i and or it with result                                                                                                        |
|     |                                                                                                             |                                             |                                                                                                                                                                                                  |
|     |                                                                                                             |                                             |                                                                                                                                                                                                  |
|     |                                                                                                             |                                             |                                                                                                                                                                                                  |
|     |                                                                                                             |                                             |                                                                                                                                                                                                  |
|     |                                                                                                             |                                             |                                                                                                                                                                                                  |
|     |                                                                                                             |                                             |                                                                                                                                                                                                  |
