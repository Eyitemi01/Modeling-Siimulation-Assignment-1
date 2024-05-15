def simple_interest_loan(principal, annual_interest_rate, num_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_months = num_years * 12
    monthly_payment = principal * (1 + monthly_interest_rate * num_years) / num_months
    
    total_payment = 0
    remaining_principal = principal
    
    print("Month\tRemaining Principal\tPayment")
    for month in range(1, num_months + 1):
        interest_payment = remaining_principal * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_principal -= principal_payment
        total_payment += monthly_payment
        
        print(f"{month}\t{round(remaining_principal, 2)}\t\t{round(monthly_payment, 2)}")
    
    print(f"\nTotal Payment: {round(total_payment, 2)}")


# Example usage
principal = 10000
annual_interest_rate = 10
num_years = 2

simple_interest_loan(principal, annual_interest_rate, num_years)