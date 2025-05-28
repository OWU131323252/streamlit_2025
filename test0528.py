import streamlit as st

st.title("第7回 Streamlit フォーム演習 - サークル入会申し込みフォーム")
st.caption("st.form を使ってサークル入会申し込みフォームを作成しましょう。")

st.markdown("---")
st.subheader("演習: サークル入会申し込みフォーム")
st.write("**課題**: フォームを使って、サークル入会の申し込み情報をまとめて処理するアプリを作成する。")

# フォームの作成
with st.form("サークル入会申込フォーム"):
    # 基本情報の入力欄
    name = st.text_input("お名前")
    grade = st.selectbox("学年", ["1年生", "2年生", "3年生", "4年生"])
    favorite_activity = st.selectbox("好きな活動", ["文化祭", "合宿", "勉強会", "交流会"])
    motivation = st.text_area("意気込み")
    
    # 送信ボタン
    submitted = st.form_submit_button("申し込む")
    
    if submitted:
        # 入力された情報をまとめて表示
        st.success("申し込みが完了しました！以下の情報が送信されました:")
        st.write(f"**お名前:** {name}")
        st.write(f"**学年:** {grade}")
        st.write(f"**好きな活動:** {favorite_activity}")
        st.write(f"**意気込み:** {motivation}")

st.markdown("---")
st.info("💡 全ての項目を入力してから「申し込む」ボタンを押すと、まとめて処理されることを確認してください。")
