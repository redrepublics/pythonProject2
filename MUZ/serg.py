from gtts import gTTS


test_params = "- Скажите, пожалуйста, куда мне отсюда идти? " \
              "Это во многом зависит от того, куда ты хочешь прийти, — ответил Кот." \
              "Да мне почти всё равно, — начала Алиса." \
              "Тогда всё равно, куда идти, — сказал Кот." \
              "Лишь бы попасть куда-нибудь, — пояснила Алиса." \
              "Не беспокойся, куда-нибудь ты обязательно попадешь, " \
              "— сказал Кот, — конечно, если не остановишься на полпути." \
              "Льюис Кэрролл, «Алиса в стране чудес»"

audio = "audio.mp3"
language = "ru"
sp = gTTS(text=test_params, lang=language, slow=False)
sp.save(audio)


