import googletrans

while True:
    str = input("번역할 문장을 입력하세요(q를 입력하면 종료):")

    if str == "q":
        break

    trans= googletrans.Translator()  # 구글 번역 클래스로 객체 생성
    result_eng =  trans.translate(str, dest="en")  # 해당 한국어 텍스트를 영어로 번역
    result_jap =  trans.translate(str, dest="ja")  # 해당 한국어 텍스트를 일어로 번역
    result_chn =  trans.translate(str, dest="zh-cn")  # 해당 한국어 텍스트를 중국어로 번역

    print(f"{str}->영어: {result_eng.text}")
    print(f"{str}->일본어: {result_jap.text}")
    print(f"{str}->중국어: {result_chn.text}")
    print(f"========================================")



























