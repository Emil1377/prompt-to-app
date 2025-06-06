import streamlit as st

st.title("Startup Pitch Deck Generator")

idea = st.text_input("💡 Enter your product idea:")
if idea:
    st.success("Generating 3-slide pitch deck...")

    st.markdown("## Slide 1: Problem & Opportunity")
    st.markdown(f"- People struggle with {idea.lower()}.")
    st.markdown("- Current solutions are inefficient or expensive.")
    st.markdown("- There’s a growing market for smarter tools.")

    st.markdown("## Slide 2: Our Solution")
    st.markdown(f"- We created **{idea}**, a modern way to solve that.")
    st.markdown("- Key features: simplicity, automation, accessibility.")
    st.markdown("- Early adopters love it.")

    st.markdown("## Slide 3: Vision & Call to Action")
    st.markdown("- Huge market potential")
    st.markdown("- Seeking early users, testers, or investors")
    st.markdown("- Let’s build it together 🚀")
