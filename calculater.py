# make function called get_corp_val
# make function called get_proper_stock


def get_corp_val1(equity_capital, roe, required_roe):
    corp_val = equity_capital + equity_capital * (roe - required_roe) / required_roe
    return corp_val


def get_corp_val2(equity_capital, roe, required_roe, w):
    # Apply increase or decrease of ROE
    corp_val = equity_capital + equity_capital * (roe - required_roe) * w / (1 + required_roe - w)
    return corp_val


def get_proper_stock(corp_value, t_issued_stock):
    proper_stock = corp_value / t_issued_stock
    return proper_stock


def print_results(
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
):
    print("분석결과")
    print(f"20%씩 ROE가 오를경우 기업가치(시가총액): {int(corp_value_inc2)} & 주가: {int(proper_stock_inc2)}")
    print(f"10%씩 ROE가 오를경우 기업가치(시가총액): {int(corp_value_inc1)} & 주가: {int(proper_stock_inc1)}")
    print(f"ROE각 영원히 지속될 경우 기업가치(시가총액): {int(corp_value)} & 주가: {int(proper_stock)}")
    print(f"10%씩 ROE가 떨어질 경우 기업가치(시가총액): {int(corp_value_dec1)} & 주가: {int(proper_stock_dec1)}")
    print(f"20%씩 ROE가 떨어질 경우 기업가치(시가총액): {int(corp_value_dec2)} & 주가: {int(proper_stock_dec2)}")

