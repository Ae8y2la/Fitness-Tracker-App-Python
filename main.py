# Start by importing the modules needed for the application
import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time

# Using Custom CSS for styling and animations
st.markdown(
    """
    <style>
/* Main background color */
.stApp {
    background-color: #E2D6C9 !important;
    color: #233326 !important;
}
/* Step 2: Set text color for h1 */
h1 {
    color: #233326 !important;
}

/* Step 3: Set text color for h2 */
h2 {
    color: #233326 !important;
}

/* Step 4: Set text color for h3 */
h3 { 
    color: ##D9B991 !important;
}

/* Step 5: Set text color for h4 */
h4 {
    color: #D9B991 !important; 
}

/* Step 6: Set text color for h5 */
h5 {
    color: #D9B991 !important; 
}

/* Step 7: Set text color for h6 */
h6 {
    color: #D9B991 !important; 
}

/* Step 8: Set text color for paragraphs (p) */
p {
    color: #233326 !important; 
}

/* Step 9: Set text color for labels */
label {
    color: #D9B991 !important; 
}

/* Step 10: Set text color for divs */
div {
    color: #626C3B !important; 
}

/* Step 11: Set text color for spans */
span {
    color: #D9B991 !important; 
}

/* Step 12: Set text color for links (a) */
a {
    color: #D9B991 !important;
}

/* Button styling */
.stButton>button {
    background-color: #E1C2B3 !important;
    color: #372A1B !important;
    border-radius: 10px;
    transition: all 0.3s ease;
}

/* Button hover effect */
.stButton>button:hover {
    background-color: #D8C8B8 !important;
    color: #2E301B !important;
    transform: scale(1.05);
}

/* Only apply hover effect to buttons, not the whole app */
button:hover {
    background-color: #D8C8B8 !important;
    color: #2E301B !important;
}

/* Input fields */
.stTextInput>div>div>input, 
.stNumberInput>div>div>input, 
.stDateInput>div>div>input, 
.stTextArea>div>div>textarea {
    background-color: #372A1B !important;
    color:#8F6246 !important;
    border-radius: 5px;
    transition: all 0.3s ease;
}

/* Input fields hover effect */
.stTextInput>div>div>input:hover, 
.stNumberInput>div>div>input:hover, 
.stDateInput>div>div>input:hover, 
.stTextArea>div>div>textarea:hover {
    border: 1px solid #8F6246  !important;
}

/* Dropdown styling */
.stSelectbox>div, 
.stNumberInput>div>div {
    background-color: #E1C2B3 !important;
    color: #D9B991 !important;
    border-radius: 5px;
}

/* Dropdown text visibility */
.stSelectbox>div>div>div {
    color: #D9B991  !important;
}

/* Dropdown options text */
.stSelectbox [role="listbox"] div {
    color: #D9B991  !important;
}

/* Dropdown hover effect */
.stSelectbox [role="listbox"] div:hover {
    background-color: #D8C8B8 !important;
    color: #8F6246  !important;
}

/* Style Goal, Exercise, Setting, Workout Logger buttons */
.option-button {
    background-color: #8F6246  !important;
    color: #8F6246   !important;
    border-radius: 5px;
    padding: 8px 12px;
    border: none;
    cursor: pointer;
}

/* Hover effect for option buttons */
.option-button:hover {
    background-color: #8F6246  !important;
    color: #8F6246 !important;

    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'workouts' not in st.session_state:
    st.session_state.workouts = []
if 'exercise_log' not in st.session_state:
    st.session_state.exercise_log = []
if 'goals' not in st.session_state:
    st.session_state.goals = []

# App title
st.title("FitTrack Pro 🏋️")

# Navigation tabs!
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "📅 Workout Planner", "📝 Exercise Log", "📈 Progress Tracker", "🎯 Goals"])

with tab1:
    st.header("Welcome to FitTrack Pro!")
    st.write("""
    Your personal fitness companion for:
    - Workout planning 📅
    - Exercise tracking 📝
    - Progress visualization 📈
    - Goal setting 🎯
    """)
    
    st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b", width=600)
    
    # Balloon animation for fun
    if st.button("Celebrate 🎉"):
        st.balloons()

with tab2:
    st.header("Workout Planner")
    
    # Workout type selection
    workout_type = st.selectbox(
        "Choose workout type:",
        ["Strength Training", "Cardio", "HIIT", "Yoga", "Custom"]
    )
    
    # Exercise input
    col1, col2, col3 = st.columns(3)
    with col1:
        exercise = st.text_input("Exercise name")
    with col2:
        sets = st.number_input("Sets", min_value=1, max_value=10, value=3)
    with col3:
        reps = st.number_input("Reps", min_value=1, max_value=50, value=10)
    
    if st.button("Add Exercise to Workout Plan"):
        if exercise:
            st.session_state.workouts.append({
                "type": workout_type,
                "exercise": exercise,
                "sets": sets,
                "reps": reps
            })
            st.success("Exercise added to workout plan!")
            time.sleep(1)  
            st.rerun()  
        else:
            st.warning("Please enter an exercise name!")
    
    # Display current workout plan
    st.subheader("Current Workout Plan")
    if st.session_state.workouts:
        workout_df = pd.DataFrame(st.session_state.workouts)
        st.dataframe(workout_df.style.highlight_max(axis=0))
    else:
        st.info("No exercises in current workout plan")

with tab3:
    st.header("Exercise Logger")
    
    # Log exercise form
    with st.form("exercise_log_form"):
        date = st.date_input("Date", datetime.date.today())
        
        # Get exercises from workouts
        exercise_options = list(set([w["exercise"] for w in st.session_state.workouts])) if st.session_state.workouts else ["Add exercises in Workout Planner first"]
        
        exercise = st.selectbox(
            "Exercise",
            options=exercise_options
        )
        
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=180)
        weight = st.number_input("Weight (kg)", min_value=0, max_value=500)
        notes = st.text_area("Notes")
        
        if st.form_submit_button("Log Exercise"):
            if exercise != "Add exercises in Workout Planner first":
                st.session_state.exercise_log.append({
                    "date": date,
                    "exercise": exercise,
                    "duration": duration,
                    "weight": weight,
                    "notes": notes
                })
                st.success("Exercise logged!")
                time.sleep(1)  
                st.rerun()  
            else:
                st.warning("Please add exercises in the Workout Planner tab first!")
    
    # Display exercise log
    st.subheader("Exercise History")
    if st.session_state.exercise_log:
        log_df = pd.DataFrame(st.session_state.exercise_log)
        st.dataframe(log_df)
    else:
        st.info("No exercises logged yet")

with tab4:
    st.header("Progress Tracker")
    
    if st.session_state.exercise_log:
        # Progress visualization
        selected_exercise = st.selectbox(
            "Select exercise to view progress",
            options=list(set([log["exercise"] for log in st.session_state.exercise_log]))
        )
        
        exercise_data = pd.DataFrame([log for log in st.session_state.exercise_log if log["exercise"] == selected_exercise])
        
        if not exercise_data.empty:
            fig, ax = plt.subplots()
            ax.plot(exercise_data["date"], exercise_data["weight"], marker='o', color='#4D9BE6')
            ax.set_xlabel("Date", color='#AF6E4D')
            ax.set_ylabel("Weight (kg)", color='#AF6E4D')
            ax.set_title(f"{selected_exercise} Progress", color='#AF6E4D')
            ax.set_facecolor('#8F6246 ')
            fig.patch.set_facecolor('#8F6246 ')
            ax.tick_params(colors='#AF6E4D')
            st.pyplot(fig)
        else:
            st.warning("No data available for selected exercise")
    else:
        st.info("No exercise data available yet")

with tab5:
    st.header("Goal Setting")
    
    # Goal input
    with st.form("goal_form"):
        goal_type = st.selectbox("Goal Type", ["Weight Loss", "Strength Gain", "Endurance", "Flexibility"])
        target = st.text_input("Target (e.g., 'Deadlift 150kg')")
        deadline = st.date_input("Target Date")
        
        if st.form_submit_button("Add Goal"):
            st.session_state.goals.append({
                "type": goal_type,
                "target": target,
                "deadline": deadline,
                "achieved": False
            })
            st.success("Goal added!")
            time.sleep(1) 
            st.rerun()  
    
    # Let's Display goals
    st.subheader("Current Goals")
    if st.session_state.goals:
        for i, goal in enumerate(st.session_state.goals):
            cols = st.columns([1, 0.2])
            with cols[0]:
                st.markdown(f"""
                **{goal['type']} Goal**
                - Target: {goal['target']}
                - Deadline: {goal['deadline']}
                - Status: {'✅ Achieved' if goal['achieved'] else '🔄 In Progress'}
                """)
            with cols[1]:
                if st.button(f"Complete##{i}"):
                    st.session_state.goals[i]["achieved"] = True
                    st.success("Goal marked as achieved!")
                    time.sleep(1)  
                    st.rerun()  
    else:
        st.info("No current goals set")
        
 # ----------------------------------------------------THE-END---------------------------------------------------------------- 