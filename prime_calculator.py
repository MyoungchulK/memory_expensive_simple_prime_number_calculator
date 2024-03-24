import sys
import click
import numpy as np

@click.command()
@click.option('-n', '--num', default = 1000, type = int)
def main(num):
    """mem expensive prime calculator
    @param num  Integer.
    """

    ## num array
    num_arr = np.arange(1, num + 1, dtype = int)

    ## residual
    resi = num_arr[:, np.newaxis] % num_arr[np.newaxis, :]

    ## zero bool
    zero_bool = resi == 0

    ## zero count
    zero_cou = np.count_nonzero(zero_bool, axis = 1)

    ## two bool
    two_bool = zero_cou == 2

    ## prime array
    prime_arr = num_arr[two_bool]

    print('Tada!')
    print(prime_arr)
    print('# of primes:', len(prime_arr))

if __name__ == "__main__":
    main()
