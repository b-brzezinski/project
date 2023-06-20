import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm
import schemes
import matplotlib.pyplot as plt

N = 5000
M = 1000
T = 10

u=-1
D=1
values, means, sigma, p_val = schemes.distributions(u,D,M,T,N)


x = np.arange(np.amin(values),np.amax(values),0.01)
fig = go.Figure()

for step in range(100):
    fig.add_trace(
        go.Scatter(
            visible=False,
            name = f'step: {str(step)}',
            x=x,
            y=norm.pdf(x,means[int(step*N/100)],sigma[int(step*N/100)])
        )
    )
fig.data[0].visible = True

steps = []
for i in range(100):
    step = dict(
        method="update",
        args=[{"visible": [False]* 100},
              {"title": "Slider switched to step: " + str(i)}], 
    )
    step["args"][0]["visible"][i] = True 
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "snapshot: "},
    pad={"t": 100},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.write_html('plots/interactive_11.html')

fig_mu, ax_mu = plt.subplots()

ax_mu.plot(np.arange(N),means,color='red',label='numerically calculated mean')
ax_mu.plot(np.arange(N),-u*T/N*np.arange(N),color='blue',label='methematically calculated mean')
ax_mu.set_title('Mean for u=-1 and D=1')
ax_mu.set_ylabel('Mean')
ax_mu.set_xlabel('step')
fig_mu.legend()
fig_mu.set_size_inches(11.69,8.27)

fig_mu.savefig('plots/mean_11.png')
fig_sigma, ax_sigma = plt.subplots()

ax_sigma.plot(np.arange(N),sigma,color='red',label='numerically calculated SD')
ax_sigma.plot(np.arange(N),np.sqrt(2*D*T/N*np.arange(N)),color='blue',label='methematically calculated SD')
fig_sigma.legend()
ax_sigma.set_title('SD for u=-1 and D=1')
ax_sigma.set_ylabel('SD')
ax_sigma.set_xlabel('step')
fig_sigma.set_size_inches(11.69,8.27)

fig_sigma.savefig('plots/SD_11.png')

fig_p, ax_p = plt.subplots()

ax_p.plot(np.arange(N),p_val,color='red',label='Shapiro-Wilk test p-value')
ax_p.plot(np.arange(N),np.ones(N)*0.05,color='blue',label='p=0.05')
ax_p.set_title('p-value for u=-1 and D=1')
ax_p.set_ylabel('p-value')
ax_p.set_xlabel('step')
fig_p.legend()
fig_p.set_size_inches(11.69,8.27)

fig_p.savefig('plots/p_11.png')


fig_p.savefig('plots/p_11.png')
fig_hist_1,ax_hist_1 = plt.subplots()
ax_hist_1.hist(values[:,499],50)
ax_hist_1.set_title('histogram for particles for u=-1 and D=1 at T=1')
ax_hist_1.set_ylabel('count')
ax_hist_1.set_xlabel('x')
fig_hist_1.set_size_inches(11.69,8.27)

fig_hist_1.savefig('plots/hist_11_1.png')

fig_hist_5,ax_hist_5 = plt.subplots()
ax_hist_5.hist(values[:,2499],50)
ax_hist_5.set_title('histogram for particles for u=-1 and D=1 at T=5')
ax_hist_5.set_ylabel('count')
ax_hist_5.set_xlabel('x')
fig_hist_5.set_size_inches(11.69,8.27)

fig_hist_5.savefig('plots/hist_11_5.png')

fig_hist_10,ax_hist_10 = plt.subplots()
ax_hist_10.hist(values[:,4999],50)
ax_hist_10.set_title('histogram for particles for u=-1 and D=1 at T=10')
ax_hist_10.set_ylabel('count')
ax_hist_10.set_xlabel('x')
fig_hist_10.set_size_inches(11.69,8.27)

fig_hist_10.savefig('plots/hist_11_10.png')
