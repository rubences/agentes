"""
Google Trends Visualization for AI Tools in Spain
Generates a line chart showing synthetic popularity index data for ChatGPT, Claude, Gemini, Copilot, and Deepseek
from September 2022 to February 2025.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates

def generate_synthetic_trends_data():
    """
    Generate synthetic but representative Google Trends data for AI tools in Spain.
    Values are on a 0-100 scale where 100 represents peak popularity.
    """
    
    # Create date range from September 2022 to February 2025
    start_date = datetime(2022, 9, 1)
    end_date = datetime(2025, 2, 28)
    dates = pd.date_range(start=start_date, end=end_date, freq='W')  # Weekly data points
    
    # Initialize the data dictionary
    data = {'Date': dates}
    
    # ChatGPT: Released November 2022, explosive growth, then stabilization
    chatgpt_trend = []
    for date in dates:
        if date < datetime(2022, 11, 1):
            # Before release
            value = np.random.normal(2, 1)
        elif date < datetime(2022, 12, 1):
            # Initial release period - rapid growth
            weeks_since_release = (date - datetime(2022, 11, 1)).days / 7
            value = min(85, 5 + weeks_since_release * 20) + np.random.normal(0, 5)
        elif date < datetime(2023, 3, 1):
            # Peak popularity period
            value = np.random.normal(95, 8)
        elif date < datetime(2023, 8, 1):
            # High but declining
            months_since_peak = (date - datetime(2023, 3, 1)).days / 30
            value = max(60, 95 - months_since_peak * 8) + np.random.normal(0, 6)
        else:
            # Stabilized high usage
            value = np.random.normal(75, 10)
        
        chatgpt_trend.append(max(0, min(100, value)))
    
    data['ChatGPT'] = chatgpt_trend
    
    # Claude: Gradual growth, steady increase
    claude_trend = []
    for date in dates:
        if date < datetime(2023, 1, 1):
            # Early period, low awareness
            value = np.random.normal(5, 2)
        elif date < datetime(2023, 6, 1):
            # Growing awareness
            months_since_start = (date - datetime(2023, 1, 1)).days / 30
            value = 5 + months_since_start * 8 + np.random.normal(0, 3)
        elif date < datetime(2024, 1, 1):
            # Steady growth
            value = np.random.normal(40, 8)
        else:
            # Mature adoption
            value = np.random.normal(55, 10)
        
        claude_trend.append(max(0, min(100, value)))
    
    data['Claude'] = claude_trend
    
    # Gemini: Released as Bard in March 2023, rebranded to Gemini in December 2023
    gemini_trend = []
    for date in dates:
        if date < datetime(2023, 3, 1):
            # Before Bard release
            value = np.random.normal(1, 0.5)
        elif date < datetime(2023, 6, 1):
            # Bard initial release
            months_since_release = (date - datetime(2023, 3, 1)).days / 30
            value = 15 + months_since_release * 12 + np.random.normal(0, 4)
        elif date < datetime(2023, 12, 1):
            # Bard period - moderate growth
            value = np.random.normal(45, 8)
        elif date < datetime(2024, 3, 1):
            # Gemini rebrand boost
            months_since_rebrand = (date - datetime(2023, 12, 1)).days / 30
            value = 45 + months_since_rebrand * 10 + np.random.normal(0, 6)
        else:
            # Gemini mature period
            value = np.random.normal(65, 12)
        
        gemini_trend.append(max(0, min(100, value)))
    
    data['Gemini'] = gemini_trend
    
    # Copilot: Steady growth, professional tool adoption pattern
    copilot_trend = []
    for date in dates:
        if date < datetime(2023, 1, 1):
            # Early developer awareness
            value = np.random.normal(15, 4)
        elif date < datetime(2023, 7, 1):
            # Growing professional adoption
            months_since_start = (date - datetime(2023, 1, 1)).days / 30
            value = 15 + months_since_start * 5 + np.random.normal(0, 3)
        elif date < datetime(2024, 6, 1):
            # Steady professional use
            value = np.random.normal(35, 6)
        else:
            # Increased mainstream awareness
            value = np.random.normal(45, 8)
        
        copilot_trend.append(max(0, min(100, value)))
    
    data['Copilot'] = copilot_trend
    
    # Deepseek: More recent entrant, rapid growth in 2024
    deepseek_trend = []
    for date in dates:
        if date < datetime(2024, 1, 1):
            # Very low awareness before 2024
            value = np.random.normal(2, 1)
        elif date < datetime(2024, 6, 1):
            # Initial growth
            months_since_start = (date - datetime(2024, 1, 1)).days / 30
            value = 2 + months_since_start * 6 + np.random.normal(0, 2)
        elif date < datetime(2024, 10, 1):
            # Accelerating growth
            value = np.random.normal(30, 6)
        else:
            # Recent surge in popularity
            months_since_surge = (date - datetime(2024, 10, 1)).days / 30
            value = 30 + months_since_surge * 15 + np.random.normal(0, 8)
        
        deepseek_trend.append(max(0, min(100, value)))
    
    data['Deepseek'] = deepseek_trend
    
    return pd.DataFrame(data)

def create_trends_chart(df, save_path='google_trends_spain_2022_2025.png'):
    """
    Create and save a line chart showing Google Trends data for AI tools in Spain.
    """
    
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Define colors for each tool
    colors = {
        'ChatGPT': '#FF6B6B',    # Red
        'Claude': '#4ECDC4',     # Teal
        'Gemini': '#45B7D1',     # Blue
        'Copilot': '#96CEB4',    # Green
        'Deepseek': '#FECA57'    # Yellow
    }
    
    # Plot each tool's trend
    for tool in ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Deepseek']:
        ax.plot(df['Date'], df[tool], 
               label=tool, 
               color=colors[tool], 
               linewidth=2.5, 
               alpha=0.8)
    
    # Customize the chart
    ax.set_title('Google Trends: AI Tools Popularity in Spain\n(September 2022 - February 2025)', 
                fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Search Interest (Relative Scale 0-100)', fontsize=12, fontweight='bold')
    
    # Format x-axis
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45)
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Customize legend
    ax.legend(loc='upper left', frameon=True, shadow=True, fontsize=11)
    
    # Set y-axis limits
    ax.set_ylim(0, 105)
    
    # Add subtle background color
    ax.set_facecolor('#FAFAFA')
    
    # Adjust layout
    plt.tight_layout()
    
    # Add annotation
    plt.figtext(0.02, 0.02, 'Data: Synthetic representative trends based on actual release dates and market adoption patterns', 
                fontsize=8, style='italic', alpha=0.7)
    
    # Save the chart
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Chart saved as: {save_path}")
    
    # Show the chart
    plt.show()
    
    return fig

def main():
    """
    Main function to generate data and create the visualization.
    """
    print("Generating synthetic Google Trends data for AI tools in Spain...")
    df = generate_synthetic_trends_data()
    
    print("\nData generated successfully!")
    print(f"Date range: {df['Date'].min().strftime('%B %Y')} to {df['Date'].max().strftime('%B %Y')}")
    print(f"Total data points: {len(df)}")
    
    print("\nCreating visualization...")
    fig = create_trends_chart(df)
    
    print("\nSample data preview:")
    print(df.head(10).to_string(index=False))
    
    # Save the data to CSV for reference
    df.to_csv('google_trends_data.csv', index=False)
    print("\nRaw data saved as: google_trends_data.csv")

if __name__ == "__main__":
    main()