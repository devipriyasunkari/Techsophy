def suggest_optimizations(df):
    import pandas as pd

    # Pivot data so each service is a column and date is the index
    pivot = df.pivot_table(index="Date", columns="Service", values="Cost", aggfunc='sum').fillna(0)

    suggestions = []

    for service in pivot.columns:
        avg_cost = pivot[service].mean()
        max_cost = pivot[service].max()

        if avg_cost < 0.3:
            suggestions.append(f"Low average usage for {service}. Consider downsizing or scheduling off-hours.")
        elif max_cost > avg_cost * 2:
            suggestions.append(f"High spike in {service}. Review auto-scaling configuration.")
    
    return suggestions


