from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
'''
@param N: delay in terms of slot
@param f: average secondary controller output
@param rel_stake: relative stake
@return probability of executing omerta attack
'''
def probability_of_omerta(N, f, rel_stake):
    return (1 - (1-f)**rel_stake)**N


def pair_N_f(N, f):
    stake_prob = []
    for stake_ratio in range(1,101):
        relative_stake_ratio = stake_ratio/100.0
        prob = probability_of_omerta(N, f, relative_stake_ratio)
        stake_prob += [(relative_stake_ratio, prob)]
    return stake_prob


figure = plt.figure()
#figure, axis = plt.subplots(1,5)

extent = None
def plot_security_parameter():
    count = 0
    for N in range(1, 11, 2):
        axis = figure.add_subplot(1,5, count+1)
        extent = axis.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
        for f in [0.4, 0.5, 0.6, 0.7, 0.8]:
            stake_prob = pair_N_f(N, f)
            axis.plot([item[0] for item in stake_prob], [item[1]*100 for item in stake_prob], label='f is {}'.format(f))
        axis.set_xlabel('relative stake %, N={}'.format(N))
        axis.set_ylabel('probability of winning %')
        axis.set_label('N is {}'.format(N))
        axis.set_title('N is {}'.format(N))
        axis.legend()
        count+=1

plot_security_parameter()

plt.show()
figure.savefig('prob.png', bbox_inches=extent)
#figure.set_figheight(5)
#figure.savefig('prob.png',  dpi=600)
