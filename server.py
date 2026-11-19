from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    analyze_text = request.args.get('textToAnalyze')
    response = emotion_detector(analyze_text)
    if response['dominant_emotion'] is None:
        return {"message": "Invalid text! Please try again!."}

    return emotion_detector(analyze_text)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
