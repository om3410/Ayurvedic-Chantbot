import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import random

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Ayurvedic Wellness AI",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    .main-header {
        color: #2c5530;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #f5f1e8 0%, #e8f4e8 100%);
        border-radius: 10px;
        border-left: 5px solid #d4a574;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f5f1e8 0%, #e8f4e8 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem;
    }
    
    .herb-card {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        border-left: 4px solid #d4a574;
    }
    
    .stButton > button {
        background-color: #2c5530;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #3e7a3e;
    }
</style>
""", unsafe_allow_html=True)

# ==================== AYURVEDIC KNOWLEDGE BASE ====================
class AyurvedicKnowledgeBase:
    def __init__(self):
        self.herbs = self._load_herbs()
        self.dosha_info = self._load_dosha_info()
        self.foods = self._load_foods()
        self.yoga_asanas = self._load_yoga_asanas()
        self.routines = self._load_routines()
    
    def _load_herbs(self):
        return {
            "ashwagandha": {
                "name": "Ashwagandha",
                "sanskrit": "अश्वगन्धा",
                "benefits": ["Stress Relief", "Better Sleep", "Energy Boost"],
                "dosha": "Vata, Kapha",
                "dosage": "500-1000mg daily"
            },
            "turmeric": {
                "name": "Turmeric",
                "sanskrit": "हरिद्रा",
                "benefits": ["Anti-inflammatory", "Antioxidant", "Digestive Aid"],
                "dosha": "All doshas",
                "dosage": "1-3g daily"
            },
            "triphala": {
                "name": "Triphala",
                "sanskrit": "त्रिफला",
                "benefits": ["Digestive Cleanser", "Detoxifier", "Improves Elimination"],
                "dosha": "All doshas",
                "dosage": "1-5g at night"
            },
            "brahmi": {
                "name": "Brahmi",
                "sanskrit": "ब्राह्मी",
                "benefits": ["Memory Boost", "Calms Mind", "Cognitive Function"],
                "dosha": "Vata, Pitta",
                "dosage": "300-500mg daily"
            },
            "ginger": {
                "name": "Ginger",
                "sanskrit": "आर्द्रक",
                "benefits": ["Improves Digestion", "Reduces Nausea", "Clears Congestion"],
                "dosha": "Kapha, Vata",
                "dosage": "1-3g daily"
            }
        }
    
    def _load_dosha_info(self):
        return {
            "vata": {
                "description": "Represents air and space. Governs movement, creativity, and nervous system.",
                "characteristics": "Creative, energetic, thin build, dry skin",
                "imbalance": "Anxiety, constipation, dry skin, insomnia",
                "balance": "Warm foods, regular routine, oil massage"
            },
            "pitta": {
                "description": "Represents fire and water. Governs digestion, metabolism, and transformation.",
                "characteristics": "Intelligent, focused, medium build, warm body",
                "imbalance": "Acidity, inflammation, skin rashes, irritability",
                "balance": "Cooling foods, moderation, meditation"
            },
            "kapha": {
                "description": "Represents earth and water. Governs structure, stability, and lubrication.",
                "characteristics": "Calm, loving, sturdy build, excellent stamina",
                "imbalance": "Weight gain, congestion, lethargy, attachment",
                "balance": "Light foods, exercise, stimulation"
            }
        }
    
    def _load_foods(self):
        return {
            "vata": {
                "increase": ["Warm cooked vegetables", "Whole grains", "Nuts", "Dairy", "Sweet fruits"],
                "decrease": ["Raw vegetables", "Cold foods", "Beans", "Dry foods"]
            },
            "pitta": {
                "increase": ["Sweet fruits", "Bitter greens", "Coconut", "Milk", "Grains"],
                "decrease": ["Spicy foods", "Sour fruits", "Fermented foods", "Alcohol"]
            },
            "kapha": {
                "increase": ["Light fruits", "Steamed vegetables", "Legumes", "Spices", "Honey"],
                "decrease": ["Sweet fruits", "Dairy", "Oily foods", "Wheat"]
            }
        }
    
    def _load_yoga_asanas(self):
        return {
            "vata": [
                {"name": "Balasana", "duration": "5 minutes", "benefits": "Calms mind"},
                {"name": "Vrikshasana", "duration": "3 minutes", "benefits": "Improves balance"},
                {"name": "Shavasana", "duration": "10 minutes", "benefits": "Deep relaxation"}
            ],
            "pitta": [
                {"name": "Chandra Namaskar", "duration": "10 rounds", "benefits": "Cooling effect"},
                {"name": "Forward Bends", "duration": "2 minutes", "benefits": "Calms mind"},
                {"name": "Moon Breathing", "duration": "5 minutes", "benefits": "Reduces heat"}
            ],
            "kapha": [
                {"name": "Surya Namaskar", "duration": "12 rounds", "benefits": "Energizes"},
                {"name": "Backbends", "duration": "3 minutes", "benefits": "Opens chest"},
                {"name": "Twists", "duration": "2 minutes", "benefits": "Stimulates digestion"}
            ]
        }
    
    def _load_routines(self):
        return {
            "vata": [
                "Warm oil self-massage daily",
                "Gentle yoga practice",
                "Regular meal times",
                "Warm beverages",
                "Early bedtime"
            ],
            "pitta": [
                "Cooling pranayama",
                "Moon bathing",
                "Moderate exercise",
                "Regular breaks",
                "Avoid competition"
            ],
            "kapha": [
                "Vigorous morning exercise",
                "Dry massage",
                "Stimulating yoga",
                "Light breakfast",
                "Variety in routine"
            ]
        }
    
    def get_all_herbs(self):
        return list(self.herbs.values())
    
    def get_dosha_info(self, dosha):
        return self.dosha_info.get(dosha.lower(), {})
    
    def get_dosha_specific_routine(self, dosha):
        """Get dosha-specific routine"""
        return self.routines.get(dosha.lower(), [])
    
    def analyze_symptoms(self, symptoms):
        # Simple analysis - returns primary dosha
        dosha_scores = {"vata": 0, "pitta": 0, "kapha": 0}
        
        vata_keywords = ["anxiety", "insomnia", "dry", "constipation", "worry"]
        pitta_keywords = ["acidity", "inflammation", "irritability", "heat", "rash"]
        kapha_keywords = ["congestion", "lethargy", "weight", "slow", "heavy"]
        
        for symptom in symptoms:
            symptom_lower = symptom.lower()
            for keyword in vata_keywords:
                if keyword in symptom_lower:
                    dosha_scores["vata"] += 1
            for keyword in pitta_keywords:
                if keyword in symptom_lower:
                    dosha_scores["pitta"] += 1
            for keyword in kapha_keywords:
                if keyword in symptom_lower:
                    dosha_scores["kapha"] += 1
        
        primary_dosha = max(dosha_scores, key=dosha_scores.get) if sum(dosha_scores.values()) > 0 else "vata"
        
        total = max(sum(dosha_scores.values()), 1)
        return {
            "dosha_probabilities": {
                "vata": dosha_scores["vata"] / total,
                "pitta": dosha_scores["pitta"] / total,
                "kapha": dosha_scores["kapha"] / total
            },
            "primary_dosha": primary_dosha
        }
    
    def get_recommended_herbs(self, symptoms):
        analysis = self.analyze_symptoms(symptoms)
        primary_dosha = analysis["primary_dosha"]
        
        recommended = []
        for herb in self.herbs.values():
            if primary_dosha.lower() in herb["dosha"].lower():
                recommended.append(herb)
        
        return recommended[:3]
    
    def get_dietary_advice(self, dosha):
        return self.foods.get(dosha.lower(), {"increase": [], "decrease": []})

# ==================== INITIALIZE SESSION STATE ====================
if 'kb' not in st.session_state:
    st.session_state.kb = AyurvedicKnowledgeBase()

if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None

if 'dosha_results' not in st.session_state:
    st.session_state.dosha_results = None

if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# Create shortcut for knowledge base
kb = st.session_state.kb

# ==================== PAGE FUNCTIONS ====================
def display_header():
    st.markdown("""
    <div class="main-header">
        <h1>🪷 Ayurvedic Wellness AI</h1>
        <p style="color: #5a7d5a;">Your Personal Guide to Balance & Health</p>
    </div>
    """, unsafe_allow_html=True)

def home_page():
    display_header()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🔍 Dosha Analysis</h3>
            <p>Discover your Ayurvedic constitution</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Analysis", key="home_dosha", use_container_width=True):
            st.session_state.current_page = "dosha"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🌿 Herb Library</h3>
            <p>Explore Ayurvedic herbs</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Herbs", key="home_herbs", use_container_width=True):
            st.session_state.current_page = "herbs"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📅 Daily Routine</h3>
            <p>Personalized daily schedule</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Routine", key="home_routine", use_container_width=True):
            st.session_state.current_page = "routine"
            st.rerun()
    
    # Welcome section
    st.markdown("---")
    st.markdown("### Welcome to Ayurvedic Wellness AI")
    st.markdown("""
    This platform helps you:
    - Discover your unique Ayurvedic constitution (Dosha)
    - Get personalized herb recommendations
    - Follow Ayurvedic daily routines
    - Track your wellness journey
    
    **Get started by taking the dosha analysis test!**
    """)
    
    # Quick tips
    with st.expander("💡 Today's Ayurvedic Tip"):
        tips = [
            "Drink warm water with lemon in the morning to stimulate digestion.",
            "Practice 15 minutes of meditation daily for mental balance.",
            "Eat your largest meal at noon when digestion is strongest.",
            "Go to bed by 10 PM for optimal rest and recovery."
        ]
        st.info(random.choice(tips))

def dosha_analysis_page():
    st.markdown("## 🔍 Dosha Analysis Test")
    
    # Profile section
    with st.expander("👤 User Profile", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name", 
                value=st.session_state.user_profile.get('name', '') if st.session_state.user_profile else '')
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        
        if st.button("Save Profile"):
            st.session_state.user_profile = {
                'name': name,
                'age': age,
                'gender': gender,
                'weight': weight
            }
            st.success("Profile saved!")
    
    # Dosha test questions
    st.markdown("### Answer these questions to discover your dosha:")
    
    questions = [
        "1. What best describes your body frame?",
        "2. How is your skin type?",
        "3. What is your typical appetite like?",
        "4. How do you handle stress?",
        "5. What is your sleep pattern?"
    ]
    
    options = [
        ["Thin, light, prominent bones", "Medium, muscular, well-proportioned", "Large, sturdy, well-padded"],
        ["Dry, rough, cool to touch", "Oily, warm, prone to rashes", "Thick, smooth, cool"],
        ["Irregular, sometimes hungry, sometimes not", "Strong, get irritable if meal is delayed", "Steady but can skip meals easily"],
        ["Worry, anxiety, nervousness", "Irritability, anger, frustration", "Withdraw, avoid, become inactive"],
        ["Light sleeper, easily disturbed", "Moderate sleeper, wake up hot", "Deep sleeper, hard to wake up"]
    ]
    
    answers = []
    
    for i, (question, option_list) in enumerate(zip(questions, options)):
        answer = st.radio(question, option_list, key=f"q_{i}", index=None)
        if answer:
            answers.append(option_list.index(answer) + 1)  # 1 for vata, 2 for pitta, 3 for kapha
        else:
            answers.append(0)
    
    if st.button("📊 Analyze My Dosha", type="primary", use_container_width=True):
        if 0 in answers:
            st.warning("Please answer all questions!")
        else:
            # Calculate scores
            vata_score = answers.count(1)
            pitta_score = answers.count(2)
            kapha_score = answers.count(3)
            
            total = vata_score + pitta_score + kapha_score
            if total > 0:
                vata_pct = (vata_score / total) * 100
                pitta_pct = (pitta_score / total) * 100
                kapha_pct = (kapha_score / total) * 100
            else:
                vata_pct = pitta_pct = kapha_pct = 33.3
            
            # Determine primary dosha
            percentages = {"vata": vata_pct, "pitta": pitta_pct, "kapha": kapha_pct}
            primary_dosha = max(percentages, key=percentages.get)
            
            # Store results
            st.session_state.dosha_results = {
                "percentages": percentages,
                "primary": primary_dosha
            }
            
            # Display results
            st.markdown("### 📈 Your Dosha Analysis Results")
            
            # Create gauge chart
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"**VATA**")
                st.markdown(f"# {vata_pct:.1f}%")
                st.progress(vata_pct/100)
            
            with col2:
                st.markdown(f"**PITTA**")
                st.markdown(f"# {pitta_pct:.1f}%")
                st.progress(pitta_pct/100)
            
            with col3:
                st.markdown(f"**KAPHA**")
                st.markdown(f"# {kapha_pct:.1f}%")
                st.progress(kapha_pct/100)
            
            st.markdown(f"### Primary Dosha: **{primary_dosha.upper()}**")
            
            # Show dosha info
            dosha_data = kb.get_dosha_info(primary_dosha)
            if dosha_data:
                with st.expander(f"📖 About {primary_dosha.upper()} Dosha"):
                    st.markdown(f"**Description:** {dosha_data['description']}")
                    st.markdown(f"**Characteristics:** {dosha_data['characteristics']}")
                    st.markdown(f"**Imbalance Signs:** {dosha_data['imbalance']}")
                    st.markdown(f"**Balancing Tips:** {dosha_data['balance']}")
            
            # Recommendations
            st.markdown("### 💡 Personalized Recommendations")
            
            tabs = st.tabs(["🌿 Herbs", "🍎 Diet", "🧘 Yoga"])
            
            with tabs[0]:
                st.markdown("**Recommended herbs for you:**")
                herbs = kb.get_all_herbs()
                for herb in herbs:
                    if primary_dosha.lower() in herb["dosha"].lower():
                        with st.expander(herb["name"]):
                            st.markdown(f"**Sanskrit:** {herb['sanskrit']}")
                            st.markdown(f"**Benefits:** {', '.join(herb['benefits'])}")
                            st.markdown(f"**Dosage:** {herb['dosage']}")
            
            with tabs[1]:
                st.markdown("**Dietary recommendations:**")
                diet = kb.get_dietary_advice(primary_dosha)
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Eat More:**")
                    for food in diet.get("increase", [])[:5]:
                        st.markdown(f"✅ {food}")
                with col2:
                    st.markdown("**Avoid:**")
                    for food in diet.get("decrease", [])[:5]:
                        st.markdown(f"❌ {food}")

def herb_library_page():
    st.markdown("## 🌿 Ayurvedic Herb Library")
    
    # Search
    search_term = st.text_input("🔍 Search herbs:", "")
    
    # Display herbs
    herbs = kb.get_all_herbs()
    
    if search_term:
        herbs = [h for h in herbs if search_term.lower() in h['name'].lower() or 
                any(search_term.lower() in b.lower() for b in h['benefits'])]
    
    for herb in herbs:
        with st.container():
            st.markdown(f"""
            <div class="herb-card">
                <h4>{herb['name']} ({herb['sanskrit']})</h4>
                <p><strong>Best for:</strong> {herb['dosha']}</p>
                <p><strong>Dosage:</strong> {herb['dosage']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("View Details"):
                st.markdown("**Benefits:**")
                for benefit in herb["benefits"]:
                    st.markdown(f"• {benefit}")
                
                # Show related recommendations
                if st.session_state.dosha_results:
                    primary_dosha = st.session_state.dosha_results["primary"]
                    if primary_dosha.lower() in herb["dosha"].lower():
                        st.success(f"✅ This herb is recommended for your {primary_dosha.upper()} dosha!")
                    else:
                        st.warning(f"⚠️ This herb may not be ideal for your {primary_dosha.upper()} dosha")

def daily_routine_page():
    st.markdown("## 📅 Ayurvedic Daily Routine (Dinacharya)")
    
    # Check if user has done dosha analysis
    if not st.session_state.dosha_results:
        st.warning("Please complete the dosha analysis first for personalized recommendations!")
        if st.button("Take Dosha Test"):
            st.session_state.current_page = "dosha"
            st.rerun()
        return
    
    primary_dosha = st.session_state.dosha_results["primary"]
    
    # Current time info
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        time_of_day = "🌅 Morning"
        suggestion = "Perfect time for meditation and exercise!"
    elif 12 <= current_hour < 17:
        time_of_day = "☀️ Daytime"
        suggestion = "Have you had your main meal yet?"
    elif 17 <= current_hour < 21:
        time_of_day = "🌇 Evening"
        suggestion = "Time for a light dinner and relaxation"
    else:
        time_of_day = "🌙 Night"
        suggestion = "Prepare for restful sleep"
    
    st.info(f"**Current Time:** {time_of_day} - {suggestion}")
    
    # Basic daily routine
    st.markdown("### 📋 Basic Daily Schedule")
    
    routine_data = {
        "Time": ["5:00-6:00 AM", "6:00-7:00 AM", "7:00-8:00 AM", "8:00-9:00 AM", 
                "12:00-1:00 PM", "6:00-7:00 PM", "9:00-10:00 PM"],
        "Activity": ["Wake up", "Oral hygiene & Oil pulling", "Exercise & Yoga", "Bath & Meditation",
                    "Main Meal", "Light Dinner", "Sleep"],
        "Description": ["Best time to wake up", "Cleanse with oil", "Gentle exercise", "15-min meditation",
                       "Largest meal of day", "2-3 hours before sleep", "Digital detox before bed"]
    }
    
    df_routine = pd.DataFrame(routine_data)
    st.dataframe(df_routine, use_container_width=True, hide_index=True)
    
    # Dosha-specific routine
    st.markdown(f"### 🎯 Special Tips for {primary_dosha.upper()} Dosha")
    
    dosha_specific = kb.get_dosha_specific_routine(primary_dosha)
    if dosha_specific:
        for tip in dosha_specific:
            st.markdown(f"• {tip}")
    else:
        st.info("No specific tips available for this dosha.")
    
    # Interactive planner
    st.markdown("### ✍️ Customize Your Routine")
    
    with st.form("routine_form"):
        wake_time = st.time_input("Wake up time", value=datetime.strptime("06:00", "%H:%M").time())
        sleep_time = st.time_input("Sleep time", value=datetime.strptime("22:00", "%H:%M").time())
        meditation = st.checkbox("Include meditation", value=True)
        exercise = st.checkbox("Include exercise", value=True)
        
        submitted = st.form_submit_button("Save My Routine")
        if submitted:
            st.success("Routine preferences saved!")

def symptom_checker_page():
    st.markdown("## 🤒 Symptom Checker")
    
    # Common symptoms
    symptoms_list = [
        "Headache", "Fatigue", "Insomnia", "Acidity", "Constipation",
        "Anxiety", "Joint Pain", "Skin Rash", "Poor Digestion", "Low Immunity"
    ]
    
    selected_symptoms = st.multiselect(
        "Select your symptoms:",
        symptoms_list,
        placeholder="Choose all that apply..."
    )
    
    if st.button("🔍 Analyze Symptoms", use_container_width=True):
        if not selected_symptoms:
            st.warning("Please select at least one symptom")
        else:
            with st.spinner("Analyzing symptoms..."):
                # Analyze symptoms
                analysis = kb.analyze_symptoms(selected_symptoms)
                
                st.markdown("### 📋 Analysis Results")
                
                # Display dosha imbalance
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("##### 🎯 Probable Dosha Imbalance")
                    for dosha, prob in analysis["dosha_probabilities"].items():
                        progress = int(prob * 100)
                        st.markdown(f"**{dosha.upper()}**: {progress}%")
                        st.progress(progress / 100)
                
                with col2:
                    st.markdown("##### 💡 Recommendations")
                    herbs = kb.get_recommended_herbs(selected_symptoms)
                    for herb in herbs[:2]:
                        st.markdown(f"**{herb['name']}** - {herb['dosage']}")
                
                # Immediate remedies
                st.markdown("### 🏥 Immediate Home Remedies")
                remedies = {
                    "Headache": ["Apply sandalwood paste on forehead", "Drink ginger tea"],
                    "Acidity": ["Drink cold milk", "Take amla powder with honey"],
                    "Constipation": ["Warm water with ghee", "Triphala powder at night"],
                    "Anxiety": ["Ashwagandha with warm milk", "Meditation"],
                    "Fatigue": ["Ashwagandha with warm milk", "Proper rest"],
                    "Insomnia": ["Warm milk with nutmeg before bed", "Foot massage with warm oil"],
                    "Joint Pain": ["Apply warm sesame oil", "Turmeric with warm milk"],
                    "Skin Rash": ["Apply neem paste", "Turmeric with honey"],
                    "Poor Digestion": ["Ginger tea before meals", "Triphala powder"],
                    "Low Immunity": ["Ashwagandha", "Tulsi tea"]
                }
                
                for symptom in selected_symptoms:
                    if symptom in remedies:
                        st.markdown(f"**For {symptom}:**")
                        for remedy in remedies[symptom]:  # CORRECTED LINE: symptom instead of symptome
                            st.markdown(f"• {remedy}")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    
    # User info
    if st.session_state.user_profile:
        st.markdown(f"**Welcome, {st.session_state.user_profile['name']}!**")
        if st.session_state.dosha_results:
            st.markdown(f"**Primary Dosha:** {st.session_state.dosha_results['primary'].upper()}")
    
    st.markdown("---")
    
    # Navigation buttons
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        st.session_state.current_page = "home"
        st.rerun()
    
    if st.button("🔍 Dosha Analysis", use_container_width=True, key="nav_dosha"):
        st.session_state.current_page = "dosha"
        st.rerun()
    
    if st.button("🌿 Herb Library", use_container_width=True, key="nav_herbs"):
        st.session_state.current_page = "herbs"
        st.rerun()
    
    if st.button("📅 Daily Routine", use_container_width=True, key="nav_routine"):
        st.session_state.current_page = "routine"
        st.rerun()
    
    if st.button("🤒 Symptom Checker", use_container_width=True, key="nav_symptoms"):
        st.session_state.current_page = "symptoms"
        st.rerun()
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### ⚡ Quick Actions")
    
    if st.button("🔄 Reset Session", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    
    if st.session_state.dosha_results:
        if st.button("📊 View Dosha Report", use_container_width=True):
            st.session_state.current_page = "dosha"
            st.rerun()
    
    st.markdown("---")
    st.caption("© 2024 Ayurvedic Wellness AI")
    st.caption("*For educational purposes only*")

# ==================== MAIN APP ROUTING ====================
if st.session_state.current_page == "home":
    home_page()
elif st.session_state.current_page == "dosha":
    dosha_analysis_page()
elif st.session_state.current_page == "herbs":
    herb_library_page()
elif st.session_state.current_page == "routine":
    daily_routine_page()
elif st.session_state.current_page == "symptoms":
    symptom_checker_page()