from calculater import get_corp_val1, get_corp_val2, get_proper_stock, print_results

# Input shareholder equity, ROE, required ROE, total issued stock
# Print corp_val and proper_stock
# TODO: Scraping kisrating.com -> Get required ROE

print("Put which corporate you want to know")
corp = input(">")
print(f"Company name: {corp}")
equity_capital = float(input("Put controlling shareholder equity: "))
roe = float(input("Put ROE: ")) / 100
required_roe = float(input("Put required ROE: ")) / 100
t_issued_stock = float(input("Put the total issued stock: "))

corp_value_inc2 = get_corp_val2(equity_capital, roe, required_roe, 1.2)
corp_value_inc1 = get_corp_val2(equity_capital, roe, required_roe, 1.1)
corp_value = get_corp_val2(equity_capital, roe, required_roe, 1)
corp_value_dec1 = get_corp_val2(equity_capital, roe, required_roe, 0.9)
corp_value_dec2 = get_corp_val2(equity_capital, roe, required_roe, 0.8)

proper_stock_inc2 = get_proper_stock(corp_value_inc2, t_issued_stock)
proper_stock_inc1 = get_proper_stock(corp_value_inc1, t_issued_stock)
proper_stock = get_proper_stock(corp_value, t_issued_stock)
proper_stock_dec1 = get_proper_stock(corp_value_dec1, t_issued_stock)
proper_stock_dec2 = get_proper_stock(corp_value_dec2, t_issued_stock)

print_results(
    corp_value_inc2,
    corp_value_inc1,
    corp_value,
    corp_value_dec1,
    corp_value_dec2,
    proper_stock_inc2,
    proper_stock_inc1,
    proper_stock,
    proper_stock_dec1,
    proper_stock_dec2,
)

