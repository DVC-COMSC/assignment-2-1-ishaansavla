def main():
    num_males = input("How many males? ")
    num_females = input("How many females? ")

    total = (int(num_males) + int(num_females))
    m_perc = float(num_males) / float(total) * 100
    f_perc = float(num_females) / float(total) * 100

    print("")
    print(f'Number of students: {total}')
    print(f'Number of males and females: {num_males} {num_females} ')
    print(f'Percentage of males and females: {m_perc:.2%} {f_perc:.2%}')
    print("")
    return m_perc, f_perc


if __name__ == '__main__':
    main()
