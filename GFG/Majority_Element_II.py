#  C

# int* findMajority(int arr[], int n, int* resultSize) {
#     int num1 = -1, num2 = -1, c1 = 0, c2 = 0;
#     for (int i = 0; i < n; i++) {
#         if (arr[i] == num1) {
#             c1++;
#         } else if (arr[i] == num2) {
#             c2++;
#         } else if (c1 == 0) {
#             num1 = arr[i];
#             c1 = 1;
#         } else if (c2 == 0) {
#             num2 = arr[i];
#             c2 = 1;
#         } else {
#             c1--;
#             c2--;
#         }
#     }
#     c1 = c2 = 0;
#     for (int i = 0; i < n; i++) {
#         if (arr[i] == num1) c1++;
#         else if (arr[i] == num2) c2++;
#     }
#     int* result = (int*)malloc(2 * sizeof(int));
#     *resultSize = 0;
#     if (c1 > n / 3) result[(*resultSize)++] = num1;
#     if (c2 > n / 3) result[(*resultSize)++] = num2;
#     if (*resultSize == 2 && result[0] > result[1]) {
#         int temp = result[1];
#         result[1] = result[0];
#         result[0] = temp;
#     }

#     return result;
# }

#  JAVA

# class Solution {
#     public List<Integer> findMajority(int[] nums) {
#         int num1 = Integer.MIN_VALUE, num2 = Integer.MIN_VALUE, c1 = 0, c2 = 0;
#         int n = nums.length;
#         for (int x : nums) {
#             if (x == num1) {
#                 c1++;
#             } else if (x == num2) {
#                 c2++;
#             } else if (c1 == 0) {
#                 num1 = x;
#                 c1 = 1;
#             } else if (c2 == 0) {
#                 num2 = x;
#                 c2 = 1;
#             } else {
#                 c1--;
#                 c2--;
#             }
#         }
#         c1 = c2 = 0;
#         for (int x : nums) {
#             if (x == num1) c1++;
#             else if (x == num2) c2++;
#         }
#         List<Integer> res = new ArrayList<>();
#         if (c1 > n / 3) res.add(num1);
#         if (c2 > n / 3) res.add(num2);
#         Collections.sort(res);
#         return res;
#     }
# }


# PYTHON

class Solution:
    def findMajority(self, arr):
        num1, num2, c1, c2 = None, None, 0, 0
        n = len(arr)
        for x in arr:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
            elif c1 == 0:
                num1 = x
                c1 = 1
            elif c2 == 0:
                num2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for x in arr:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
        res = []
        if c1 > n // 3:
            res.append(num1)
        if c2 > n // 3:
            res.append(num2)
        res.sort()
        return res