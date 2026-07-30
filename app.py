import streamlit as st

st.set_page_config(page_title="Life Insurance Planning Tool", layout="centered")

st.title("Canadian Life Insurance Planning Tool")

st.warning(
    "⚠️ This is an educational student project. All figures are illustrative "
    "estimates and do NOT constitute real insurance quotes or professional advice. "
    "Please consult a licensed insurance advisor before making any decisions."
)

st.markdown("""
## Welcome

This platform helps you understand your life insurance planning options through
five interactive tools. Use the sidebar to navigate between them.

### What you can explore:

1. **Needs Calculator** — Estimate how much coverage you might need
2. **Recommendation** — See which product type fits your situation
3. **Premium Calculator** — Get an illustrative premium estimate
4. **Investment Projection** — Explore long-term investment growth scenarios
5. **Model Insights** — View the statistical analysis behind this tool

### Why this project exists

This tool is meant to help you understand insurance concepts and prepare
questions before speaking with a licensed advisor — not to replace one.

### Technology
Built with Python, Streamlit, and R (statistical analysis).
""")

st.caption("👈 Use the sidebar to get started.")