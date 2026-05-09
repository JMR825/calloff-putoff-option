import matplotlib.pyplot as plt
# Ask the user for inputs
option_type = input("Enter option type (call/put): ").lower().strip()
strike = float(input("Enter strike price: $"))
premium = float(input("Enter premium paid: $"))
# Simple check: premium can't be negative
if premium < 0:
    print("❌ Premium cannot be negative!")
    exit()
print(f"\n✅ Settings confirmed:")
print(f"   Option: {option_type.upper()}")
print(f"   Strike: ${strike}")
print(f"   Premium: ${premium}")
stock_prices=list(range(50,151,5))
# Gross Payoffs (never negative)
call_gross = [max(s - strike, 0) for s in stock_prices]
put_gross  = [max(strike - s, 0) for s in stock_prices]

# Net Profits (Gross - Premium)
call_net = [g - premium for g in call_gross]
put_net  = [g - premium for g in put_gross]
if option_type == 'call':
    net_profits = call_net
else:
    net_profits = put_net
print("\n📊 Quick Check (First 5 prices):")
for i in range(5):
    print(f"Stock: ${stock_prices[i]:>3.0f}  →  Net Profit: ${net_profits[i]:.2f}")
    # --- PART 3: PLOTTING ---

# 1. Create a blank canvas
plt.figure(figsize=(10, 6))

# 2. Plot the Net Profit line
plt.plot(stock_prices, net_profits, linewidth=2, color='blue', label='Net Profit/Loss')

# 3. Draw a horizontal line at $0 (the breakeven axis)
plt.axhline(0, color='black', linewidth=1, linestyle='-')

# 4. Draw a vertical dashed line at the Strike Price
plt.axvline(strike, color='gray', linestyle='--', linewidth=1, label=f'Strike Price (${strike})')

# 5. Calculate & mark the Breakeven point
if option_type == 'call':
    breakeven = strike + premium
else:
    breakeven = strike - premium

plt.axvline(breakeven, color='red', linestyle='--', linewidth=1, label=f'Breakeven (${breakeven})')

# 6. Add labels, title, and grid
plt.title(f'{option_type.capitalize()} Option Payoff Diagram', fontsize=14)
plt.xlabel('Stock Price at Expiry ($)', fontsize=12)
plt.ylabel('Net Profit / Loss ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

# 7. Show the plot
plt.show()