import streamlit as st
from transmutation_engine import Transmutator

st.set_page_config(page_title="Transmutation Engine Classic", layout="wide")
st.title("🔥 Transmutation Engine Classic")
st.markdown("**Offline • Entropy = Chaos • Stabilization = Truth**")

col1, col2, col3 = st.columns(3)
cycles = col1.slider("Cycles", 1, 5, 5)
entropy = col2.slider("Entropy (Heat)", 0.1, 1.5, 1.5, 0.1)
stabilization = col3.slider("Stabilization (Cool)", 0.1, 0.8, 0.3, 0.1)

source_anchor = st.text_area(
    "Source Anchor (Prompt)",
    height=300,
    value="""You are the world's greatest explorer of self-descriptive English sentences.

Rules (strict, no exceptions):
- Input string contains only lowercase a-z and spaces
- It must contain phrases like "one a", "two b", "three c", ..., "ten z"
- Every letter that appears anywhere (including inside number words) must be exactly counted
- Order doesn't matter
- Use only: one, two, three, four, five, six, seven, eight, nine, ten

Task: Find a new valid strict autogram under 200 characters. Prove with exact counts."""
)

if st.button("🚀 Transmute"):
    with st.spinner("Running transmutation cycles..."):
        engine = Transmutator(cycles=cycles, entropy=entropy, stabilization=stabilization)
        report = engine.run_transmutation(source_anchor)

        st.subheader("Final Evolution")
        st.code(report["final"], language="text")

        # Auto-validator for autograms
        if any(word in report["final"].lower() for word in ["one", "two", "three", "four", "five"]):
            st.subheader("Autogram Validator")
            result = engine.validate_autogram(report["final"])
            st.write("**Valid?**", "✅ Yes" if result["valid"] else "❌ No")
            st.table(result["report"])
