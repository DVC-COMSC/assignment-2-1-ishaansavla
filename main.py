def main():

    males = float(input("How many male students? "))
    females = float(input("How many female students? "))

    total = (males + females)
    m_perc = format(float(males / total), '.2%')
    f_perc = format(float(females / total),'.2%')


    print("")
    print(f'Males: {m_perc}')
    print(f'Females: {f_perc}')
    print("")

    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """


    return m_perc, f_perc


if __name__ == '__main__':
    main()
