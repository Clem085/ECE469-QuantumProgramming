import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from qiskit.quantum_info import Statevector
import colorcet as cc

def sv_disc(sv, show_labels=True, phase_colors=False, num_columns=None):
    '''
    Display state vector using multidisc format, adapted from 
    'Programming Quantum Computers: Essential Algorithms and Code Samples', 
    by Johnston, Harrigan, and Gimeno-Segovia (O'Reilly, 2019).
    
    Each computational basis state is represented by a disc. 
    Magnitude is the radius of a shaded circle in the disc. 
    Phase is a CCW-rotated line. 
    If phase_colors is True, magnitude is colored according to phase.
    
    Parameters:
        sv (qiskit.quantum_info.Statevector): state vector
        show_labels (bool): print binary number for each state (default = True)
        phase_colors (bool): apply color map to magnitude (default = False)
        num_columns (int): maximum number of discs in each row; 
            if None, uses 8 if vector size <= 32, otherwise 16
    '''
    plt.ioff()  # don't draw as fig is created -- return fig instead
    ndiscs = sv.dim
    maxcols = 0
    if num_columns is None:
        maxcols = 8 if (sv.dim <= 32) else 16
    else:
        maxcols = num_columns
    ncols = min(sv.dim,maxcols)  # no more than maxcol columns
    nrows = ndiscs // ncols 
    if nrows*ncols != ndiscs:
        nrows += 1
    #colormap = cc.cm.cyclic_mybm_20_100_c48_s25
    colormap = cc.cm.cyclic_isoluminant

    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=[1.5*ncols,1.5*nrows], gridspec_kw = {'wspace':0, 'hspace':0})
    axs = axs.flat
    for i in range(0,nrows*ncols):
        axs[i].set_axis_off()
        if show_labels:
            axs[i].set_xlim(-1.5,1.5)
            axs[i].set_ylim(-1.5,1.5)
            
        else:
            axs[i].set_xlim(-1.2,1.2)
            axs[i].set_ylim(-1.2,1.2)
        if i < ndiscs:
            if show_labels: axs[i].text(0, 1.25, "{:0{width}b}".format(i,width=sv.num_qubits), ha='center', size='large')
            disc = plt.Circle((0,0),1, ec='k',fc='w',zorder=0)
            axs[i].add_patch(disc)
    for i in range(0,ndiscs):
        r = np.abs(sv.data[i])
        t = 0
        if r > 1e-5:
            t = np.angle(sv.data[i])
            if t < 0: t = 2*np.pi + t
            px = np.cos(t+(np.pi/2))
            py = np.sin(t+(np.pi/2))
            axs[i].plot([0,px],[0, py],linewidth=1.0,color='k',zorder=10, markevery=(1,1), marker='o', markersize=5)
            #axs[i].scatter(px,py,15, c='k')
        color = fc=colormap(t/(2*np.pi)) if (phase_colors) else colormap(0)
        mag = plt.Circle((0,0), r, fc=color, zorder=5)
        axs[i].add_patch(mag)
    return fig


def sv_disc_update(fig, sv):
    for i in range(0, sv.dim):
        ax = fig.axes[i]
        # update angle
        t = np.angle(sv.data[i])
        if t < 0: t = 2*np.pi + t
        px = np.cos(t+(np.pi/2))
        py = np.sin(t+(np.pi/2))
        ax.findobj(plt.Line2D)[0].set(data=[[0,px],[0,py]])
        # update magnitude
        ax.patches[1].set_radius(np.abs(sv.data[i]))
    return
