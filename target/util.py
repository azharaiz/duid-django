# Program to calculate compound interest with monthly contribution at end of
# month
# Credit :
# https://www.instructables.com
# /Python-Compounding-Interest-With-Monthly-Deposit/
def monthly_deposit_calculator(principal, annualrate,
                               years, target):
    numberoftimescompounded = 12
    if target <= principal or years == 0:
        return 0
    preliminarynumber = (1 + (annualrate / numberoftimescompounded))
    raisedtopower = (numberoftimescompounded * years)
    compoundinterestplusprincipal = principal * (
            preliminarynumber ** raisedtopower)
    if annualrate <= 0:
        return target / (years * 12)
    oneplus = (1 + (annualrate / numberoftimescompounded))
    raisedtopower2 = (numberoftimescompounded * years)
    ratedividedbynumberoftimes = annualrate / numberoftimescompounded
    halfdone = (((oneplus ** raisedtopower2) - 1) / ratedividedbynumberoftimes)
    return (target - compoundinterestplusprincipal) / halfdone
