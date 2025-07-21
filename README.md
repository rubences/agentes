# Google Trends Visualization for AI Tools in Spain

This project generates a line chart showing Google Trends popularity index for major AI chatbots and coding tools from September 2022 to February 2025, specifically for Spain.

## Tools Analyzed

- **ChatGPT**: OpenAI's conversational AI (launched November 2022)
- **Claude**: Anthropic's AI assistant (launched March 2022, gained popularity later)
- **Gemini**: Google's AI model (originally Bard in March 2023, rebranded December 2023)
- **Copilot**: GitHub's AI coding assistant (mainstream adoption from 2023)
- **Deepseek**: AI development platform (gained significant popularity in 2024)

## Features

- Synthetic but representative data based on actual release dates and market adoption patterns
- Weekly data points from September 2022 to February 2025
- Spain-specific search interest trends
- Professional visualization with matplotlib
- Export functionality for both chart and raw data

## Installation

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the visualization script:

```bash
python google_trends_visualization.py
```

This will:
- Generate synthetic trends data
- Create and display the line chart
- Save the chart as `google_trends_spain_2022_2025.png`
- Export raw data as `google_trends_data.csv`

## Output

The script generates:
- **PNG Chart**: High-resolution line chart showing trends over time
- **CSV Data**: Raw data points for further analysis
- **Console Output**: Summary statistics and data preview

## Data Methodology

The synthetic data is based on:
- Actual release dates of each AI tool
- Realistic adoption patterns observed in the market
- Spain-specific search behavior considerations
- Seasonal and trend variations

The popularity index ranges from 0-100, where 100 represents peak search interest relative to the highest point in the dataset for the given time period and location.