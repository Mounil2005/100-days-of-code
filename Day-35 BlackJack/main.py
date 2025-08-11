import streamlit as st
import random
import time


st.set_page_config(
    page_title="🎰 Blackjack Game",
    page_icon="🃏",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .card-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        color: white;
        font-size: 1.2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .computer-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        color: white;
        font-size: 1.2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .game-result {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    .win {
        background-color: #28a745;
        color: white;
    }
    
    .lose {
        background-color: #dc3545;
        color: white;
    }
    
    .draw {
        background-color: #ffc107;
        color: black;
    }
    
    .stats-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #007bff;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def card_to_emoji(card_value):
    """Convert card values to emoji representations"""
    card_emojis = {
        11: "🅰️", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣",
        6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣", 10: "🔟"
    }
    return card_emojis.get(card_value, "🃏")

def display_cards(hand, show_emojis=True):
    """Display cards with emojis and values"""
    if show_emojis:
        emojis = " ".join([card_to_emoji(card) for card in hand])
        return f"{emojis} → {hand}"
    return str(hand)

def ace_adjust(hand):
    """Adjust ace values to prevent busting when possible"""
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

def is_blackjack(hand):
    """Check if hand is a blackjack (21 with 2 cards)"""
    return len(hand) == 2 and sum(hand) == 21 and (11 in hand or 1 in hand) and 10 in hand

def initialize_session_state():
    """Initialize session state variables"""
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'user_hand' not in st.session_state:
        st.session_state.user_hand = []
    if 'computer_hand' not in st.session_state:
        st.session_state.computer_hand = []
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'user_turn_over' not in st.session_state:
        st.session_state.user_turn_over = False
    if 'wins' not in st.session_state:
        st.session_state.wins = 0
    if 'losses' not in st.session_state:
        st.session_state.losses = 0
    if 'draws' not in st.session_state:
        st.session_state.draws = 0

def start_new_game():
    """Start a new game"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    st.session_state.user_hand = random.choices(cards, k=2)
    st.session_state.computer_hand = random.choices(cards, k=2)
    st.session_state.game_started = True
    st.session_state.game_over = False
    st.session_state.user_turn_over = False

def hit_card():
    """Add a card to user's hand"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    st.session_state.user_hand.extend(random.choices(cards, k=1))

def computer_turn():
    """Execute computer's turn"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_total = ace_adjust(st.session_state.computer_hand.copy())
    
    while computer_total < 17:
        st.session_state.computer_hand.extend(random.choices(cards, k=1))
        computer_total = ace_adjust(st.session_state.computer_hand.copy())
    
    st.session_state.game_over = True

def determine_winner():
    """Determine the winner and update stats"""
    user_total = ace_adjust(st.session_state.user_hand.copy())
    computer_total = ace_adjust(st.session_state.computer_hand.copy())
    
    user_bj = is_blackjack(st.session_state.user_hand)
    computer_bj = is_blackjack(st.session_state.computer_hand)
    
    if user_bj and computer_bj:
        st.session_state.draws += 1
        return "🤝 Both have Blackjack! It's a Draw!", "draw"
    elif user_bj:
        st.session_state.wins += 1
        return "🎉 Blackjack! You Win!", "win"
    elif computer_bj:
        st.session_state.losses += 1
        return "💻 Computer has Blackjack! Computer Wins!", "lose"
    elif user_total > 21:
        st.session_state.losses += 1
        return "💥 You Bust! Computer Wins!", "lose"
    elif computer_total > 21:
        st.session_state.wins += 1
        return "🎊 Computer Busts! You Win!", "win"
    elif user_total > computer_total:
        st.session_state.wins += 1
        return "🏆 You Win!", "win"
    elif computer_total > user_total:
        st.session_state.losses += 1
        return "🤖 Computer Wins!", "lose"
    else:
        st.session_state.draws += 1
        return "🤝 It's a Draw!", "draw"


initialize_session_state()


st.markdown('<h1 class="main-header">🎰 Blackjack Game 🃏</h1>', unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### 📊 Game Statistics")
    st.markdown(f"""
    <div class="stats-box">
        <strong>🏆 Wins:</strong> {st.session_state.wins}<br>
        <strong>❌ Losses:</strong> {st.session_state.losses}<br>
        <strong>🤝 Draws:</strong> {st.session_state.draws}<br>
        <strong>🎯 Total Games:</strong> {st.session_state.wins + st.session_state.losses + st.session_state.draws}
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.wins + st.session_state.losses + st.session_state.draws > 0:
        win_rate = (st.session_state.wins / (st.session_state.wins + st.session_state.losses + st.session_state.draws)) * 100
        st.markdown(f"**Win Rate:** {win_rate:.1f}%")


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if not st.session_state.game_started:
        if st.button("🎮 Start New Game", type="primary", use_container_width=True):
            start_new_game()
            st.rerun()
    else:
        if st.button("🔄 New Game", type="secondary", use_container_width=True):
            start_new_game()
            st.rerun()


if st.session_state.game_started:
    user_total = ace_adjust(st.session_state.user_hand.copy())
    computer_total = ace_adjust(st.session_state.computer_hand.copy())
    
    
    st.markdown("### 🤖 Computer's Hand")
    if not st.session_state.game_over and not st.session_state.user_turn_over:
        
        visible_card = st.session_state.computer_hand[0]
        st.markdown(f"""
        <div class="computer-card">
            {card_to_emoji(visible_card)} 🎴 → [{visible_card}, ?]<br>
            <strong>Visible Total: {visible_card if visible_card != 11 else 'A'}</strong>
        </div>
        """, unsafe_allow_html=True)
    else:
        
        computer_cards_display = display_cards(st.session_state.computer_hand)
        st.markdown(f"""
        <div class="computer-card">
            {computer_cards_display}<br>
            <strong>Total: {computer_total}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    
    st.markdown("### 👤 Your Hand")
    user_cards_display = display_cards(st.session_state.user_hand)
    st.markdown(f"""
    <div class="card-display">
        {user_cards_display}<br>
        <strong>Total: {user_total}</strong>
    </div>
    """, unsafe_allow_html=True)
    

    if not st.session_state.game_over and not st.session_state.user_turn_over:
        
        if is_blackjack(st.session_state.user_hand) or is_blackjack(st.session_state.computer_hand):
            st.session_state.user_turn_over = True
            computer_turn()
        elif user_total > 21:
            st.session_state.user_turn_over = True
            computer_turn()
        else:
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🃏 Hit (Take Card)", type="primary", use_container_width=True):
                    hit_card()
                    st.rerun()
            with col2:
                if st.button("✋ Stand", type="secondary", use_container_width=True):
                    st.session_state.user_turn_over = True
                    computer_turn()
                    st.rerun()
    
    
    if st.session_state.game_over:
        result_message, result_type = determine_winner()
        st.markdown(f'<div class="game-result {result_type}">{result_message}</div>', 
                   unsafe_allow_html=True)
        
        
        st.markdown("### 📋 Final Results")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"👤 **Your Total:** {user_total}")
        with col2:
            st.info(f"🤖 **Computer Total:** {computer_total}")


with st.expander("📖 How to Play Blackjack"):
    st.markdown("""
    **Objective:** Get as close to 21 as possible without going over (busting).
    
    **Card Values:**
    - Number cards (2-10): Face value
    - Face cards (J, Q, K): Worth 10 points
    - Ace: Worth 11 or 1 (whichever is better)
    
    **How to Win:**
    - Get closer to 21 than the dealer without busting
    - Get a "Blackjack" (21 with first 2 cards)
    - Dealer busts (goes over 21)
    
    **Dealer Rules:**
    - Dealer must hit on 16 or less
    - Dealer must stand on 17 or more
    
    **Controls:**
    - **Hit:** Take another card
    - **Stand:** Keep your current total
    """)


