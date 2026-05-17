import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test case class to verify the accuracy of emotion detection results."""

    def test_emotion_detector(self):
        """Tests multiple statements to ensure the expected dominant emotion

        matches the API output.
        """
        # 1. Prueba para Alegría (Joy) - "Me alegra que esto haya sucedido"
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")

        # 2. Prueba para Ira (Anger) - "Estoy realmente enojado por esto"
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")

        # 3. Prueba para Desagrado (Disgust) - "Me siento disgustado solo de escuchar sobre esto"
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")

        # 4. Prueba para Tristeza (Sadness) - "Estoy tan triste por esto"
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")

        # 5. Prueba para Miedo (Fear) - "Tengo mucho miedo de que esto suceda"
        result_5 = emotion_detector("I am really afraid of this happening")
        self.assertEqual(result_5["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()