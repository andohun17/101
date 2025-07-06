import streamlit as st
from webcam_face import get_face_curve_points
from fit_score import fit_taylor_curve, calc_fit_score

st.set_page_config(page_title="테일러 급수 기반 얼굴-악세사리 적합도 평가")

st.title("👓 테일러 급수 기반 얼굴-악세사리 적합도 평가 웹앱")
st.write("웹캠으로 얼굴 곡선을 측정하고, 악세사리 곡선과의 적합도를 평가해보세요!")

# 1단계: 얼굴 좌표 측정
if st.button("1단계: 웹캠으로 얼굴 곡선 측정 시작"):
    coords = get_face_curve_points()
    if coords:
        a0, a1, a2 = fit_taylor_curve(coords)
        st.success(f"✅ 측정 완료! 사용자 얼굴 곡선의 테일러 계수:\n- a₀ = {a0:.3f}\n- a₁ = {a1:.3f}\n- a₂ = {a2:.3f}")

        # 2단계: 디자인 곡선 입력
        st.subheader("2단계: 악세사리 곡선 계수 입력")
        a0_d = st.number_input("디자인 곡선 a₀", value=5.0)
        a1_d = st.number_input("디자인 곡선 a₁", value=0.3)
        a2_d = st.number_input("디자인 곡선 a₂", value=-0.05)

        # 3단계: 적합도 평가
        if st.button("3단계: 적합도 계산"):
            score = calc_fit_score([a0, a1, a2], [a0_d, a1_d, a2_d])
            st.metric("적합도 점수", f"{score}점")
    else:
        st.error("❌ 얼굴을 인식하지 못했습니다. 다시 시도해 주세요.")
