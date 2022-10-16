from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

speak.Speak("Prashik chutiya hai, bohat bada hai wo ")
# import qrcode
# img = qrcode.make("https://www.youtube.com/")
# img.save("youtubeQR.jpg")
