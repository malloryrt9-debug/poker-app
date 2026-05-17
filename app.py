import streamlit as st

st.set_page_config(page_title="Mobile Poker AI", page_icon="♠️")
st.title("♠️ 9-Player Poker AI Advisor")

st.header("1. Table Situation")
position = st.selectbox("Your Position:", ["Early (Acts First)", "Middle", "Late (Button)", "Blinds"])
card1 = st.selectbox("First Card:", ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"])
card2 = st.selectbox("Second Card:", ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"])
suited = st.checkbox("Are they the same suit?")

st.subheader("Pot Odds")
pot = st.number_input("Current Pot Size ($):", min_value=0, value=100)
to_call = st.number_input("Amount to Call ($):", min_value=0, value=20)

st.header("🤖 AI Strategic Advice")
if st.button("Analyze Hand", use_container_width=True):
    is_pair = (card1 == card2)
    is_premium = card1 in ["A", "K", "Q"] and card2 in ["A", "K", "Q"]
    
    if to_call > 0:
        pot_odds = (to_call / (pot + to_call)) * 100
        st.metric("Your Pot Odds", f"{pot_odds:.1f}%")
    
    if is_pair and is_premium:
        st.success("🔥 MONSTER HAND: Raise or re-raise immediately!")
    elif is_premium or (is_pair and card1 in ["J", "10", "9"]):
        if position == "Early (Acts First)":
            st.warning("⚠️ STRONG HAND: Act carefully out of position. Standard raise.")
        else:
            st.success("✅ STRONG HAND: Play aggressively from late position. Raise!")
    elif suited and card1 in ["A", "K", "Q", "J"]:
        st.info("📈 SPECULATIVE HAND: Good flush potential. Call a small bet.")
    else:
        st.error("❌ WEAK HAND: Fold. This hand loses money against 9 players.")
