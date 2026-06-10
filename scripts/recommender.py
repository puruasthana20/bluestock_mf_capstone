import pandas as pd

perf_df = pd.read_csv(
    "../data/processed/clean_scheme_performance.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

recommendations = (

    perf_df[
        perf_df["risk_grade"]
        == risk
    ]

    .sort_values(
        "sharpe_ratio",
        ascending=False
    )

    .head(3)

)

print(
    recommendations[
        [
            "scheme_name",
            "sharpe_ratio"
        ]
    ]
)