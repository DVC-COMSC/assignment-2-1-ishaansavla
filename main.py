def main():

    num_males = int(40)
    num_females = int(60)

    total = (num_males + num_females)
    m_perc = float(num_males) / total
    f_perc = float(num_females) / total


    print("")
    print(f'Number of students: {total}')
    print(f'Number of males: {num_males}')
    print(f'Number of females: {num_females}')
    print(f'Males: (format {m_perc:.2%}')
    print(f'Females: (format {f_perc:.2%}')
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
