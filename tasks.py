import webbrowser
import os
# Open Chrome or any website
def open_chrome():
    webbrowser.open("https://www.google.com")
    return "Opened Chrome for you!"

def open_website(url):
    webbrowser.open(url)
    return f"Opened {url} for you!"
def open_notepad():
    os.system("notepad")
    return "Notes Thane ok"
"""
# Open Camera
def open_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Cannot access the camera"
    print("Press 'q' to quit camera")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return "Camera closed"
"""
# Send WhatsApp message
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(number, message)
    return f"Sent message to {number}"
