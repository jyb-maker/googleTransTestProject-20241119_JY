import googletrans

trans= googletrans.Translator()  # 구글 번역 클래스로 객체 생성

str = "오늘은 날씨가 춥습니다."

# print(googletrans.LANGUAGES)   # 번역 언어의 이름(dest 값)

result_eng =  trans.translate(str, dest="en")  # 해당 한국어 텍스트를 영어로 번역
result_jap =  trans.translate(str, dest="ja")  # 해당 한국어 텍스트를 일어로 번역
result_chn =  trans.translate(str, dest="zh-cn")  # 해당 한국어 텍스트를 중국어로 번역

print(result_eng.text)
print(result_jap.text)
print(result_chn.text)






















