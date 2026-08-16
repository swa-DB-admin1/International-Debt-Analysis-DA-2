QUERIES = {

    # ============================================================
    # BASIC LEVEL
    # ============================================================

    1: {
        "question": "Retrieve all distinct country names",
        "sql": """
            SELECT DISTINCT country_name
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
            ORDER BY country_name;
        """
    },

    2: {
        "question": "Count the total number of countries",
        "sql": """
            SELECT COUNT(DISTINCT country_name) AS total_countries
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL;
        """
    },

    3: {
        "question": "Find the total number of indicators",
        "sql": """
            SELECT COUNT(DISTINCT series_name) AS total_indicators
            FROM allcountries_debt_data
            WHERE series_name IS NOT NULL;
        """
    },

    4: {
        "question": "Display the first 10 records",
        "sql": """
            SELECT *
            FROM allcountries_debt_data
            LIMIT 10;
        """
    },

    5: {
        "question": "Calculate the total global debt",
        "sql": """
            SELECT
                SUM(debt_value) AS total_global_debt
            FROM allcountries_debt_data
            WHERE debt_value IS NOT NULL;
        """
    },

    6: {
        "question": "List all unique indicator names",
        "sql": """
            SELECT DISTINCT series_name AS indicator
            FROM allcountries_debt_data
            WHERE series_name IS NOT NULL
            ORDER BY series_name;
        """
    },

    7: {
        "question": "Find the number of records for each country",
        "sql": """
            SELECT
                country_name,
                COUNT(*) AS record_count
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
            GROUP BY country_name
            ORDER BY record_count DESC;
        """
    },

    8: {
        "question": "Display all records where debt is greater than 1 billion USD",
        "sql": """
            SELECT *
            FROM allcountries_debt_data
            WHERE debt_value > 1000000000
            ORDER BY debt_value DESC;
        """
    },

    9: {
        "question": "Find minimum, maximum and average debt",
        "sql": """
            SELECT
                MIN(debt_value) AS minimum_debt,
                MAX(debt_value) AS maximum_debt,
                AVG(debt_value) AS average_debt
            FROM allcountries_debt_data
            WHERE debt_value IS NOT NULL;
        """
    },

    10: {
        "question": "Count total number of records",
        "sql": """
            SELECT COUNT(*) AS total_records
            FROM allcountries_debt_data;
        """
    },


    # ============================================================
    # INTERMEDIATE LEVEL
    # ============================================================

    11: {
        "question": "Find total debt for each country",
        "sql": """
            SELECT
                country_name,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY total_debt DESC;
        """
    },

    12: {
        "question": "Display top 10 countries with the highest total debt",
        "sql": """
            SELECT
                country_name,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY total_debt DESC
            LIMIT 10;
        """
    },

    13: {
        "question": "Find average debt per country",
        "sql": """
            SELECT
                country_name,
                AVG(debt_value) AS average_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY average_debt DESC;
        """
    },

    14: {
        "question": "Calculate total debt for each indicator",
        "sql": """
            SELECT
                series_name AS indicator,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE series_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY series_name
            ORDER BY total_debt DESC;
        """
    },

    15: {
        "question": "Identify the indicator contributing the highest total debt",
        "sql": """
            SELECT
                series_name AS indicator,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE series_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY series_name
            ORDER BY total_debt DESC
            LIMIT 1;
        """
    },

    16: {
        "question": "Find the country with the lowest total debt",
        "sql": """
            SELECT
                country_name,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY total_debt ASC
            LIMIT 1;
        """
    },

    17: {
        "question": "Calculate total debt for each country and indicator combination",
        "sql": """
            SELECT
                country_name,
                series_name AS indicator,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND series_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name, series_name
            ORDER BY total_debt DESC;
        """
    },

    18: {
        "question": "Count how many indicators each country has",
        "sql": """
            SELECT
                country_name,
                COUNT(DISTINCT series_name) AS indicator_count
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND series_name IS NOT NULL
            GROUP BY country_name
            ORDER BY indicator_count DESC;
        """
    },

    19: {
        "question": "Display countries whose total debt is above the global average",
        "sql": """
            SELECT
                country_name,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            HAVING SUM(debt_value) >
            (
                SELECT AVG(country_total)
                FROM
                (
                    SELECT
                        country_name,
                        SUM(debt_value) AS country_total
                    FROM allcountries_debt_data
                    WHERE country_name IS NOT NULL
                      AND debt_value IS NOT NULL
                    GROUP BY country_name
                ) AS country_totals
            )
            ORDER BY total_debt DESC;
        """
    },

    20: {
        "question": "Rank countries based on total debt",
        "sql": """
            SELECT
                country_name,
                total_debt,
                RANK() OVER (
                    ORDER BY total_debt DESC
                ) AS debt_rank
            FROM
            (
                SELECT
                    country_name,
                    SUM(debt_value) AS total_debt
                FROM allcountries_debt_data
                WHERE country_name IS NOT NULL
                  AND debt_value IS NOT NULL
                GROUP BY country_name
            ) AS country_debt
            ORDER BY debt_rank;
        """
    },


    # ============================================================
    # ADVANCED LEVEL
    # ============================================================

    21: {
        "question": "Find the top 5 indicators contributing most to global debt",
        "sql": """
            SELECT
                series_name AS indicator,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE series_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY series_name
            ORDER BY total_debt DESC
            LIMIT 5;
        """
    },

    22: {
        "question": "Calculate percentage contribution of each country to total global debt",
        "sql": """
            SELECT
                country_name,
                SUM(debt_value) AS total_debt,
                ROUND(
                    SUM(debt_value) * 100.0 /
                    (
                        SELECT SUM(debt_value)
                        FROM allcountries_debt_data
                        WHERE debt_value IS NOT NULL
                    ),
                    2
                ) AS contribution_percentage
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY contribution_percentage DESC;
        """
    },

    23: {
        "question": "Identify the top 3 countries for each indicator based on debt",
        "sql": """
            SELECT
                indicator,
                country_name,
                total_debt,
                indicator_rank
            FROM
            (
                SELECT
                    series_name AS indicator,
                    country_name,
                    SUM(debt_value) AS total_debt,
                    RANK() OVER (
                        PARTITION BY series_name
                        ORDER BY SUM(debt_value) DESC
                    ) AS indicator_rank
                FROM allcountries_debt_data
                WHERE series_name IS NOT NULL
                  AND country_name IS NOT NULL
                  AND debt_value IS NOT NULL
                GROUP BY series_name, country_name
            ) AS ranked_data
            WHERE indicator_rank <= 3
            ORDER BY indicator, indicator_rank;
        """
    },

    24: {
        "question": "Find the difference between maximum and minimum debt for each country",
        "sql": """
            SELECT
                country_name,
                MAX(debt_value) AS maximum_debt,
                MIN(debt_value) AS minimum_debt,
                MAX(debt_value) - MIN(debt_value) AS debt_difference
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY debt_difference DESC;
        """
    },

    25: {
        "question": "Create a view for the top 10 countries with highest debt",
        "sql": """
            CREATE OR REPLACE VIEW top_10_countries_debt AS
            SELECT
                country_name,
                SUM(debt_value) AS total_debt
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            ORDER BY total_debt DESC
            LIMIT 10;
        """
    },

    26: {
        "question": "Categorize countries into High, Medium and Low Debt",
        "sql": """
            WITH country_debt AS
            (
                SELECT
                    country_name,
                    SUM(debt_value) AS total_debt
                FROM allcountries_debt_data
                WHERE country_name IS NOT NULL
                  AND debt_value IS NOT NULL
                GROUP BY country_name
            ),
            debt_stats AS
            (
                SELECT
                    AVG(total_debt) AS avg_debt,
                    STDDEV(total_debt) AS std_debt
                FROM country_debt
            )
            SELECT
                c.country_name,
                c.total_debt,
                CASE
                    WHEN c.total_debt > s.avg_debt + s.std_debt
                        THEN 'High Debt'
                    WHEN c.total_debt >= s.avg_debt
                        THEN 'Medium Debt'
                    ELSE 'Low Debt'
                END AS debt_category
            FROM country_debt c
            CROSS JOIN debt_stats s
            ORDER BY c.total_debt DESC;
        """
    },

    27: {
        "question": "Calculate cumulative debt per country using window functions",
        "sql": """
            WITH yearly_debt AS
            (
                SELECT
                    country_name,
                    year,
                    SUM(debt_value) AS yearly_debt
                FROM allcountries_debt_data
                WHERE country_name IS NOT NULL
                  AND debt_value IS NOT NULL
                GROUP BY country_name, year
            )
            SELECT
                country_name,
                year,
                yearly_debt,
                SUM(yearly_debt) OVER (
                    PARTITION BY country_name
                    ORDER BY year
                    ROWS BETWEEN UNBOUNDED PRECEDING
                    AND CURRENT ROW
                ) AS cumulative_debt
            FROM yearly_debt
            ORDER BY country_name, year;
        """
    },

    28: {
        "question": "Find indicators where average debt is higher than overall average debt",
        "sql": """
            SELECT
                series_name AS indicator,
                AVG(debt_value) AS average_debt
            FROM allcountries_debt_data
            WHERE series_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY series_name
            HAVING AVG(debt_value) >
            (
                SELECT AVG(debt_value)
                FROM allcountries_debt_data
                WHERE debt_value IS NOT NULL
            )
            ORDER BY average_debt DESC;
        """
    },

    29: {
        "question": "Identify countries contributing more than 5% of global debt",
        "sql": """
            SELECT
                country_name,
                SUM(debt_value) AS total_debt,
                ROUND(
                    SUM(debt_value) * 100.0 /
                    (
                        SELECT SUM(debt_value)
                        FROM allcountries_debt_data
                        WHERE debt_value IS NOT NULL
                    ),
                    2
                ) AS contribution_percentage
            FROM allcountries_debt_data
            WHERE country_name IS NOT NULL
              AND debt_value IS NOT NULL
            GROUP BY country_name
            HAVING contribution_percentage > 5
            ORDER BY contribution_percentage DESC;
        """
    },

    30: {
        "question": "Find the most dominant indicator for each country",
        "sql": """
            SELECT
                country_name,
                indicator,
                total_debt
            FROM
            (
                SELECT
                    country_name,
                    series_name AS indicator,
                    SUM(debt_value) AS total_debt,
                    RANK() OVER (
                        PARTITION BY country_name
                        ORDER BY SUM(debt_value) DESC
                    ) AS indicator_rank
                FROM allcountries_debt_data
                WHERE country_name IS NOT NULL
                  AND series_name IS NOT NULL
                  AND debt_value IS NOT NULL
                GROUP BY country_name, series_name
            ) AS ranked_indicators
            WHERE indicator_rank = 1
            ORDER BY country_name;
        """
    }
}