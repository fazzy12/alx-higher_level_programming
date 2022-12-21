#!/usr/bin/python3
def find_peak(list_of_integers):
    
"""Return a peak in a list of unsorted integers."""

if list_of_integers == []:
    return None

size = len(list_of_integers)
if size == 1:
    return list_of_integers[0]

# Divide the list into two halves
mid = size // 2
left = list_of_integers[:mid]
right = list_of_integers[mid:]

# Find the peak in the left and right halves
peak_left = find_peak(left)
peak_right = find_peak(right)

# Return the larger of the two peaks
return max(peak_left, peak_right)

