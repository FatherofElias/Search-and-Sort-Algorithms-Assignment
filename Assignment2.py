# Task 2

def merge_sort(video_titles):
    if len(video_titles) <= 1:
        return video_titles

    mid = len(video_titles) // 2
    left_half = video_titles[:mid]
    right_half = video_titles[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list

# Example usage:
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

sorted_titles = merge_sort(video_titles)
print("Sorted video titles:")
for title in sorted_titles:
    print(title)
