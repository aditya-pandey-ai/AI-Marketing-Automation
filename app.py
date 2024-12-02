import streamlit as st
import pandas as pd
from functions.load_data import load_campaign_data
from functions.batch_processing import batch_process_campaigns
from functions.generate_insights import generate_llm_insights
from functions.action_executor import simulate_action_execution
from functions.visualization import (
    plot_comparison,
    plot_revenue_waterfall,
    plot_parallel_coordinates,
    plot_roi_bubble_chart
)
from functions.reporting import generate_pdf_report
from data.db import setup_database, store_campaign_history, store_recommendations, retrieve_recommendations

# Configure Streamlit page
st.set_page_config(page_title="Marketing Automation", layout="wide")

# Sidebar Configuration
st.sidebar.title("Marketing Campaign Analysis")
campaign_file = st.sidebar.file_uploader("Upload Campaign Data (CSV)", type=["csv"])
target_cpa = st.sidebar.number_input("Target CPA", value=50.0)
min_ctr = st.sidebar.number_input("Minimum CTR", value=0.01)

run_analysis = st.sidebar.button("Run Analysis")
view_history = st.sidebar.button("View History")

# Initialize the database
setup_database()

# Main View
st.title("Marketing Automation Agent")

# Initialize session state for actions
if "actions" not in st.session_state:
    st.session_state.actions = None

if campaign_file:
    try:
        # Step 1: Load campaign data
        campaign_data = load_campaign_data(campaign_file)
        st.subheader("Uploaded Campaign Data")
        st.dataframe(campaign_data)

        if run_analysis:
            # Step 2: Process campaigns
            actions = batch_process_campaigns(campaign_data, target_cpa, min_ctr)
            st.session_state.actions = actions  # Store in session state
            st.subheader("Campaign Recommendations")
            st.json(actions)

            # Store recommendations in the database
            store_recommendations(actions)

            # Step 3: Generate LLM insights
            insights = generate_llm_insights(campaign_data.head(3).to_dict(orient="records"))
            st.subheader("AI-Generated Insights")
            st.text(insights)

            # Step 4: Execute Actions
            simulate_action_execution(actions)

            # Step 5: Visualize Trends
            st.subheader("Performance Dashboard")

            comparison_fig = plot_comparison(campaign_data)
            st.plotly_chart(comparison_fig)

            bubble_fig = plot_roi_bubble_chart(campaign_data)
            st.plotly_chart(bubble_fig)

            parallel_fig = plot_parallel_coordinates(campaign_data)
            st.plotly_chart(parallel_fig)

            waterfall_fig = plot_revenue_waterfall(campaign_data)
            st.plotly_chart(waterfall_fig)

    except Exception as e:
        st.error(f"Error processing file: {e}")

if st.sidebar.button("Generate PDF Report"):
    if st.session_state.actions:
        try:
            # Generate and save the PDF report
            report_file = "campaign_report.pdf"
            generate_pdf_report(st.session_state.actions, report_file)
            st.success(f"Report generated successfully: {report_file}")

            # Add a download button for the generated report
            with open(report_file, "rb") as file:
                st.download_button(
                    label="Download PDF Report",
                    data=file,
                    file_name="Campaign_Report.pdf",
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Failed to generate PDF report: {e}")
    else:
        st.error("No actions available to generate the report. Run the analysis first.")

if view_history:
    # Sidebar button to view historical recommendations
    history = retrieve_recommendations()
    if not history.empty:
        st.subheader("Recommendation History")
        st.dataframe(history)
    else:
        st.info("No recommendations found in the database.")
