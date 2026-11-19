from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        testcase1=emotion_detector("I am glad this happened")
        testcase2=emotion_detector("I am really mad about this")
        testcase3=emotion_detector("I feel disgusted just hearing about this")
        testcase4=emotion_detector("I am so sad about this")
        testcase5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(testcase1['dominant_emotion'],'joy')
        self.assertEqual(testcase2['dominant_emotion'],'anger')
        self.assertEqual(testcase3['dominant_emotion'],'disgust')
        self.assertEqual(testcase4['dominant_emotion'],'sadness')
        self.assertEqual(testcase5['dominant_emotion'],'fear')
if __name__ == '__main__':
    unittest.main()