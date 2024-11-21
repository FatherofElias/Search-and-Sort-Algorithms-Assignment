# Assignment 2 Task 2

from flask import Flask, jsonify

app = Flask(__name__)

# List of video titles
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

# Merge sort function
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

@app.route('/videos', methods=['GET'])
def get_sorted_videos():
    sorted_titles = merge_sort(video_titles)
    return jsonify(sorted_titles)

if __name__ == '__main__':
    app.run(debug=True)
