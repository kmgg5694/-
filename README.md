# - # [백춘황 성명학 웹 어플리케이션 프로젝트]

이 소스 코드는 대표님의 20년 내공을 스마트폰과 PC에서 구현하기 위한 웹 앱(Web App) 엔진입니다.

```python
import streamlit as st

# [설정] 화면 넓게 사용 및 제목 설정
st.set_page_config(page_title="백춘황 성명학 어플", layout="centered")

# [디자인] 상단 제목
st.title("📜 백춘황 원장 성명학 감명 시스템")
st.markdown("---")

# [입력] 이름 및 한자 획수 입력 (사주 제외, 성명학 집중)
st.subheader("👤 성함 및 획수 입력")
col1, col2 = st.columns(2)
with col1:
    name_kor = st.text_input("한글 성함", placeholder="예: 박지윤")
    s_w = st.number_input("성 한자 획수", min_value=1, value=7)
with col2:
    n1_w = st.number_input("이름1 한자 획수", min_value=1, value=4)
    n2_w = st.number_input("이름2 한자 획수", min_value=1, value=6)

# [로직] 8괘 및 주역괘 산출 함수
trigrams = {1: "천(天)", 2: "택(澤)", 3: "화(火)", 4: "뢰(雷)", 
            5: "풍(風)", 6: "수(水)", 7: "산(山)", 0: "지(地)"}

def get_tri(num):
    return trigrams[num % 8]

# [버튼] 감명 시작
if st.button("🚀 즉시 감명하기"):
    # 4격 수리 계산
    won = n1_w + n2_w      # 초년
    hyung = s_w + n1_w     # 장년
    lee = s_w + n2_w       # 중년
    jung = s_w + n1_w + n2_w # 총운

    st.markdown("### 📊 수리 및 주역괘 분석 결과")
    
    # 결과 테이블 구성
    res_col1, res_col2, res_col3, res_col4 = st.columns(4)
    with res_col1:
        st.info(f"**초년(원)**\n\n{won}획\n\n{get_tri(won)}")
    with res_col2:
        st.success(f"**장년(형)**\n\n{hyung}획\n\n{get_tri(hyung)}")
    with res_col3:
        st.warning(f"**중년(이)**\n\n{lee}획\n\n{get_tri(lee)}")
    with res_col4:
        st.error(f"**총운(정)**\n\n{jung}획\n\n{get_tri(jung)}")

    st.markdown("---")
    
    # 주역 동효 계산
    dong_hyo = jung % 6
    if dong_hyo == 0: dong_hyo = 6
    st.write(f"💡 **주역 동효:** {dong_hyo}효가 변함 (정격 기준)")

    # [핵심] 노트북LM 전달용 텍스트 자동 생성
    copy_text = f"""
    [감명 데이터]
    이름: {name_kor}
    수리: 원({won}), 형({hyung}), 이({lee}), 정({jung})
    주역: 상괘({get_tri(hyung)}), 하괘({get_tri(won)}/{get_tri(lee)}/{get_tri(jung)})
    동효: {dong_hyo}효 변함
    위 결과를 바탕으로 백춘황 원장님의 비전 자료에 따라 정밀 해설을 요청합니다.
    """
    
    st.text_area("📋 노트북LM 전달용 결과 (복사하세요)", value=copy_text, height=150)
    st.caption("위 박스 내용을 복사해서 노트북LM에 붙여넣으면 즉시 해설이 나옵니다.")

st.markdown("---")
st.caption("© 2026 백춘황 성명학 연구소 | 스마트폰 연동형 웹 프로젝트")
