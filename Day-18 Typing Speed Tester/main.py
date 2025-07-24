import streamlit as st
from streamlit_ace import st_ace
import time
import random

quotes = [
    "The quick brown fox jumps over the lazy dog.",
    "Discipline is the bridge between goals and success.", 
    "Typing is a fundamental skill for productivity and speed.",
    "Python is a great language for developing applications rapidly.",
    "Simplicity is the soul of efficiency in design and development.",
    "Artificial intelligence is the new electricity in the world of tech.",
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

def generate_quote():
    return " ".join(random.sample(quotes, 2))

def highlight_text(original, typed):
    html = ""
    for i, char in enumerate(original):
        if i < len(typed):
            if typed[i] == char:
                
                html += f'<span style="color: #22c55e; background-color: #dcfce7; font-weight: bold;">{char}</span>'
            else:
                 
                html += f'<span style="color: #ef4444; background-color: #fecaca; font-weight: bold;">{char}</span>'
        else:
            
            html += f'<span style="color: #1f2937; background-color: #f9fafb;">{char}</span>'
    return html

def calculate_stats(original, typed, elapsed_time):
    if elapsed_time <= 0:
        return 0, 0, 0
    
    mistakes = 0
    correct_chars = 0
    
    
    min_len = min(len(original), len(typed))
    for i in range(min_len):
        if typed[i] == original[i]:
            correct_chars += 1
        else:
            mistakes += 1
    
    
    if len(typed) > len(original):
        mistakes += len(typed) - len(original)
    
    words_typed = len(typed.split())
    wpm = (words_typed / (elapsed_time / 60)) if elapsed_time > 0 else 0
    
   
    accuracy = (correct_chars / len(typed)) * 100 if len(typed) > 0 else 100
    
    return wpm, accuracy, mistakes


st.set_page_config(page_title="Typing Speed Tester", page_icon="⌨️", layout="centered")


if 'quote' not in st.session_state:
    st.session_state.quote = generate_quote()
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'time_limit' not in st.session_state:
    st.session_state.time_limit = 60
if 'completed' not in st.session_state:
    st.session_state.completed = False


st.title("⌨️ Real-Time Typing Speed Tester")


time_limit = st.selectbox("Select Duration", [15, 30, 60], index=2)
st.session_state.time_limit = time_limit


st.markdown("""
<h3 style='color: #ffffff; background: #1f2937; padding: 10px; border-radius: 8px; margin: 10px 0;'>
    📝 Type the text below:
</h3>
""", unsafe_allow_html=True)

quote_display = f"""
<div style='
    background: #ffffff;
    color: #1f2937;
    padding: 20px;
    border-radius: 12px;
    font-family: "Consolas", "Monaco", monospace;
    font-size: 18px;
    line-height: 1.6;
    border: 2px solid #3b82f6;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin: 10px 0;
'>
    {highlight_text(st.session_state.quote, "")}
</div>
"""
st.markdown(quote_display, unsafe_allow_html=True)


st.markdown("""
<h3 style='color: #ffffff; background: #1f2937; padding: 10px; border-radius: 8px; margin: 10px 0;'>
    ✍️ Start typing here:
</h3>
""", unsafe_allow_html=True)

typed_text = st_ace(
    value="",
    language='text',
    theme='github',  
    key="ace_editor",
    height=150,
    auto_update=True,
    font_size=16,
    wrap=True,
    show_gutter=True,
    show_print_margin=False
)


if typed_text and not st.session_state.timer_running and not st.session_state.completed:
    st.session_state.start_time = time.time()
    st.session_state.timer_running = True


elapsed_time = 0
if st.session_state.start_time:
    elapsed_time = time.time() - st.session_state.start_time


if st.session_state.timer_running and elapsed_time >= st.session_state.time_limit:
    st.session_state.timer_running = False
    st.session_state.completed = True


if typed_text.strip() == st.session_state.quote.strip() and typed_text.strip():
    st.session_state.completed = True
    st.session_state.timer_running = False
    st.balloons()


if typed_text:
    updated_quote_display = f"""
    <div style='
        background: #ffffff;
        color: #1f2937;
        padding: 20px;
        border-radius: 12px;
        font-family: "Consolas", "Monaco", monospace;
        font-size: 18px;
        line-height: 1.6;
        border: 2px solid #3b82f6;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
    '>
        {highlight_text(st.session_state.quote, typed_text)}
    </div>
    """
    
    st.markdown("### 📝 Type the text below:")
    st.markdown(updated_quote_display, unsafe_allow_html=True)


remaining_time = max(0, st.session_state.time_limit - elapsed_time)
if st.session_state.timer_running:
    timer_color = "#ef4444" if remaining_time <= 10 else "#22c55e"
    st.markdown(f'''
    <div style="
        background: {timer_color};
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
    ">
        ⏱️ Time: {int(remaining_time)}s
    </div>
    ''', unsafe_allow_html=True)
elif st.session_state.completed:
    st.markdown('''
    <div style="
        background: #8b5cf6;
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
    ">
        🎉 Completed!
    </div>
    ''', unsafe_allow_html=True)
else:
    st.markdown(f'''
    <div style="
        background: #6b7280;
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 20px;
        margin: 20px 0;
    ">
        ⏱️ Ready: {st.session_state.time_limit}s
    </div>
    ''', unsafe_allow_html=True)


wpm, accuracy, mistakes = calculate_stats(st.session_state.quote, typed_text, elapsed_time)

st.markdown("""
<h3 style='color: #ffffff; background: #1f2937; padding: 10px; border-radius: 8px; margin: 10px 0;'>
    📊 Live Statistics
</h3>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'''
    <div style="background: #dbeafe; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #3b82f6;">
        <h3 style="color: #1e40af; margin: 0;">🚀 WPM</h3>
        <h2 style="color: #1e40af; margin: 10px 0;">{wpm:.1f}</h2>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div style="background: #dcfce7; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #22c55e;">
        <h3 style="color: #166534; margin: 0;">🎯 Accuracy</h3>
        <h2 style="color: #166534; margin: 10px 0;">{accuracy:.1f}%</h2>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div style="background: #fecaca; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ef4444;">
        <h3 style="color: #991b1b; margin: 0;">❌ Mistakes</h3>
        <h2 style="color: #991b1b; margin: 10px 0;">{mistakes}</h2>
    </div>
    ''', unsafe_allow_html=True)


if len(st.session_state.quote) > 0:
    progress = min(len(typed_text) / len(st.session_state.quote), 1.0)
    st.progress(progress, text=f"Progress: {progress*100:.1f}% complete")


st.markdown("---")
if st.button("🔄 Reset", use_container_width=True, type="primary"):
    st.session_state.quote = generate_quote()
    st.session_state.start_time = None
    st.session_state.timer_running = False
    st.session_state.completed = False
    st.rerun()


if st.session_state.timer_running:
    time.sleep(0.5)
    st.rerun()


st.markdown("""
<style>
    /* Ensure all text is readable */
    .stMarkdown {
        color: #1f2937 !important;
    }
    
    /* Fix any remaining contrast issues */
    .stSelectbox label {
        color: #1f2937 !important;
    }
    
    /* Ensure buttons are visible */
    .stButton button {
        background-color: #3b82f6 !important;
        color: white !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)
