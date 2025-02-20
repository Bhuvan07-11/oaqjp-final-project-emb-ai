"""
Emotion Detection API using Flask
"""

import sys
import os
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

# Add the project path to the Python path
project_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(project_path, '..'))

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in the given text.

    Returns a JSON response with emotion scores and the dominant emotion.
    """
    data = request.json
    text_to_analyze = data.get('text')
    
    if not text_to_analyze:
        return jsonify({'error': 'Invalid text! Please try again.'}), 400

    try:
        result = emotion_detector(text_to_analyze)
        
        # Debugging information
        print("Emotion detection result:", result)
        
        if result['dominant_emotion'] is None:
            return jsonify({'error': 'Invalid text! Please try again.'}), 400

        response = {
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness'],
            'dominant_emotion': result['dominant_emotion']
        }
        
        return jsonify(response)
    except KeyError as e:
        print("KeyError:", str(e))
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
