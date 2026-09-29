python
import streamlit as st
import math

# -----------------------------------------
# 화면 설정
# -----------------------------------------

st.set_page_config(
    page_title="모임 회비 계산기",
    page_icon="💰",
    layout="centered"
)

# -----------------------------------------
# 글씨 크게 설정
# -----------------------------------------

st.markdown("""
<style>
    .큰제목 {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 35px;
    }

    .설명 {
        font-size: 22px;
        text-align: center;
        line-height: 1.8;
        margin-bottom: 30px;
    }

    .stNumberInput label {
        font-size: 24px !important;
        font-weight: bold !important;
    }

    .stNumberInput input {
        font-size: 24px !important;
        padding: 15px !important;
    }

    .stButton button {
        font-size: 26px !important;
        font-weight: bold !important;
        padding: 15px !important;
        width: 100%;
    }

    .결과제목 {
        font-size: 25px;
        font-weight: bold;
        text-align: center;
        margin-top: 35px;
    }

    .회비 {
        font-size: 52px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0 30px 0;
    }

    .총액 {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        line-height: 1.8;
    }

    .안내 {
        font-size: 25px;
        font-weight: bold;
        text-align: center;
        line-height: 1.8;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# 제목
# -----------------------------------------

st.markdown(
    '<div class="큰제목">💰 모임 회비 계산기</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="설명">모임에서 쓴 돈과 사람 수를 입력하면<br>한 사람이 낼 회비를 계산해 드립니다.</div>',
    unsafe_allow_html=True
)


# -----------------------------------------
# 전체 쓴 돈 입력
# -----------------------------------------

전체금액 = st.number_input(
    "전체 쓴 돈",
    min_value=0,
    value=0,
    step=1000,
    format="%d"
)


# -----------------------------------------
# 사람 수 입력
# -----------------------------------------

사람수 = st.number_input(
    "사람 수",
    min_value=0,
    value=0,
    step=1,
    format="%d"
)


# -----------------------------------------
# 계산하기 버튼
# -----------------------------------------

if st.button("계산하기"):

    # 사람 수가 0인 경우
    if 사람수 == 0:

        st.markdown(
            '<div class="안내">사람 수를 1명 이상 입력해 주세요.</div>',
            unsafe_allow_html=True
        )

    else:

        # -----------------------------------------
        # 한 사람당 회비 계산
        # -----------------------------------------

        # 사람당 금액을 계산한 뒤
        # 100원 단위로 올림
        한사람금액 = math.ceil(
            전체금액 / 사람수 / 100
        ) * 100

        # 실제로 걷게 되는 총액
        실제총액 = 한사람금액 * 사람수

        # 천 단위 쉼표 표시
        한사람금액표시 = f"{한사람금액:,}원"
        실제총액표시 = f"{실제총액:,}원"

        # -----------------------------------------
        # 결과 표시
        # -----------------------------------------

        st.markdown(
            '<div class="결과제목">한 사람당 회비</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="회비">{한사람금액표시}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div class="총액">
            실제로 걷게 되는 총액<br>
            {실제총액표시}
            </div>
            ''',
            unsafe_allow_html=True
        )

