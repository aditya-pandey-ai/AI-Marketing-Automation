import plotly.express as px
import plotly.graph_objects as go



def plot_comparison(data):
    """
    Side-by-side comparison of key metrics for campaigns.
    """
    metrics = ['CTR', 'CPA', 'ROAS']
    fig = go.Figure()

    for metric in metrics:
        if metric in data.columns:
            fig.add_trace(go.Bar(
                x=data['Campaign ID'],
                y=data[metric],
                name=metric
            ))

    fig.update_layout(
        barmode='group',
        title='Campaign Performance Comparison',
        xaxis_title='Campaign ID',
        yaxis_title='Metric Value'
    )
    return fig

def plot_roi_bubble_chart(data):
    """
    Bubble chart to compare campaign ROI with impressions as bubble size.
    """
    data['ROI'] = (data['Revenue'] - data['Spend']) / data['Spend']  # Calculate ROI

    fig = px.scatter(
        data,
        x='Spend',
        y='Revenue',
        size='Impressions',
        color='Campaign ID',
        hover_data=['ROI'],
        title='ROI Analysis by Campaign',
        labels={'Spend': 'Spend ($)', 'Revenue': 'Revenue ($)', 'Impressions': 'Impressions'}
    )
    fig.update_traces(marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_layout(legend_title_text='Campaigns')
    return fig

def plot_parallel_coordinates(data):
    """
    Parallel coordinates plot for multi-metric campaign comparison.
    """
    fig = px.parallel_coordinates(
        data,
        dimensions=['Spend', 'Revenue', 'ROAS', 'Impressions', 'Clicks'],
        color='ROAS',
        color_continuous_scale=px.colors.sequential.Inferno,
        title='Multi-Metric Campaign Comparison'
    )
    return fig

def plot_revenue_waterfall(data):
    """
    Waterfall chart showing contributions of campaigns to total revenue.
    """
    campaign_revenue = data.groupby('Campaign ID')['Revenue'].sum().reset_index()

    fig = go.Figure(go.Waterfall(
        name="Campaign Revenue",
        orientation="v",
        x=campaign_revenue['Campaign ID'],
        y=campaign_revenue['Revenue'],
        connector=dict(line=dict(color="rgb(63, 63, 63)")),
    ))

    fig.update_layout(
        title="Campaign Revenue Contribution",
        xaxis_title="Campaign ID",
        yaxis_title="Revenue ($)",
        waterfallgap=0.5
    )
    return fig
