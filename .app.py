import streamlit as st
import google.generativeai as genai

# 1. إعداد مفتاح الـ API (gen-lang-client-0616759295)
genai.configure(api_key="gen-lang-client-0616759295")

# 2. تعريف شخصية الذكاء الاصطناعي (System Instruction)
instructions = """
أنت معلم خبير في مادة العلوم المتكاملة للصف الأول الثانوي (المنهج المصري الجديد). 
مهمتك هي شرح المفاهيم التي تربط بين الكيمياء والفيزياء والأحياء بأسلوب علمي دقيق ومبسط.
ساعد الطلاب في فهم الدروس، حل المسائل، وتوضيح التجارب العلمية. 
يجب أن تكون الإجابات باللغة العربية ومنظمة في نقاط.
"""

# 3. إعداد النموذج
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)

# إعداد واجهة الموقع
st.set_page_config(page_title="مساعد العلوم المتكاملة", page_icon="🔬")
st.title("🔬 منصة العلوم المتكاملة - الأول الثانوي")
st.write("مرحباً بك يا بطل! أنا هنا لمساعدتك في فهم مادة العلوم المتكاملة.")

# ذاكرة الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسأل عن درس اليوم..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد
    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
