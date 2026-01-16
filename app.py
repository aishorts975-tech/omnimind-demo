import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="OmniMind Intelligence Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3B82F6;
    }
    .agent-status {
        background: linear-gradient(90deg, #10B981 0%, #34D399 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 5px;
        text-align: center;
    }
    .alert-high { border-left: 4px solid #EF4444; }
    .alert-medium { border-left: 4px solid #F59E0B; }
    .alert-low { border-left: 4px solid #10B981; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 OmniMind Intelligence Platform</h1>', unsafe_allow_html=True)
st.markdown("**Enterprise-grade AI intelligence with 10,000+ autonomous agents**")

# Sidebar Configuration
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103655.png", width=100)
    st.markdown("### Configuration")
    
    selected_industry = st.selectbox(
        "Select Industry",
        ["Technology", "Financial Services", "Healthcare", "Energy", "Consumer Goods", "Real Estate"]
    )
    
    time_horizon = st.slider("Forecast Horizon (days)", 7, 90, 30)
    
    st.markdown("---")
    st.markdown("### Agent Control")
    agent_count = st.number_input("Active Agents", min_value=1000, max_value=10000, value=5000, step=1000)
    auto_refresh = st.toggle("Auto-refresh", value=True)
    
    st.markdown("---")
    st.markdown("#### About OmniMind")
    st.info("""
    **OmniMind Architecture:**
    - 10,000+ Autonomous AI Agents
    - Real-time Data Processing
    - Predictive Intelligence Engine
    - Enterprise-Grade Security
    """)

# Main Dashboard Layout
col1, col2 = st.columns([2, 1])

with col1:
    # Market Intelligence Section
    st.markdown("### 📈 Market Intelligence Dashboard")
    
    # Generate simulated data
    dates = pd.date_range(start='2026-01-01', periods=time_horizon, freq='D')
    base_value = 100
    trend_data = []
    
    for i in range(time_horizon):
        trend = base_value + (i * random.uniform(1.5, 3.5))
        if selected_industry == "Technology":
            trend *= 1.2
        elif selected_industry == "Healthcare":
            trend += random.uniform(0, 5)
        trend_data.append(trend)
    
    # Create trend chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, 
        y=trend_data,
        mode='lines+markers',
        name='Predicted Trend',
        line=dict(color='#3B82F6', width=3),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.1)'
    ))
    
    fig.update_layout(
        title=f"{selected_industry} Market Forecast",
        xaxis_title="Date",
        yaxis_title="Market Index",
        hovermode="x unified",
        template="plotly_white",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Metrics Row
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Prediction Confidence", "89%", "+2% this week")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Risk Level", "Medium", "-5% from last month")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Data Freshness", "98%", "Real-time")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Agent Status
    st.markdown("### 🤖 Agent Status")
    st.markdown(f'<div class="agent-status">{agent_count:,} Active Agents</div>', unsafe_allow_html=True)
    st.progress(agent_count / 10000)
    
    # Agent Distribution
    agent_data = {
        "Type": ["Prediction", "Simulation", "Validation", "Monitoring"],
        "Count": [agent_count//2, agent_count//4, agent_count//6, agent_count//12],
        "Status": ["✅ Active", "🔄 Processing", "✅ Active", "⚠️ Warning"]
    }
    st.dataframe(pd.DataFrame(agent_data), use_container_width=True, hide_index=True)
    
    # System Health
    st.markdown("### 🏥 System Health")
    health_metrics = {
        "API Response Time": "47ms",
        "Data Processing": "1.2M records/hour",
        "Uptime": "99.97%",
        "Error Rate": "0.03%"
    }
    
    for metric, value in health_metrics.items():
        st.text(f"{metric}: {value}")

# Risk Alerts Section
st.markdown("### ⚠️ Risk Intelligence Alerts")

alert_col1, alert_col2, alert_col3 = st.columns(3)

with alert_col1:
    st.markdown('<div class="metric-card alert-high">', unsafe_allow_html=True)
    st.markdown("**HIGH RISK**")
    st.markdown("Supply chain disruption detected in Asian markets")
    st.caption("🕒 2 hours ago | Confidence: 92%")
    st.markdown('</div>', unsafe_allow_html=True)

with alert_col2:
    st.markdown('<div class="metric-card alert-medium">', unsafe_allow_html=True)
    st.markdown("**MEDIUM RISK**")
    st.markdown("Regulatory changes expected in EU tech sector")
    st.caption("🕒 1 day ago | Confidence: 78%")
    st.markdown('</div>', unsafe_allow_html=True)

with alert_col3:
    st.markdown('<div class="metric-card alert-low">', unsafe_allow_html=True)
    st.markdown("**LOW RISK**")
    st.markdown("Competitor product launch scheduled for Q2")
    st.caption("🕒 3 days ago | Confidence: 65%")
    st.markdown('</div>', unsafe_allow_html=True)

# Live Intelligence Feed
st.markdown("### 📊 Live Intelligence Feed")

# Simulated intelligence data
intel_samples = [
    {
        "source": "Market API",
        "insight": "AI chip demand increased by 15% month-over-month",
        "impact": "High",
        "confidence": 92
    },
    {
        "source": "News Analysis",
        "insight": "EU Parliament discussing new AI regulations",
        "impact": "Medium",
        "confidence": 78
    },
    {
        "source": "Social Sentiment",
        "insight": "Consumer confidence turning positive in tech sector",
        "impact": "Medium",
        "confidence": 85
    },
    {
        "source": "Geopolitical Intel",
        "insight": "Trade agreement negotiations progressing positively",
        "impact": "Low",
        "confidence": 70
    }
]

for intel in intel_samples:
    with st.expander(f"{intel['source']}: {intel['insight']}"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Impact Level", intel['impact'])
        with col_b:
            st.metric("Confidence", f"{intel['confidence']}%")
        st.caption(f"Processed by {random.randint(50, 200)} specialized agents")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280;">
    <p><strong>OmniMind v1.0</strong> | Enterprise Intelligence Platform</p>
    <p>10,000+ Autonomous AI Agents | Real-time Predictive Intelligence</p>
    <p>🔒 SOC2 Compliant | ⚡ 99.9% Uptime | 🔗 API-First Architecture</p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh logic
if auto_refresh:
    st.rerun()
