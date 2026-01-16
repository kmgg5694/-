import streamlit as st

# [설정] 웹 및 모바일 화면 최적화
st.set_page_config(page_title="백춘황 성명학 어플", layout="centered")

# [디자인] 제목 및 설명
st.title("📜 백춘황 원장 성명학 시스템")
st.markdown("---")

# [입력] 성함 및 획수 입력부
st.subheader("👤 성함 및 획수 입력")
col1, col2 = st.columns(2)
with col1:
    name_kor = st.text_input("한글 성함", placeholder="예: 박지윤")
    s_w = st.number_input("성(姓) 한자 획수", min_value=1, value=7)
with col2:
    n1_w = st.number_input("이름1 한자 획수", min_value=1, value=4)
    n2_w = st.number_input("이름2 한자 획수", min_value=1, value=6)

# [로직] 8괘 및 주역괘 산출 데이터 (대표님 비전 방식)
# 8괘 순서: 1천, 2택, 3화, 4뢰, 5풍, 6수, 7산, 8지
trigrams = {1: "천(天)", 2: "택(澤)", 3: "화(火)", 4: "뢰(雷)", 
            5: "풍(風)", 6: "수(水)", 7: "산(山)", 0: "지(地)"}

def get_tri(num):
    return trigrams[num % 8]

# [실행] 감명 버튼
if st.button("🚀 즉시 감명하기"):
    # 4격 수리 계산 로직
    won = n1_w + n2_w      # 초년 (이름1 + 이름2)
    hyung = s_w + n1_w     # 장년 (성 + 이름1)
    lee = s_w + n2_w       # 중년 (성 + 이름2)
    jung = s_w + n1_w + n2_w # 총운 (전체 합)

    st.markdown("### 📊 분석 결과")
    
    # 모바일(스마트폰)에서 보기 좋게 2칸씩 배치
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.success(f"**초년(원):** {won}획 / {get_tri(won)}")
        st.info(f"**장년(형):** {hyung}획 / {get_tri(hyung)}")
    with res_col2:
        st.warning(f"**중년(이):** {lee}획 / {get_tri(lee)}")
        st.error(f"**총운(정):** {jung}획 / {get_tri(jung)}")

    st.markdown("---")
    
    # 주역 동효 (정격 기준 6으로 나눈 나머지)
    dong_hyo = jung % 6
    if dong_hyo == 0: dong_hyo = 6
    st.write(f"💡 **주역 동효:** {dong_hyo}효 변함")

    # [핵심] 노트북LM에 바로 붙여넣을 수 있는 텍스트 생성
    copy_text = f"""
[성명학 감명 데이터 보고서]
성함: {name_kor}
수리: 원({won}), 형({hyung}), 이({lee}), 정({jung})
주역 상괘: {get_tri(hyung)}
주역 하괘: {get_tri(won)} / {get_tri(lee)} / {get_tri(jung)}
동효: {dong_hyo}효 변함

이 결과를 바탕으로 백춘황 원장님의 성명학 바이블 소스에 근거하여 상세 해설을 작성해줘.
    """
    
    # 스마트폰에서 꾹 눌러 복사하기 편하게 텍스트 상자 제공
    st.text_area("📋 아래 내용을 복사해서 노트북LM에 붙여넣으세요", value=copy_text, height=200)

st.markdown("---")
st.caption("© 2026 백춘황 성명학 연구소 | 폰 연동형 웹 앱 프로젝트")
