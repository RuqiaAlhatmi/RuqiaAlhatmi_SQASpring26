# Job Market Trends Analysis System
# Algorithm: Analyze job posting by sector, experience level, and salary range
# Implements: switch (via dictionary dispatch) + if-else for salary band classification

def classify_salary_band(salary):
    """Classify salary into quality band using if-else."""
    if salary < 0:
        return "Invalid"
    elif salary < 25000:
        return "Entry-Level Band"
    elif salary < 50000:
        return "Mid-Level Band"
    elif salary < 80000:
        return "Senior Band"
    elif salary < 120000:
        return "Lead/Principal Band"
    else:
        return "Executive Band"

def analyze_sector(sector_code):
    """Analyze employment sector using switch-like dispatch."""
    sector_map = {
        1: "Technology",
        2: "Healthcare",
        3: "Finance",
        4: "Education",
        5: "Manufacturing"
    }
    sector_name = sector_map.get(sector_code, "Unknown Sector")
    return sector_name

def analyze_job_posting(sector_code, experience_years, salary):
    """
    Main analysis function for a single job posting.
    Returns a structured analysis result.
    """
    sector = analyze_sector(sector_code)
    salary_band = classify_salary_band(salary)

    if sector == "Unknown Sector":
        status = "REJECTED"
        recommendation = "Invalid sector code. Cannot process."
    else:
        if experience_years < 0:
            status = "REJECTED"
            recommendation = "Invalid experience value."
        elif experience_years < 2:
            level = "Junior"
            if salary > 60000:
                status = "FLAGGED"
                recommendation = "Salary unusually high for junior position. Review required."
            else:
                status = "APPROVED"
                recommendation = f"Junior posting in {sector}. Salary band: {salary_band}."
        elif experience_years < 5:
            level = "Mid"
            if salary < 30000:
                status = "FLAGGED"
                recommendation = "Salary below market for mid-level. Review required."
            else:
                status = "APPROVED"
                recommendation = f"Mid-level posting in {sector}. Salary band: {salary_band}."
        else:
            level = "Senior"
            if salary < 50000:
                status = "FLAGGED"
                recommendation = "Salary below market for senior role. Review required."
            else:
                status = "APPROVED"
                recommendation = f"Senior posting in {sector}. Salary band: {salary_band}."

    return {
        "sector": sector,
        "salary_band": salary_band,
        "status": status,
        "recommendation": recommendation
    }

def main():
    print("=== Job Market Trends Analysis System ===\n")
    test_cases = [
        (1, 1, 45000),   # Tech, Junior, normal salary
        (2, 3, 62000),   # Healthcare, Mid, normal
        (3, 7, 95000),   # Finance, Senior, normal
        (6, 2, 40000),   # Unknown sector
        (4, 1, 75000),   # Education Junior, high salary -> FLAGGED
    ]
    for sector_code, exp, salary in test_cases:
        result = analyze_job_posting(sector_code, exp, salary)
        print(f"Sector Code: {sector_code} | Exp: {exp}yrs | Salary: ${salary:,}")
        print(f"  -> Sector: {result['sector']}")
        print(f"  -> Band:   {result['salary_band']}")
        print(f"  -> Status: {result['status']}")
        print(f"  -> Note:   {result['recommendation']}")
        print()

if __name__ == "__main__":
    main()
