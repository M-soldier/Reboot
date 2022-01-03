# -*- coding: utf-8 -*-
import threading
from library import nlp
from library import vad
from library import tts
from library import action
from library import client
from library import camera_mine
from library import emotion
from playsound import playsound


def play(file):
    playsound(file)


class MAIN(object):
    def __init__(self):
        emotion.stop_word()
        self.NLP = nlp.nlp()
        self.VAD = vad.vad()
        self.CLIENT = client.client("", "")
        self.CAMERA = camera_mine.camera()
        self.ACTION = action.action()
        self.text = ""
        self.text_people = ""

    def main(self):
        while True:
            get_out = self.VAD.Monitor_new()
            if get_out:
                print("自动退出")
                break
            text, text_people = self.NLP.get_text()
            if text is not None:
                if text_people.find("表情") == 1:
                    back = self.CAMERA.start()
                    if back == 0:
                        score = emotion.sentiment_score("您的表情是生气，不要生气哦，生气就不帅了喔")
                        TTS = tts.tts("您的表情是生气，不要生气哦，生气就不帅了喔")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 1:
                        score = emotion.sentiment_score("您的表情是厌恶，我有什么做的不对的吗，你为什么要这么看着我")
                        TTS = tts.tts("您的表情是厌恶，我有什么做的不对的吗，你为什么要这么看着我")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 2:
                        score = emotion.sentiment_score("您的表情是恐惧，不用害怕，有我在，我可以为你驱散恐惧")
                        TTS = tts.tts("您的表情是恐惧，不用害怕，有我在，我可以为你驱散恐惧")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 3:
                        score = emotion.sentiment_score("您的表情是高兴，你开心我也高兴，主人的笑脸是我最大的快乐")
                        TTS = tts.tts("您的表情是高兴，你开心我也高兴，主人的笑脸是我最大的快乐")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 4:
                        score = emotion.sentiment_score("您的表情是悲伤，不必遗憾，也不必惆怅，一切顺其自然，一切都会过去的")
                        TTS = tts.tts("您的表情是悲伤，不必遗憾，也不必惆怅，一切顺其自然，一切都会过去的")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 5:
                        score = emotion.sentiment_score("您的表情是惊讶，有什么值得惊讶的吗？也说给我听听呗")
                        TTS = tts.tts("您的表情是惊讶，有什么值得惊讶的吗？也说给我听听呗")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 6:
                        score = emotion.sentiment_score("您的表情是中立，你好严肃啊，笑一笑嘛")
                        TTS = tts.tts("您的表情是中立，你好严肃啊，笑一笑嘛")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                    if back == 7:
                        score = emotion.sentiment_score("您的摄像头出问题了，我暂时看不到你的表情呢")
                        TTS = tts.tts("您的摄像头出问题了，我暂时看不到你的表情呢")
                        TTS.text_to_speech()
                        self.choose_mode(score)
                else:
                    score = emotion.sentiment_score(text)
                    TTS = tts.tts(text)
                    TTS.text_to_speech()
                    self.choose_mode(score)

    def MAIN(self):
        while True:
            self.VAD.Monitor()
            self.CLIENT.file_path = "./data/record.wav"
            self.CLIENT.method = "judge_audio"
            judge = self.CLIENT.send()
            if judge == "True":
                text, text_people = self.NLP.get_text()
                if text is not None:
                    if text_people.find("表情") == 1:
                        back = self.CAMERA.start()
                        if back == 0:
                            score = emotion.sentiment_score("您的表情是生气，不要生气哦，生气就不帅了喔")
                            TTS = tts.tts("您的表情是生气，不要生气哦，生气就不帅了喔")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 1:
                            score = emotion.sentiment_score("您的表情是厌恶，我有什么做的不对的吗，你为什么要这么看着我")
                            TTS = tts.tts("您的表情是厌恶，我有什么做的不对的吗，你为什么要这么看着我")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 2:
                            score = emotion.sentiment_score("您的表情是恐惧，不用害怕，有我在，我可以为你驱散恐惧")
                            TTS = tts.tts("您的表情是恐惧，不用害怕，有我在，我可以为你驱散恐惧")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 3:
                            score = emotion.sentiment_score("您的表情是高兴，你开心我也高兴，主人的笑脸是我最大的快乐")
                            TTS = tts.tts("您的表情是高兴，你开心我也高兴，主人的笑脸是我最大的快乐")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 4:
                            score = emotion.sentiment_score("您的表情是悲伤，不必遗憾，也不必惆怅，一切顺其自然，一切都会过去的")
                            TTS = tts.tts("您的表情是悲伤，不必遗憾，也不必惆怅，一切顺其自然，一切都会过去的")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 5:
                            score = emotion.sentiment_score("您的表情是惊讶，有什么值得惊讶的吗？也说给我听听呗")
                            TTS = tts.tts("您的表情是惊讶，有什么值得惊讶的吗？也说给我听听呗")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 6:
                            score = emotion.sentiment_score("您的表情是中立，你好严肃啊，笑一笑嘛")
                            TTS = tts.tts("您的表情是中立，你好严肃啊，笑一笑嘛")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                        if back == 7:
                            score = emotion.sentiment_score("您的摄像头出问题了，我暂时看不到你的表情呢")
                            TTS = tts.tts("您的摄像头出问题了，我暂时看不到你的表情呢")
                            TTS.text_to_speech()
                            self.choose_mode(score)
                    else:
                        score = emotion.sentiment_score(text)
                        TTS = tts.tts(text)
                        TTS.text_to_speech()
                        self.choose_mode(score)
                self.main()

            if judge == "False":
                score = emotion.sentiment_score("您的语音信息不在语音库中，无法与我沟通我")
                TTS = tts.tts("您的语音信息不在语音库中，无法与我沟通我")
                TTS.text_to_speech()
                self.choose_mode(score)

    def choose_mode(self, score):
        if score >= 2:
            event_obj = threading.Event()
            event_obj.set()
            thread_1 = threading.Thread(target=self.ACTION.happy, args=(event_obj,))
            thread_1.start()
            thread_2 = threading.Thread(target=play, args=('./data/demo.mp3',))
            thread_2.start()
            thread_2.join()
            event_obj.clear()
            print("开心")
        elif score <= -2:
            event_obj = threading.Event()
            event_obj.set()
            thread_1 = threading.Thread(target=self.ACTION.sad, args=(event_obj,))
            thread_1.start()
            thread_2 = threading.Thread(target=play, args=('./data/demo.mp3',))
            thread_2.start()
            thread_2.join()
            event_obj.clear()
            print("悲伤")
        else:
            event_obj = threading.Event()
            event_obj.set()
            thread_1 = threading.Thread(target=self.ACTION.clam, args=(event_obj,))
            thread_1.start()
            thread_2 = threading.Thread(target=play, args=('./data/demo.mp3',))
            thread_2.start()
            thread_2.join()
            event_obj.clear()
            print("平静")


if __name__ == "__main__":
    pass
