from typing import List

# two-ptr technique in O(n) runtime and O(1) space
def max_area(height: List[int]) -> int:
    # two ptr approach with O(n) time and O(1) space
    l = 0
    r = len(height) - 1
    ans = min(height[l], height[r]) * (r - l) # track maximum water

    while l < r:
        # move whichever side is shorter (since moving the taller one will FOR SURE decrease the water as
        # the shorter stick determines the water height)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        
        # update the max water if possible
        new = min(height[l], height[r]) * (r - l)
        if new > ans:
            ans = new

    # out of the loop and we've explored all possibilities
    return ans

def main():
    height = [4,3,2,1,4]
    print(max_area(height))

if __name__ == '__main__':
    main()