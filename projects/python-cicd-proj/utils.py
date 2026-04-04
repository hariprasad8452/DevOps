import numpy as np

def analyze_sales_data(sales):
    arr = np.array(sales)

    return {
        "total_sales": float(np.sum(arr)),
        "average_sales": float(np.mean(arr)),
        "max_sale": float(np.max(arr)),
        "min_sale": float(np.min(arr)),
        "std_dev": float(np.std(arr))
    }
