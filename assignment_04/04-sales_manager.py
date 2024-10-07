# Requirements for Sales Manager Position
MIN_YEARS_SALES = 2
MIN_YEARS_TOP_AWARD = 1

# User's provided data:
years_sales = int(input('Enter your years of sales experience: '))
years_top_award = int(input('Enter how many years you have been salesperson of the year: ')) # any error would be user error in this case.

if years_sales >= MIN_YEARS_SALES and years_top_award >= MIN_YEARS_TOP_AWARD:
    print('You are eligible the Sales Manager Position.')
else:
    print('You are not eligible for the Sales Manager Position.')
    if MIN_YEARS_SALES > years_sales:
        print('You do not meet the minimum years in sales.')
    if MIN_YEARS_TOP_AWARD > years_top_award:
        print('You do not meet the minimum for the years as salesperson of the year.')
