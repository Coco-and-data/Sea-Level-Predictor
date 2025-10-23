from sea_level_predictor import draw_plot

print("Testing Sea Level Predictor...")
print("=" * 50)

try:
    print("Creating sea level prediction plot...")
    draw_plot()
    print("✅ Sea level plot saved as 'sea_level_plot.png'")
    
    print("\n" + "=" * 50)
    print("🎉 SUCCESS! Visualization created!")
    print("Check your file: sea_level_plot.png")
    print("\nThe plot shows:")
    print("  - Scatter plot of historical data (1880-present)")
    print("  - Red line: prediction using ALL data")
    print("  - Green line: prediction using data from 2000+")
    print("  - Both lines extend to year 2050")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Make sure all libraries are installed:")
    print("pip install pandas matplotlib scipy numpy")
