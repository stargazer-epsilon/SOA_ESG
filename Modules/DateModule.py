# This module processes dates expressed in YYYYMM form

def month_of(a_date):
    """Returns the month of a given date."""
    return a_date % 100

def year_of(a_date):
    """Returns the year of a given date."""
    return a_date // 100

def months_between(a_date1, a_date2):
    """Returns a positive result only if aDate2 is after aDate1."""
    return 12 * (year_of(a_date2) - year_of(a_date1)) + month_of(a_date2) - month_of(a_date1)

def future_date(current_date, months):
    """Returns a date some months in the future."""
    future_month = (month_of(current_date) + months) % 12
    if future_month == 0: 
        future_month = 12
    future_date = 100 * (year_of(current_date) + (months // 12)) + future_month
    if future_month < month_of(current_date):
        future_date = future_date + 100
    return future_date

def prior_date(current_date, months):
    """Returns a date some months in the past."""
    prior_year = year_of(current_date) - (months // 12)
    prior_month = month_of(current_date) - (months % 12)
    if prior_month < 1:
        prior_month = prior_month + 12
        prior_year = prior_year - 1
    return (100 * prior_year) + prior_month
