import cv2
import streamlit as st

st.title("📷 빗물받이 촬영 가이드")

cap = cv2.VideoCapture(0)
frame_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.error("❌ 웹캠을 열 수 없습니다.")
        break

    # 중앙 초록 박스
    h, w = frame.shape[:2]
    box_w, box_h = w // 2, h // 2
    x1, y1 = w // 2 - box_w // 4, h // 2 - box_h // 4
    x2, y2 = w // 2 + box_w // 4, h // 2 + box_h // 4
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    frame_placeholder.image(frame, channels="BGR")

cap.release()
