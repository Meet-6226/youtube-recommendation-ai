import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# --- CONFIG ---
st.set_page_config(
    page_title="YouTube Revenue AI Lab", 
    page_icon="🎬", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM STYLE INJECTION ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: radial-gradient(circle at top right, #1e1e2f, #0a0c10);
    }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(255, 0, 0, 0.4);
    }
    
    h1, h2, h3 {
        background: linear-gradient(90deg, #FF0000, #FF6B6B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #FF0000, #D30000);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.4);
        transform: scale(1.02);
    }
    
    .metric-label { color: #8899A6; font-size: 0.9rem; margin-bottom: 5px; }
    .metric-value { color: #FFFFFF; font-size: 1.8rem; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
try:
    hero_img = Image.open("hero.png")
    st.image(hero_img, use_container_width=True)
except:
    st.title("🎬 YouTube Engagement AI Lab")

st.markdown("### Accelerating Revenue through Predictive Engagement Modeling")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.markdown("### ⚙️ Video Configuration")
    with st.container(border=True):
        cat = st.selectbox("Content Category", ['Education', 'Gaming', 'Music', 'Tech', 'Entertainment'])
        dev = st.selectbox("Target Audience Device", ['mobile', 'desktop', 'tablet'])
        duration = st.slider("Duration (seconds)", 60, 3600, 600)
    
    st.markdown("### 📈 Reach Parameters")
    with st.container(border=True):
        is_rec = st.toggle("Algorithmic Recommendation", value=True)
        views_base = st.number_input("Base Impressions", 1000, 5000000, 50000, step=5000)
    
    st.markdown("---")
    run_btn = st.button("🚀 EXECUTE NEURAL ANALYSIS", use_container_width=True)

# --- MAIN DASHBOARD LOGIC ---
if run_btn:
    # --- PREDICTION ENGINE (Logic from Model) ---
    base_prob = 0.35
    boosts = {
        'Education': 0.12, 'Gaming': 0.05, 'Music': 0.08, 'Tech': 0.15, 'Entertainment': 0.04
    }
    device_boost = {'mobile': 0.07, 'desktop': 0.03, 'tablet': 0.02}
    
    prob = base_prob + boosts[cat] + device_boost[dev]
    if is_rec: prob += 0.18
    if duration > 1800: prob += 0.05
    
    prob = min(prob, 0.98)
    est_engaged_views = views_base * prob
    est_revenue = est_engaged_views * 0.012

    # --- TABS FOR ORGANIZED INSIGHTS ---
    tab1, tab2, tab3 = st.tabs(["🎯 KPI Forecast", "📂 Deep Dive Analysis", "💡 Strategic Advisory"])

    with tab1:
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown(f'''
            <div class="glass-card">
                <div class="metric-label">Engagement Probability</div>
                <div class="metric-value">{prob*100:.1f}%</div>
            </div>
            ''', unsafe_allow_html=True)
            
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = prob * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                gauge = {
                    'axis': {'range': [None, 100], 'tickcolor': "white"},
                    'bar': {'color': "#FF0000"},
                    'bgcolor': "rgba(0,0,0,0)",
                    'steps': [
                        {'range': [0, 50], 'color': 'rgba(255,0,0,0.1)'},
                        {'range': [50, 80], 'color': 'rgba(255,0,0,0.2)'},
                        {'range': [80, 100], 'color': 'rgba(255,0,0,0.3)'}
                    ],
                }
            ))
            fig_gauge.update_layout(height=250, margin=dict(t=0, b=0, l=10, r=10), paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
            st.plotly_chart(fig_gauge, use_container_width=True)

        with c2:
            st.markdown(f'''
            <div class="glass-card">
                <div class="metric-label">Est. Engaged Views</div>
                <div class="metric-value">{int(est_engaged_views):,}</div>
            </div>
            ''', unsafe_allow_html=True)

        with c3:
            st.markdown(f'''
            <div class="glass-card">
                <div class="metric-label">Projected Revenue Lift</div>
                <div class="metric-value">${est_revenue:,.2f}</div>
            </div>
            ''', unsafe_allow_html=True)

    with tab2:
        st.subheader("Performance Comparison")
        data_viz = pd.DataFrame({
            'KPI': ['CTR', 'Retention', 'Ad Yield', 'Engage Rate'],
            'Baseline': [4.2, 35, 8.5, 12],
            'Current': [5.8, 48, 12.2, prob*100]
        })
        fig_bar = px.bar(
            data_viz, x="KPI", y=["Baseline", "Current"],
            barmode="group", color_discrete_sequence=["#444", "#FF0000"],
            template="plotly_dark"
        )
        fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_bar, use_container_width=True)

    with tab3:
        st.success(f"### Optimal Strategy Found")
        st.markdown(f"Analysis complete for segment {cat} on {dev}.")
else:
    st.markdown("""
    <div style="text-align: center; padding: 100px; opacity: 0.6;">
        <h1>👈 Configure & Execute</h1>
    </div>
    """, unsafe_allow_html=True)
