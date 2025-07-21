import cv2
from datetime import datetime
import geocoder

def get_location():
    try:
        g = geocoder.ip('me')
        if g.ok:
            return g.latlng  
        else:
            return ["Unknown", "Unknown"]
    except Exception as e:
        print("Error fetching location:", e)
        return ["Error", "Error"]

def scan_qr_with_opencv():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    print("Scanning for QR code. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if bbox is not None and data:
            print("\n📦 QR Code Detected!")
            print("QR Data:", data)

            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            print("🕒 Scanned At:", timestamp)

            lat, lng = get_location()
            print(f"📍 Location: Latitude = {lat}, Longitude = {lng}")

            for i in range(len(bbox)):
                cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), (255, 0, 0), 2)

            cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

scan_qr_with_opencv()
