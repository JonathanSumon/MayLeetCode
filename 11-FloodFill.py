"""
An image is represented by a 2-D array of integers, each integer representing 
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) 
of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels 
connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those 
pixels (also with the same color as the starting pixel), and so on. 
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""
#Solution
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen = set()
        next_pixel = collections.deque()
        next_pixel.append((sr, sc))
        
        while next_pixel:
            pixel = next_pixel.popleft()
            
            if pixel in seen:
                continue
                
            seen.add(pixel)
            x, y = pixel
            pixel_color = image[x][y]
            
            if x > 0:
                if image[x-1][y] == pixel_color and (x-1, y):
                    next_pixel.append((x-1, y))
            if y > 0:
                if image[x][y-1] == pixel_color and (x, y-1):
                    next_pixel.append((x, y-1))
            if x < len(image) - 1:
                if image[x+1][y] == pixel_color and (x+1, y):
                    next_pixel.append((x+1, y))
            if y < len(image[0]) - 1:
                if image[x][y+1] == pixel_color and (x, y+1):
                    next_pixel.append((x, y+1))
            
            image[x][y] = newColor
            
        return image