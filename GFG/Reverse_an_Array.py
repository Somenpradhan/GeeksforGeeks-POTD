# C

# void reverseArray(int arr[], int n) {
#     int left = 0, right = n - 1;

#     while (left < right) {
#         arr[left] ^= arr[right];
#         arr[right] ^= arr[left];
#         arr[left] ^= arr[right];
#         left++;
#         right--;
#     }
# }

# JAVA

# class Solution {
#     public void reverseArray(int[] arr) {
#         Integer[] boxedArray = Arrays.stream(arr).boxed().toArray(Integer[]::new);
#         List<Integer> list = Arrays.asList(boxedArray);
#         Collections.reverse(list);
#         for (int i = 0; i < arr.length; i++) {
#             arr[i] = list.get(i);
#         }
#     }
# }

# PYTHON

class Solution:
    def reverseArray(self, arr):
        arr.reverse()