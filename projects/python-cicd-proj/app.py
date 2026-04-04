from utils import analyze_sales_data

def main():
    # Simulated real-world data (daily sales)
    sales_data = [120, 340, 560, 230, 450, 390, 610]

    report = analyze_sales_data(sales_data)

    print("📊 Sales Analysis Report")
    print("-" * 30)

    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
