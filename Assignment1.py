# Task 1
def binary_search(video_titles, target):
    left, right = 0, len(video_titles) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = video_titles[mid]

        if mid_value == target:
            return mid  # Target found at index mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage:
video_titles = [
    "Artificial Intelligence Revolution",
    "Cooking Masterclass: Italian Cuisine",
    "Digital Photography Essentials",
    "Exploring the Cosmos",
    "Financial Planning for Beginners",
    "Fitness Fundamentals: Strength Training",
    "History Uncovered: Ancient Civilizations",
    "Nature's Wonders: National Geographic",
    "The Art of Coding",
    "Travel Diaries: Discovering Europe"
]

target_title = "Exploring the Cosmos"
index = binary_search(video_titles, target_title)

if index != -1:
    print(f"'{target_title}' found at index {index}.")
else:
    print(f"'{target_title}' not found in the video titles.")
