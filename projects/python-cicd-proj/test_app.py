from utils import analyze_sales_data

def test_sales_analysis():
    data = [10, 20, 30]

    result = analyze_sales_data(data)

    assert result["total_sales"] == 60
    assert result["average_sales"] == 20
