import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# Graphic 1: Tariff and Currency Offset
def plot_tariff_offset():
    base_price, tariff_rate, currency_offset = 100, 0.10, 0.10
    prices = [base_price, base_price * (1 + tariff_rate), 
              base_price * (1 - currency_offset) * (1 + tariff_rate)]
    labels = ['No Tariff', 'Tariff, No Offset', 'Tariff with Offset']
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, prices, color=['#4CAF50', '#FF5733', '#3498DB'], edgecolor='black')
    plt.title('Impact of Tariffs on Import Prices\n(10% Tariff on $100 Widget)', fontsize=14)
    plt.ylabel('Price in USD', fontsize=12)
    plt.ylim(0, 120)
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f'${bar.get_height():.2f}', 
                 ha='center', va='bottom', fontsize=10)
    plt.text(0.5, 0.95, 'Currency Offset Reduces Price Impact\n(2018-2019 Example)', 
             transform=plt.gca().transAxes, fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.8))
    plt.tight_layout()
    plt.savefig('tariff_offset.png')
    plt.show()

# Graphic 2: Stock Market Scenarios
def plot_stock_scenarios():
    time = np.arange(1, 13)
    baseline = 100
    scenario1 = baseline * (1 + np.linspace(0, 0.10, 12))
    scenario2 = baseline * (1 + np.linspace(0, -0.05, 6))
    scenario2 = np.concatenate([scenario2, scenario2[-1] * np.ones(6)])
    scenario3 = baseline * (1 + np.linspace(0, -0.15, 4))
    scenario3 = np.concatenate([scenario3, baseline * (1 + np.linspace(-0.15, -0.05, 8))])
    
    plt.figure(figsize=(10, 6))
    plt.plot(time, scenario1, label='Scenario 1: With Currency Offset (+5-10%)', color='#4CAF50', lw=2)
    plt.plot(time, scenario2, label='Scenario 2: No Offset (Flat to -5%)', color='#FF5733', lw=2)
    plt.plot(time, scenario3, label='Scenario 3: Retaliation (-10-15%)', color='#3498DB', lw=2)
    plt.title('S&P 500 Performance Under Tariff Scenarios\n(2025 Illustrative)', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('S&P 500 Index Value', fontsize=12)
    plt.legend(fontsize=10)
    plt.text(0.5, 0.95, 'Gradual Tariffs Favor Scenario 1\nRetaliation Risks Scenario 3', 
             transform=plt.gca().transAxes, fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.8))
    plt.tight_layout()
    plt.savefig('stock_scenarios.png')
    plt.show()

# Graphic 3: Sector Performance
def plot_sector_performance():
    sectors = ['Manufacturing', 'Retail', 'Tech', 'Energy', 'Exporters']
    performance = [5, 8, -2, 10, -5]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(sectors, performance, color=['#4CAF50', '#FF5733', '#3498DB', '#FFC107', '#9C27B0'], 
                   edgecolor='black')
    plt.title('Sector Performance Under Tariff Scenario 1\n(With Currency Offset)', fontsize=14)
    plt.ylabel('Stock Price Change (%)', fontsize=12)
    plt.ylim(-10, 15)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5 if yval >= 0 else yval - 1, f'{yval}%', 
                 ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10)
    plt.text(0.5, 0.95, 'Domestic Sectors Gain, Exporters Lag\nDue to Strong Dollar', 
             transform=plt.gca().transAxes, fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.8))
    plt.tight_layout()
    plt.savefig('sector_performance.png')
    plt.show()

if __name__ == "__main__":
    plot_tariff_offset()
    plot_stock_scenarios()
    plot_sector_performance()
