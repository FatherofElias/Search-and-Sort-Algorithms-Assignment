# Assigment 1 Task 2

from flask import Flask, request, jsonify

app = Flask(__name__)

# List of video titles
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

# Binary search function
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

@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query', '')
    index = binary_search(video_titles, query)

    if index != -1:
        result = {
            'status': 'success',
            'video_title': video_titles[index],
            'index': index
        }
    else:
        result = {
            'status': 'not found',
            'message': f"Video titled '{query}' not found."
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
