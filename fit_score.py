import numpy as np

def fit_taylor_curve(coords):
    # 좌표 분리
    x_vals = np.array([x for x, y in coords])
    y_vals = np.array([y for x, y in coords])

    # 중심화를 통해 x값 기준점 정렬 (x=0 기준 근사처럼 만들기)
    x_vals = x_vals - np.mean(x_vals)

    # 2차 다항식으로 근사 → 테일러 계수: a₂x² + a₁x + a₀
    coeffs = np.polyfit(x_vals, y_vals, 2)  # [a2, a1, a0]
    return coeffs[2], coeffs[1], coeffs[0]  # a0, a1, a2 순서로 반환

def calc_fit_score(user_coeffs, design_coeffs):
    a0_u, a1_u, a2_u = user_coeffs
    a0_d, a1_d, a2_d = design_coeffs

    error = 0
    for x in range(-5, 6):  # -5부터 5까지 11개 점에서 비교
        y_user = a0_u + a1_u * x + a2_u * x**2
        y_design = a0_d + a1_d * x + a2_d * x**2
        error += (y_user - y_design) ** 2

    score = max(0, 100 - error * 10)  # 오차가 클수록 점수 낮아짐
    return round(score, 1)
